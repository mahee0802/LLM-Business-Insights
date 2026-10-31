import pandas as pd
import pytest

from src.analysis.generate_kpis import (
    order_kpis,
    payment_kpis,
    review_kpis,
    revenue_kpis,
)
from src.data.build_business_dataset import aggregate_to_order_grain


@pytest.fixture
def items_df():
    """
    Item-level table (one row per order item), as in business_master.csv.
      o1: 2 items (100 + 50), rated 5, paid 150, delivered in 5 days, on time
      o2: 1 item (200), rated 1, paid 200, delivered in 10 days, 3 days late
      o3: no items (NaN value), rated 4, paid 100
    """
    return pd.DataFrame({
        "order_id": ["o1", "o1", "o2", "o3"],
        "order_status": ["delivered", "delivered", "delivered", "canceled"],
        "purchase_year_month": ["2017-01", "2017-01", "2017-02", "2017-02"],
        "product_category_name_english": ["toys", "toys", "books", None],
        "order_item_id": [1, 2, 1, None],
        "price": [90.0, 45.0, 180.0, None],
        "total_order_item_value": [100.0, 50.0, 200.0, None],
        "delivery_time_days": [5.0, 5.0, 10.0, None],
        "delivery_delay_days": [-2.0, -2.0, 3.0, None],
        "payment_type": ["credit_card", "credit_card", "boleto", "voucher"],
        "payment_installments": [3.0, 3.0, 1.0, 1.0],
        "payment_value": [150.0, 150.0, 200.0, 100.0],
        "review_id": ["r1", "r1", "r2", "r3"],
        "review_score": [5.0, 5.0, 1.0, 4.0],
    })


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


def test_aggregate_to_order_grain():
    payments = pd.DataFrame({
        "order_id": ["o1", "o1", "o2"],
        "payment_type": ["credit_card", "voucher", "boleto"],
        "payment_installments": [3, 1, 1],
        "payment_value": [100.0, 50.0, 200.0],
    })
    reviews = pd.DataFrame({
        "order_id": ["o1", "o1", "o2"],
        "review_id": ["r_old", "r_new", "r2"],
        "review_score": [1, 5, 4],
        "review_answer_timestamp": pd.to_datetime(
            ["2017-01-01", "2017-01-05", "2017-02-01"]
        ),
    })

    pay_agg, rev_dedup = aggregate_to_order_grain(payments, reviews)

    assert pay_agg["order_id"].is_unique
    assert rev_dedup["order_id"].is_unique
    row = pay_agg.set_index("order_id").loc["o1"]
    assert row["payment_value"] == 150.0
    assert row["payment_type"] == "credit_card"  # the largest payment
    assert rev_dedup.set_index("order_id").loc["o1", "review_id"] == "r_new"


def test_join_does_not_duplicate_items():
    items = pd.DataFrame({"order_id": ["o1", "o1", "o2"], "price": [10, 20, 30]})
    payments = pd.DataFrame({
        "order_id": ["o1", "o1", "o2"],
        "payment_type": ["credit_card", "voucher", "boleto"],
        "payment_installments": [1, 1, 1],
        "payment_value": [20.0, 10.0, 30.0],
    })
    reviews = pd.DataFrame({
        "order_id": ["o1", "o2"],
        "review_id": ["r1", "r2"],
        "review_score": [5, 4],
        "review_answer_timestamp": pd.to_datetime(["2017-01-01", "2017-01-02"]),
    })

    pay_agg, rev_dedup = aggregate_to_order_grain(payments, reviews)
    merged = items.merge(pay_agg, on="order_id", how="left").merge(
        rev_dedup, on="order_id", how="left"
    )

    assert len(merged) == len(items)  # no fan-out
    assert merged["price"].sum() == items["price"].sum()