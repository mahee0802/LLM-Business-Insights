from pyspark.sql import functions as F
from pyspark.sql.window import Window
from src.spark.load_data import (
    load_orders,
    load_customers,
    load_order_items,
    load_products,
    load_payments,
    load_reviews,
    load_sellers,
    load_translation
)
def aggregate_to_order_grain(payments, reviews):
    """Collapse payments and reviews to one row per order_id before joining."""
    w_pay = Window.partitionBy("order_id").orderBy(F.col("payment_value").desc())
    top_payment = (
        payments.withColumn("rn", F.row_number().over(w_pay))
        .filter("rn = 1")
        .select("order_id", "payment_type")
    )
    payments_agg = (
        payments.groupBy("order_id")
        .agg(
            F.max("payment_installments").alias("payment_installments"),
            F.sum("payment_value").alias("payment_value"),
        )
        .join(top_payment, "order_id")
    )

    w_rev = Window.partitionBy("order_id").orderBy(F.col("review_answer_timestamp").desc())
    reviews_dedup = (
        reviews.withColumn("rn", F.row_number().over(w_rev))
        .filter("rn = 1")
        .drop("rn")
    )
    return payments_agg, reviews_dedup
def merge_datasets():
    orders = load_orders()
    customers = load_customers()
    order_items = load_order_items()
    products = load_products()
    payments = load_payments()
    reviews = load_reviews()
    sellers = load_sellers()
    translation = load_translation()
    payments, reviews = aggregate_to_order_grain(payments, reviews)
    business_df = orders.join(
        customers,
        on="customer_id",
        how="left"
    )
    # Order Items
    business_df = business_df.join(
        order_items,
        on="order_id",
        how="left"
    )
    # Products
    business_df = business_df.join(
        products,
        on="product_id",
        how="left"
    )
    # Category Translation
    business_df = business_df.join(
        translation,
        on="product_category_name",
        how="left"
    )
    # Payments
    business_df = business_df.join(
        payments,
        on="order_id",
        how="left"
    )
    # Reviews
    business_df = business_df.join(
        reviews,
        on="order_id",
        how="left"
    )
    # Sellers
    business_df = business_df.join(
        sellers,
        on="seller_id",
        how="left"
    )
    return business_df