import pytest
from pyspark.sql import SparkSession

from src.spark.joins import aggregate_to_order_grain
from src.spark.kpis import order_kpis, payment_kpis, revenue_kpis, review_kpis


@pytest.fixture(scope="session")
def spark():
    s = SparkSession.builder.master("local[1]").appName("tests").getOrCreate()
    s.conf.set("spark.sql.shuffle.partitions", "1")
    yield s


@pytest.fixture
def items_df(spark):
    """
    Item-level table (one row per order item), as produced by the pipeline.
      o1: 2 items (100 + 50), rated 5, paid 150, delivered in 5 days, on time
      o2: 1 item (200), rated 1, paid 200, delivered in 10 days, 3 days late
      o3: no items, rated 4, paid 100
    """
    schema = (
        "order_id string, order_status string, purchase_year_month string, "
        "product_category_name_english string, order_item_id int, "
        "total_order_item_value double, delivery_time_days int, "
        "delivery_delay_days int, payment_type string, payment_installments int, "
        "payment_value double, review_id string, review_score int"
    )
    rows = [
        ("o1", "delivered", "2017-01", "toys", 1, 100.0, 5, -2, "credit_card", 3, 150.0, "r1", 5),
        ("o1", "delivered", "2017-01", "toys", 2, 50.0, 5, -2, "credit_card", 3, 150.0, "r1", 5),
        ("o2", "delivered", "2017-02", "books", 1, 200.0, 10, 3, "boleto", 1, 200.0, "r2", 1),
        ("o3", "canceled", "2017-02", None, None, 0.0, None, None, "voucher", 1, 100.0, "r3", 4),
    ]
    return spark.createDataFrame(rows, schema)


def test_total_revenue_and_aov(items_df):
    result = revenue_kpis(items_df)
    assert result["total_revenue"] == 350.0
    # AOV excludes the order with no items: (150 + 200) / 2
    assert result["average_order_value"] == 175.0


def test_order_kpis_count_orders_not_rows(items_df):
    result = order_kpis(items_df)
    assert result["total_orders"] == 3
    assert result["delayed_orders"] == 1
    # delivery time is averaged per order: (5 + 10) / 2
    assert result["average_delivery_time_days"] == 7.5


def test_review_kpis_count_reviews_not_item_rows(items_df):
    result = review_kpis(items_df)
    # 3 reviews, not 4 item rows
    assert sum(result["rating_distribution"].values()) == 3
    assert result["average_review_rating"] == 3.33


def test_payment_kpis_are_order_level(items_df):
    result = payment_kpis(items_df)
    assert result["average_payment_value"] == 150.0  # (150 + 200 + 100) / 3
    assert result["average_installments"] == 1.67


def test_aggregate_to_order_grain_and_no_fanout(spark):
    items = spark.createDataFrame(
        [("o1", 10.0), ("o1", 20.0), ("o2", 30.0)],
        "order_id string, price double",
    )
    payments = spark.createDataFrame(
        [
            ("o1", "credit_card", 3, 100.0),
            ("o1", "voucher", 1, 50.0),
            ("o2", "boleto", 1, 200.0),
        ],
        "order_id string, payment_type string, payment_installments int, payment_value double",
    )
    reviews = spark.createDataFrame(
        [
            ("o1", "r_old", 1, "2017-01-01 00:00:00"),
            ("o1", "r_new", 5, "2017-01-05 00:00:00"),
            ("o2", "r2", 4, "2017-02-01 00:00:00"),
        ],
        "order_id string, review_id string, review_score int, review_answer_timestamp string",
    )

    pay_agg, rev_dedup = aggregate_to_order_grain(payments, reviews)

    # one row per order after aggregation
    assert pay_agg.count() == 2
    assert rev_dedup.count() == 2

    o1 = pay_agg.filter("order_id = 'o1'").first()
    assert o1["payment_value"] == 150.0
    assert o1["payment_type"] == "credit_card"  # the largest payment
    assert rev_dedup.filter("order_id = 'o1'").first()["review_id"] == "r_new"  # latest review

    # joining back onto items must not duplicate item rows
    merged = items.join(pay_agg, "order_id", "left").join(rev_dedup, "order_id", "left")
    assert merged.count() == items.count()