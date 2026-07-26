from src.spark.joins import merge_datasets

business_df = merge_datasets()

business_df.show(5)

business_df.printSchema()
print("Total Rows:", business_df.count())