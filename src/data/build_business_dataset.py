import pandas as pd
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parents[2]
RAW_DATA = BASE_DIR / "data" / "raw" / "olist_dataset"
PROCESSED_DATA = BASE_DIR / "data" / "processed"
def load_data():

    orders = pd.read_csv(RAW_DATA / "olist_orders_dataset.csv")

    customers = pd.read_csv(RAW_DATA / "olist_customers_dataset.csv")

    order_items = pd.read_csv(RAW_DATA / "olist_order_items_dataset.csv")

    products = pd.read_csv(RAW_DATA / "olist_products_dataset.csv")

    payments = pd.read_csv(RAW_DATA / "olist_order_payments_dataset.csv")

    reviews = pd.read_csv(RAW_DATA / "olist_order_reviews_dataset.csv")

    sellers = pd.read_csv(RAW_DATA / "olist_sellers_dataset.csv")

    translation = pd.read_csv(
        RAW_DATA / "product_category_name_translation.csv"
    )

    print("\nDatasets Loaded Successfully\n")

    print("Orders      :", orders.shape)
    print("Customers   :", customers.shape)
    print("Order Items :", order_items.shape)
    print("Products    :", products.shape)
    print("Payments    :", payments.shape)
    print("Reviews     :", reviews.shape)
    print("Sellers     :", sellers.shape)
    print("Translation :", translation.shape)

    return (
        orders,
        customers,
        order_items,
        products,
        payments,
        reviews,
        sellers,
        translation
    )
def merge_datasets(
    orders,
    customers,
    order_items,
    products,
    payments,
    reviews,
    sellers,
    translation
):
    """
    Merge all datasets into one master business dataset.
    """

    print("\nStarting dataset merges...\n")

    # Merge Orders + Customers
    business_df = orders.merge(
        customers,
        on="customer_id",
        how="left"
    )

    print("Merged Orders + Customers :", business_df.shape)

    # Merge Order Items
    business_df = business_df.merge(
        order_items,
        on="order_id",
        how="left"
    )

    print("Merged Order Items :", business_df.shape)

    # Merge Products
    business_df = business_df.merge(
        products,
        on="product_id",
        how="left"
    )

    print("Merged Products :", business_df.shape)

    # Merge Category Translation
    business_df = business_df.merge(
        translation,
        on="product_category_name",
        how="left"
    )

    print("Merged Translation :", business_df.shape)

    # Merge Payments
    business_df = business_df.merge(
        payments,
        on="order_id",
        how="left"
    )

    print("Merged Payments :", business_df.shape)

    # Merge Reviews
    business_df = business_df.merge(
        reviews,
        on="order_id",
        how="left"
    )

    print("Merged Reviews :", business_df.shape)

    # Merge Sellers
    business_df = business_df.merge(
        sellers,
        on="seller_id",
        how="left"
    )

    print("Merged Sellers :", business_df.shape)
    return business_df
def preprocess_data(df):
    """
    Clean the merged business dataset and create
    useful features for analytics.
    """

    print("\nPreprocessing business dataset...\n")

    # List of date columns
    date_columns = [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date",
        "review_creation_date",
        "review_answer_timestamp"
    ]

    # Convert each column to datetime
    for col in date_columns:
        if col in df.columns:
            df[col] = pd.to_datetime(
                df[col],
                errors="coerce"
            )

    print("Date columns converted successfully.")
    duplicate_count = df.duplicated().sum()

    print(f"Duplicate rows found: {duplicate_count}")

    if duplicate_count > 0:
        df = df.drop_duplicates()

        print(f"Removed {duplicate_count} duplicate rows.")
    else:
        print("No duplicate rows found.")

    df["purchase_year"] = df["order_purchase_timestamp"].dt.year
    df["purchase_month"] = df["order_purchase_timestamp"].dt.month
    df["purchase_month_name"] = df["order_purchase_timestamp"].dt.month_name()
    df["purchase_year_month"] = (
    df["order_purchase_timestamp"]
      .dt.to_period("M")
      .astype(str)
)
    df["purchase_quarter"] = df["order_purchase_timestamp"].dt.quarter
    df["purchase_day"] = df["order_purchase_timestamp"].dt.day
    df["purchase_weekday"] = df["order_purchase_timestamp"].dt.day_name()
    df["delivery_time_days"] = (df["order_delivered_customer_date"] -df["order_purchase_timestamp"]).dt.days
    df["delivery_delay_days"] = (
    (
        df["order_delivered_customer_date"]
        - df["order_estimated_delivery_date"]
    ).dt.total_seconds()
    / (24 * 60 * 60)
).round(2)
    df["total_order_item_value"] = (df["price"] + df["freight_value"]).round(2)
    def categorize_review(score):
     if pd.isna(score):
        return "No Review"
     elif score == 5:
        return "Excellent"
     elif score == 4:
        return "Good"
     elif score == 3:
        return "Average"
     elif score in [1, 2]:
        return "Poor"
     else:
        return "Unknown"
    df["review_category"] = df["review_score"].apply(categorize_review)
    df["product_category_name"] = (
    df["product_category_name"]
    .fillna("Unknown")
)
    df["product_category_name_english"] = (
    df["product_category_name_english"]
    .fillna("Unknown")
)
    df["review_category"] = (
    df["review_category"]
    .fillna("No Review")
)
# Note:
# Missing values for delivery, reviews, and order items are
# preserved because they represent meaningful business events
# (e.g., cancelled orders, undelivered orders, no customer review).
    print("Business dataset preprocessing completed successfully.")

    return df

def inspect_dataset(df):
    print(f"\nDataset Shape: {df.shape}")

    # Column Names
    print("\nColumns:")
    for column in df.columns:
        print(f"- {column}")

    # Data Types
    print("\nData Types:")
    print(df.dtypes)

    # Missing Values
    print("\nMissing Values:")
    missing_values = df.isnull().sum()
    print(missing_values[missing_values > 0])

    # Duplicate Rows
    print(f"\nDuplicate Rows: {df.duplicated().sum()}")

    # First Five Rows
    print("\nFirst Five Rows:")
    print(df.head())

def save_dataset(df):
    print("\nSaving business dataset...")
    PROCESSED_DATA.mkdir(parents=True, exist_ok=True)
    output_path = PROCESSED_DATA / "business_master.csv"
    df.to_csv(output_path, index=False)
    print(f"Business dataset saved successfully!")
    print(f"Location: {output_path}")

def main():
    (
        orders,
        customers,
        order_items,
        products,
        payments,
        reviews,
        sellers,
        translation,
    ) = load_data()

    business_df = merge_datasets(
    orders,
    customers,
    order_items,
    products,
    payments,
    reviews,
    sellers,
    translation,
)

    business_df = preprocess_data(business_df)
    inspect_dataset(business_df)
    save_dataset(business_df)
    print("\nBusiness Dataset Created Successfully!")
if __name__ == "__main__":  
    main()