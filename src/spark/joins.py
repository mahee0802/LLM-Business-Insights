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
def merge_datasets():
    orders = load_orders()
    customers = load_customers()
    order_items = load_order_items()
    products = load_products()
    payments = load_payments()
    reviews = load_reviews()
    sellers = load_sellers()
    translation = load_translation()
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