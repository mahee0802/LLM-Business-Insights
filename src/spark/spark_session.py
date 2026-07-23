from pyspark.sql import SparkSession
def create_spark_session():
    spark = (
        SparkSession.builder
        .appName("LLM Business Insights")
        .master("local[*]")
        .getOrCreate()
    )
    return spark