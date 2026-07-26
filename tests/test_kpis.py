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

from src.spark.joins import merge_datasets
from src.spark.transform import transform_data
from src.spark.feature_engineering import create_features

from src.spark.kpis import (
    revenue_kpis,
    customer_kpis,
    order_kpis
)


def main():

    print("=" * 60)
    print("Loading datasets...")
    print("=" * 60)

    orders = load_orders()
    customers = load_customers()
    order_items = load_order_items()
    products = load_products()
    payments = load_payments()
    reviews = load_reviews()
    sellers = load_sellers()
    translation = load_translation()

    print("\nDatasets loaded successfully.\n")

    print("=" * 60)
    print("Merging datasets...")
    print("=" * 60)

    df = merge_datasets(
        orders,
        customers,
        order_items,
        products,
        payments,
        reviews,
        sellers,
        translation
    )

    print("\nMerged Dataset")
    print(f"Rows : {df.count()}")
    print(f"Columns : {len(df.columns)}")

    print("=" * 60)
    print("Applying Transformations...")
    print("=" * 60)

    df = transform_data(df)

    print("=" * 60)
    print("Applying Feature Engineering...")
    print("=" * 60)

    df = create_features(df)

    print("\nFinal Dataset")
    print(f"Rows : {df.count()}")
    print(f"Columns : {len(df.columns)}")

    # =====================================================
    # Revenue KPIs
    # =====================================================

    print("\n")
    print("=" * 60)
    print("REVENUE KPIs")
    print("=" * 60)

    revenue = revenue_kpis(df)

    for key, value in revenue.items():
        print(f"{key}:")
        print(value)
        print()

    # =====================================================
    # Customer KPIs
    # =====================================================

    print("\n")
    print("=" * 60)
    print("CUSTOMER KPIs")
    print("=" * 60)

    customer = customer_kpis(df)

    for key, value in customer.items():
        print(f"{key}:")
        print(value)
        print()

    # =====================================================
    # Order KPIs
    # =====================================================

    print("\n")
    print("=" * 60)
    print("ORDER KPIs")
    print("=" * 60)

    order = order_kpis(df)

    for key, value in order.items():
        print(f"{key}:")
        print(value)
        print()


if __name__ == "__main__":
    main()