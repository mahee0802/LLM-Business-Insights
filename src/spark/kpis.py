from pyspark.sql.functions import (col,desc,sum,avg,count,countDistinct,round as spark_round,max,min,when)
from src.spark.joins import merge_datasets
from src.spark.transform import transform_data
from src.spark.feature_engineering import create_features
import json
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parents[2]
PROCESSED_DATA = BASE_DIR / "data" / "processed"
def revenue_kpis(df):
    revenue = {}
    # KPI 1 : Total Revenue
    total_revenue = (df.agg(spark_round(sum("total_order_item_value"),2).alias("total_revenue")).first()["total_revenue"])
    revenue["total_revenue"] = float(total_revenue)
    # KPI 2 : Average Order Value
    order_totals = (df.groupBy("order_id").agg(sum("total_order_item_value").alias("order_total")))
    avg_order_value = (order_totals.agg(spark_round(avg("order_total"),2).alias("average_order_value")).first()["average_order_value"])
    revenue["average_order_value"] = float(avg_order_value)
    # KPI 3 : Monthly Revenue Trend
    monthly_revenue = (df.groupBy("purchase_year_month").agg(spark_round(sum("total_order_item_value"),2).alias("revenue")).orderBy("purchase_year_month"))
    revenue["monthly_revenue"] = {
    row["purchase_year_month"]: float(row["revenue"])
    for row in monthly_revenue.collect()
    if row["revenue"] is not None}
    # KPI 4 : Revenue by Product Category
    category_revenue = (
        df.groupBy("product_category_name_english")
        .agg(
            spark_round(
                sum("total_order_item_value"),
                2
            ).alias("revenue")
        )
        .orderBy(desc("revenue"))
    )
    revenue["revenue_by_category"] = {
        row["product_category_name_english"]: float(row["revenue"])
        for row in category_revenue.collect()
    }
    print("Revenue KPIs generated successfully.")
    return revenue
def customer_kpis(df):
    customers = {}
    # KPI 1 : Total Customers
    total_customers = (
        df.agg(
            countDistinct("customer_unique_id")
            .alias("total_customers")
        )
        .first()["total_customers"]
    )
    customers["total_customers"] = int(total_customers)
    # KPI 2 : Repeat Customers
    repeat_customers = (
        df.groupBy("customer_unique_id")
        .agg(
            countDistinct("order_id")
            .alias("order_count")
        )
        .filter(col("order_count") > 1)
        .count()
    )
    customers["repeat_customers"] = int(repeat_customers)
    # KPI 3 : Customers by State
    customers_state = (
        df.groupBy("customer_state")
        .agg(
            countDistinct("customer_unique_id")
            .alias("customer_count")
        )
        .orderBy(desc("customer_count"))
    )
    customers["customers_by_state"] = {
        row["customer_state"]: int(row["customer_count"])
        for row in customers_state.collect()
    }
    # KPI 4 : Average Orders per Customer
    orders_per_customer = (
        df.groupBy("customer_unique_id")
        .agg(
            countDistinct("order_id")
            .alias("order_count")
        )
    )
    avg_orders = (
        orders_per_customer
        .agg(
            avg("order_count")
            .alias("average_orders")
        )
        .first()["average_orders"]
    )
    customers["average_orders_per_customer"] = round(
    float(avg_orders),
    2
)
    print("Customer KPIs generated successfully.")
    return customers
def order_kpis(df):
    orders = {}
    # KPI 1 : Total Orders
    total_orders = (
        df.agg(
            countDistinct("order_id")
            .alias("total_orders")
        )
        .first()["total_orders"]
    )
    orders["total_orders"] = int(total_orders)
    # KPI 2 : Order Status Distribution
    status_distribution = (
        df.groupBy("order_status")
        .agg(
            countDistinct("order_id")
            .alias("order_count")
        )
        .orderBy(desc("order_count"))
    )
    orders["order_status_distribution"] = {
        row["order_status"]: int(row["order_count"])
        for row in status_distribution.collect()
    }
    # KPI 3 : Average Delivery Time (Days)
    avg_delivery_time = (
        df.filter(
            col("delivery_time_days").isNotNull()
        )
        .agg(
            avg("delivery_time_days")
            .alias("avg_delivery_time")
        )
        .first()["avg_delivery_time"]
    )
    orders["average_delivery_time_days"] = round(
    float(avg_delivery_time),
    2
)
    # KPI 4 : Delayed Orders
    delayed_orders = (
        df.filter(
            col("delivery_delay_days") > 0
        )
        .agg(
            countDistinct("order_id")
            .alias("delayed_orders")
        )
        .first()["delayed_orders"]
    )
    orders["delayed_orders"] = int(delayed_orders)
    # KPI 5 : Delayed Order Percentage
    if total_orders:
        delayed_percentage = (delayed_orders / total_orders) * 100
    else:
        delayed_percentage = 0
    orders["delayed_order_percentage"] = round(
    delayed_percentage,
    2
)
    print("Order KPIs generated successfully.")
    return orders
def product_kpis(df):
    products = {}

    # KPI 1 : Top Selling Categories
    top_categories = (
        df.groupBy("product_category_name_english")
        .agg(
            count("order_item_id").alias("items_sold")
        )
        .orderBy(desc("items_sold"))
        .limit(10)
    )

    products["top_selling_categories"] = {
        row["product_category_name_english"]: int(row["items_sold"])
        for row in top_categories.collect()
    }

    # KPI 2 : Revenue by Category
    category_revenue = (
        df.groupBy("product_category_name_english")
        .agg(
            spark_round(
                sum("total_order_item_value"),
                2
            ).alias("revenue")
        )
        .orderBy(desc("revenue"))
        .limit(10)
    )

    products["revenue_by_category"] = {
        row["product_category_name_english"]: float(row["revenue"])
        for row in category_revenue.collect()
    }

    # KPI 3 : Average Product Price
    avg_price = (
        df.agg(
            avg("price").alias("avg_price")
        )
        .first()["avg_price"]
    )

    products["average_product_price"] = round(float(avg_price), 2)

    print("Product KPIs generated successfully.")

    return products
def payment_kpis(df):
    payments = {}

    # KPI 1 : Payment Method Distribution
    payment_methods = (
        df.groupBy("payment_type")
        .agg(
            countDistinct("order_id").alias("orders")
        )
        .orderBy(desc("orders"))
    )

    payments["payment_method_distribution"] = {
        row["payment_type"]: int(row["orders"])
        for row in payment_methods.collect()
    }

    # KPI 2 : Average Payment Value
    avg_payment = (
        df.agg(
            avg("payment_value").alias("avg_payment")
        )
        .first()["avg_payment"]
    )

    payments["average_payment_value"] = round(float(avg_payment), 2)

    # KPI 3 : Average Installments
    avg_installments = (
        df.agg(
            avg("payment_installments").alias("avg_installments")
        )
        .first()["avg_installments"]
    )

    payments["average_installments"] = round(float(avg_installments), 2)

    print("Payment KPIs generated successfully.")

    return payments
def review_kpis(df):
    reviews = {}

    # KPI 1 : Average Review Rating
    avg_rating = (
        df.agg(
            avg("review_score").alias("avg_rating")
        )
        .first()["avg_rating"]
    )

    reviews["average_review_rating"] = round(float(avg_rating), 2)

    # KPI 2 : Rating Distribution
    rating_distribution = (
    df.filter(
        col("review_score").isNotNull()
    )
    .groupBy("review_score")
    .agg(
        count("review_id").alias("count")
    )
    .orderBy("review_score"))
    reviews["rating_distribution"] = {
    int(row["review_score"]): int(row["count"])
    for row in rating_distribution.collect()}
    # KPI 3 : Best Rated Categories
    best_categories = (
        df.groupBy("product_category_name_english")
        .agg(
            spark_round(
                avg("review_score"),
                2
            ).alias("rating")
        )
        .orderBy(desc("rating"))
        .limit(10)
    )

    reviews["best_rated_categories"] = {
        row["product_category_name_english"]: float(row["rating"])
        for row in best_categories.collect()
    }

    # KPI 4 : Worst Rated Categories
    worst_categories = (
        df.groupBy("product_category_name_english")
        .agg(
            spark_round(
                avg("review_score"),
                2
            ).alias("rating")
        )
        .orderBy("rating")
        .limit(10)
    )

    reviews["worst_rated_categories"] = {
        row["product_category_name_english"]: float(row["rating"])
        for row in worst_categories.collect()
    }

    print("Review KPIs generated successfully.")

    return reviews
def geography_kpis(df):
    geography = {}

    # KPI 1 : Revenue by State
    revenue_state = (
        df.groupBy("customer_state")
        .agg(
            spark_round(
                sum("total_order_item_value"),
                2
            ).alias("revenue")
        )
        .orderBy(desc("revenue"))
        .limit(10)
    )

    geography["revenue_by_state"] = {
        row["customer_state"]: float(row["revenue"])
        for row in revenue_state.collect()
    }

    # KPI 2 : Orders by State
    orders_state = (
        df.groupBy("customer_state")
        .agg(
            countDistinct("order_id").alias("orders")
        )
        .orderBy(desc("orders"))
        .limit(10)
    )

    geography["orders_by_state"] = {
        row["customer_state"]: int(row["orders"])
        for row in orders_state.collect()
    }

    # KPI 3 : Customers by State
    customers_state = (
        df.groupBy("customer_state")
        .agg(
            countDistinct("customer_unique_id").alias("customers")
        )
        .orderBy(desc("customers"))
        .limit(10)
    )

    geography["customers_by_state"] = {
        row["customer_state"]: int(row["customers"])
        for row in customers_state.collect()
    }

    print("Geography KPIs generated successfully.")

    return geography
def seller_kpis(df):
    sellers = {}

    top_sellers = (
        df.groupBy(
            "seller_id",
            "seller_state"
        )
        .agg(
            spark_round(
                sum("total_order_item_value"),
                2
            ).alias("revenue")
        )
        .orderBy(desc("revenue"))
        .limit(10)
    )

    sellers["top_sellers_by_revenue"] = [
        {
            "seller_id": row["seller_id"],
            "seller_state": row["seller_state"],
            "revenue": float(row["revenue"])
        }
        for row in top_sellers.collect()
    ]

    print("Seller KPIs generated successfully.")

    return sellers
def generate_business_summary(df):

    summary = {
        "revenue": revenue_kpis(df),
        "customers": customer_kpis(df),
        "orders": order_kpis(df),
        "products": product_kpis(df),
        "payments": payment_kpis(df),
        "reviews": review_kpis(df),
        "geography": geography_kpis(df),
        "sellers": seller_kpis(df)
    }

    print("Business Summary Generated Successfully.")

    return summary
def save_summary(summary):

    PROCESSED_DATA.mkdir(parents=True, exist_ok=True)

    output_path = PROCESSED_DATA / "business_summary.json"

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(
            summary,
            file,
            indent=4,
            ensure_ascii=False
        )

    print("Business summary saved successfully.")
    print(f"Location : {output_path}")
def main():

    print("=" * 60)
    print("Spark KPI Pipeline Started")
    print("=" * 60)

    # Merge all datasets
    df = merge_datasets()

    print("Datasets merged successfully.")

    # Data cleaning / transformations
    df = transform_data(df)

    print("Transformations completed.")

    # Feature engineering
    df = create_features(df)

    print("Feature engineering completed.")

    # Generate KPIs
    summary = generate_business_summary(df)

    # Save JSON
    save_summary(summary)

    print("\nBusiness KPIs generated successfully!")
if __name__ == "__main__":
    main()