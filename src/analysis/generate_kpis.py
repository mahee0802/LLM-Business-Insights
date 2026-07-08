import json
import pandas as pd
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parents[2]
PROCESSED_DATA = BASE_DIR / "data" / "processed"
def load_business_data():
    df = pd.read_csv(PROCESSED_DATA / "business_master.csv")
    print("Dataset loaded successfully.")
    print("Shape:", df.shape)
    return df

def revenue_kpis(df):
    revenue = {}
    #KPI 1: Total Revenue
    revenue["total_revenue"] = round(
        df["total_order_item_value"].sum(),
        2
    )
    # KPI 2: Average Order Value
    order_totals = (
        df.groupby("order_id")["total_order_item_value"]
        .sum()
    )
    revenue["average_order_value"] = round(
        order_totals.mean(),
        2
    )
    # KPI 3: Monthly Revenue Trend
    monthly_revenue = (
        df.groupby("purchase_year_month")["total_order_item_value"]
        .sum()
        .sort_index()
        .round(2)
    )
    revenue["monthly_revenue"] = monthly_revenue.to_dict()
    # KPI 4: Revenue by Product Category
    category_revenue = (
        df.groupby("product_category_name_english")["total_order_item_value"]
        .sum()
        .sort_values(ascending=False)
        .round(2)
    )
    revenue["revenue_by_category"] = category_revenue.to_dict()
    print("Revenue KPIs generated successfully.")
    return revenue

def customer_kpis(df):
    customers = {}
    # KPI 1: Total Customers
    customers["total_customers"] = int(df["customer_unique_id"].nunique())
    # KPI 2: Repeat Customers
    repeat = (df.groupby("customer_unique_id")["order_id"].nunique())
    customers["repeat_customers"] = int((repeat > 1).sum())
    # KPI 3: Customers by State
    state = (df.groupby("customer_state")["customer_unique_id"].nunique().sort_values(ascending=False))
    customers["customers_by_state"] = (state.to_dict())
    # KPI 4: Average Orders per Customer
    avg_orders = (df.groupby("customer_unique_id")["order_id"].nunique().mean())
    customers["average_orders_per_customer"] = round(avg_orders, 2)
    return customers

def order_kpis(df):
    orders = {}
    # KPI 1: Total Orders
    orders["total_orders"] = int(df["order_id"].nunique())
    # KPI 2: Order Status Distribution
    status_distribution = (df.groupby("order_status")["order_id"].nunique().sort_values(ascending=False))
    orders["order_status_distribution"] = (status_distribution.to_dict())
    # KPI 3: Average Delivery Time (Days)
    avg_delivery_time = (df["delivery_time_days"].dropna().mean())
    orders["average_delivery_time_days"] = round(avg_delivery_time,2)
    # KPI 4: Delayed Orders
    delayed_orders = (df.loc[df["delivery_delay_days"] > 0, "order_id"].nunique())
    orders["delayed_orders"] = int(delayed_orders)
    orders["delayed_order_percentage"] = round((delayed_orders / orders["total_orders"]) * 100,2)
    print("Order KPIs generated successfully.")
    return orders

def product_kpis(df):
    products = {}
    # KPI 1: Top Selling Categories
    top_categories = (df.groupby("product_category_name_english")["order_item_id"].count().sort_values(ascending=False)).head(10)
    products["top_selling_categories"] = top_categories.to_dict()
    # KPI 2: Revenue by Category
    category_revenue = (
        df.groupby("product_category_name_english")["total_order_item_value"]
        .sum()
        .sort_values(ascending=False).head(10).round(2))
    products["revenue_by_category"] = category_revenue.to_dict()
    # KPI 3: Average Product Price
    avg_price = df["price"].mean()
    products["average_product_price"] = round(avg_price,2)
    print("Product KPIs generated successfully.")
    return products

def payment_kpis(df):
    payments = {}
    # KPI 1: Payment Method Distribution
    payment_methods = (df.groupby("payment_type")["order_id"].nunique().sort_values(ascending=False))
    payments["payment_method_distribution"] = (payment_methods.to_dict())
    # KPI 2: Average Payment Value
    avg_payment = df["payment_value"].mean()
    payments["average_payment_value"] = round(avg_payment,2)
    # KPI 3: Average Installments
    avg_installments = df["payment_installments"].mean()
    payments["average_installments"] = round(avg_installments,2)
    print("Payment KPIs generated successfully.")
    return payments

def review_kpis(df):
    reviews = {}
    # KPI 1: Average Review Rating
    avg_rating = df["review_score"].mean()
    reviews["average_review_rating"] = round(avg_rating,2)
    # KPI 2: Rating Distribution
    rating_distribution = (df.groupby("review_score")["review_id"].count().sort_index())
    reviews["rating_distribution"] = (rating_distribution.to_dict())
    # KPI 3: Best Rated Categories (Top 10)
    best_categories = (
        df.groupby("product_category_name_english")["review_score"]
        .mean()
        .dropna()
        .sort_values(ascending=False)
        .head(10)
        .round(2)
    )
    reviews["best_rated_categories"] = (best_categories.to_dict())
    # KPI 4: Worst Rated Categories (Top 10)
    worst_categories = (
        df.groupby("product_category_name_english")["review_score"]
        .mean()
        .dropna()
        .sort_values(ascending=True)
        .head(10)
        .round(2)
    )
    reviews["worst_rated_categories"] = (worst_categories.to_dict())
    print("Review KPIs generated successfully.")
    return reviews

def geography_kpis(df):
    geography = {}
    # KPI 1: Revenue by State
    revenue_by_state = (
        df.groupby("customer_state")["total_order_item_value"]
        .sum()
        .sort_values(ascending=False).head(10)
        .round(2)
    )
    geography["revenue_by_state"] = (revenue_by_state.to_dict())
    # KPI 2: Orders by State
    orders_by_state = (
        df.groupby("customer_state")["order_id"]
        .nunique()
        .sort_values(ascending=False).head(10)
    )
    geography["orders_by_state"] = (orders_by_state.to_dict())
    # KPI 3: Customers by State
    customers_by_state = (df.groupby("customer_state")["customer_unique_id"].nunique().sort_values(ascending=False).head(10))
    geography["customers_by_state"] = (customers_by_state.to_dict())
    print("Geography KPIs generated successfully.")
    return geography

def seller_kpis(df):
    sellers = {}
    # KPI 1: Top Sellers by Revenue
    top_sellers = (
    df.groupby(["seller_id", "seller_state"])["total_order_item_value"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)
    sellers["top_sellers_by_revenue"] = top_sellers.to_dict(orient="records")
    print("Seller KPIs generated successfully.")
    return sellers
    
# Generate Complete Business Summary
def generate_business_summary(df):
    summary = {
        "revenue": revenue_kpis(df),
        "customers": customer_kpis(df),
        "orders": order_kpis(df),
        "products": product_kpis(df),
        "payments": payment_kpis(df),
        "reviews": review_kpis(df),
        "geography": geography_kpis(df),
        "sellers": seller_kpis(df)
    }
    print("Business Summary Generated Successfully.")
    return summary

# Save Business Summary
def save_summary(summary):
    PROCESSED_DATA.mkdir(parents=True, exist_ok=True)
    output_path = PROCESSED_DATA / "business_summary.json"
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(
            summary,
            file,
            indent=4,
            ensure_ascii=False
        )
    print("Business summary saved successfully.")
    print(f"Location: {output_path}")

def main():
    df = load_business_data()
    summary = generate_business_summary(df)
    save_summary(summary)
    print("\nBusiness KPIs generated successfully!")
if __name__ == "__main__":
    main()