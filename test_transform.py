from src.spark.joins import merge_datasets
from src.spark.transform import transform_data

business_df = merge_datasets()

business_df = transform_data(business_df)

business_df.printSchema()

business_df.show(5, truncate=False)