from src.spark.joins import merge_datasets
from src.spark.transform import transform_data
from src.spark.feature_engineering import create_features

business_df = merge_datasets()

business_df = transform_data(business_df)

business_df = create_features(business_df)

business_df.printSchema()

business_df.select(
    "purchase_year",
    "purchase_month",
    "purchase_month_name",
    "purchase_year_month",
    "purchase_weekday",
    "delivery_time_days",
    "delivery_delay_days",
    "total_order_item_value",
    "review_category"
).show(10, truncate=False)