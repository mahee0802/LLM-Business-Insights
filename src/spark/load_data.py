from pathlib import Path
from src.spark.spark_session import create_spark_session
spark = create_spark_session()
BASE_DIR = Path(__file__).resolve().parents[2]
RAW_DATA = BASE_DIR / "data" / "raw" / "olist_dataset"
def load_orders():
    orders = spark.read.csv(
        str(RAW_DATA / "olist_orders_dataset.csv"),
        header=True,
        inferSchema=True
    )
    return orders
def load_customers():
    customers = spark.read.csv(
        str(RAW_DATA / "olist_customers_dataset.csv"),
        header=True,
        inferSchema=True
    )
    return customers
def load_order_items():
    order_items = spark.read.csv(
        str(RAW_DATA / "olist_order_items_dataset.csv"),
        header=True,
        inferSchema=True
    )
    return order_items
def load_products():
    products = spark.read.csv(
        str(RAW_DATA / "olist_products_dataset.csv"),
        header=True,
        inferSchema=True
    )
    return products
def load_payments():
    payments = spark.read.csv(
        str(RAW_DATA / "olist_order_payments_dataset.csv"),
        header=True,
        inferSchema=True
    )
    return payments
def load_reviews():
    reviews = (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .option("multiLine", True)
        .option("quote", '"')
        .option("escape", '"')
        .csv(str(RAW_DATA / "olist_order_reviews_dataset.csv"))
    )
    return reviews
def load_sellers():
    sellers = spark.read.csv(
        str(RAW_DATA / "olist_sellers_dataset.csv"),
        header=True,
        inferSchema=True
    )
    return sellers
def load_geolocation():
    geolocation = spark.read.csv(
        str(RAW_DATA / "olist_geolocation_dataset.csv"),
        header=True,
        inferSchema=True
    )
    return geolocation
def load_translation():
    translation = spark.read.csv(
        str(RAW_DATA / "product_category_name_translation.csv"),
        header=True,
        inferSchema=True
    )
    return translation
def load_all_datasets():
    return 
    {
        "orders": load_orders(),
        "customers": load_customers(),
        "order_items": load_order_items(),
        "products": load_products(),
        "payments": load_payments(),
        "reviews": load_reviews(),
        "sellers": load_sellers(),
        "geolocation": load_geolocation(),
        "translation": load_translation()
    }