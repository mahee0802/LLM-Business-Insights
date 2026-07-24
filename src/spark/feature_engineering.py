from pyspark.sql.functions import (col,year,month,quarter,dayofmonth,date_format,datediff,round as spark_round,when,lit)
from pyspark.sql.functions import coalesce, lit
def create_features(df):
    df = df.withColumn("purchase_year",year(col("order_purchase_timestamp")))
    df = df.withColumn("purchase_month",month(col("order_purchase_timestamp")))
    df = df.withColumn("purchase_month_name",date_format(col("order_purchase_timestamp"),"MMMM"))
    df = df.withColumn(
    "purchase_year_month",date_format(col("order_purchase_timestamp"),"yyyy-MM"))
    df = df.withColumn("purchase_quarter",quarter(col("order_purchase_timestamp")))
    df = df.withColumn("purchase_day",dayofmonth(col("order_purchase_timestamp")))
    df = df.withColumn("purchase_weekday",date_format(col("order_purchase_timestamp"),"EEEE"))
    df = df.withColumn(
    "delivery_time_days",
    datediff(
        col("order_delivered_customer_date"),
        col("order_purchase_timestamp")
    )
)
    df = df.withColumn(
    "delivery_delay_days",
    datediff(
        col("order_delivered_customer_date"),
        col("order_estimated_delivery_date")
    )
)
    df = df.withColumn(
    "total_order_item_value",
    spark_round(
        coalesce(col("price"), lit(0)) +
        coalesce(col("freight_value"), lit(0)),
        2
    )
)
    df = df.withColumn(
    "review_category",
    when(
        col("review_score").isNull(),
        "No Review"
    )
    .when(
        col("review_score") == 5,
        "Excellent"
    )
    .when(
        col("review_score") == 4,
        "Good"
    )
    .when(
        col("review_score") == 3,
        "Average"
    )
    .when(
        col("review_score").isin([1,2]),
        "Poor"
    )
    .otherwise("Unknown")
)
    return df