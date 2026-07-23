from pyspark.sql.functions import col, try_to_timestamp
from pyspark.sql.types import IntegerType
def transform_data(df):
    date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date",
    "review_creation_date",
    "review_answer_timestamp"]
    print(df.columns)
    for column in date_columns:
        df = df.withColumn(column,try_to_timestamp(col(column)))
    before = df.count()
    df = df.dropDuplicates()
    after = df.count()
    duplicates_removed = before - after
    print(f"Removed {duplicates_removed} duplicate rows.")
    df = df.fillna(
    {
        "product_category_name": "Unknown"
    })
    df = df.fillna(
    {
    "product_category_name_english": "Unknown"
    })
    df = df.withColumn(
    "review_score",
    col("review_score").cast(IntegerType()))
    return df



