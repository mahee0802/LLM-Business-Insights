import streamlit as st
import pandas as pd
from datetime import datetime
from src.data.load_data import load_business_summary
from src.llm.prompts import (
    build_business_report_prompt,
    build_revenue_prompt,
    build_customer_prompt,
    build_product_prompt,
    build_custom_prompt,
)
from src.llm.generate_insights import generate_business_report
from src.utils.save_report import save_report
business_summary = load_business_summary()
total_revenue = business_summary["revenue"]["total_revenue"]
total_customers = business_summary["customers"]["total_customers"]
total_orders = business_summary["orders"]["total_orders"]
average_review = business_summary["reviews"]["average_review_rating"]
monthly_revenue = business_summary["revenue"]["monthly_revenue"]
monthly_revenue_df = pd.DataFrame(
    monthly_revenue.items(),
    columns=["Month", "Revenue"]
)
monthly_revenue_df["Month"] = pd.to_datetime(
    monthly_revenue_df["Month"]
)

monthly_revenue_df = monthly_revenue_df.sort_values("Month")
# Page Configuration
st.set_page_config(
    page_title="Business AI Analyst",
    page_icon="📊",
    layout="wide"
)
# Main Page
st.title("📊 AI Business Analyst")

st.caption("Generate professional business intelligence reports using Large Language Models.")
st.write(
    """
    Welcome to the AI-powered Business Insights Generator.

    Generate professional business reports and ask custom business questions.
    """
)
st.subheader("📈 Business Snapshot")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("💰 Total Revenue",f"R$ {total_revenue:,.2f}")
with col2:
    st.metric("📦 Total Orders",f"{total_orders:,}")
with col3:
    st.metric("👥 Total Customers",f"{total_customers:,}")
with col4:
    st.metric("⭐ Avg Review",f"{average_review:.2f}")
st.subheader("📈 Monthly Revenue Trend")
st.line_chart(monthly_revenue_df.set_index("Month"))
# Sidebar
st.sidebar.header("Business AI Analyst")
st.sidebar.write(
    """
    Generate AI-powered business insights from the processed business summary.
    """
)
st.sidebar.divider()
st.sidebar.subheader("Choose Analysis")
analysis = st.sidebar.selectbox(
    "Select an analysis type:",
    (
        "Full Business Report",
        "Revenue Analysis",
        "Customer Analysis",
        "Product Analysis",
        "Custom Business Question"
    )
)
st.write(f"Selected Analysis: **{analysis}**")
# Custom Business Question
user_question = ""
if analysis == "Custom Business Question":
    user_question = st.text_area(
    "Enter your business question:",
    placeholder="Example: Which state generates the highest revenue and why?"
)
if user_question:
    st.write("Your Question:")
    st.write(user_question)
generate = st.sidebar.button(
    "Generate Report",
    use_container_width=True
)
if generate:

    if analysis == "Full Business Report":

        prompt = build_business_report_prompt(
            business_summary
        )

        filename = "business_report.md"

    elif analysis == "Revenue Analysis":

        prompt = build_revenue_prompt(
            business_summary
        )

        filename = "revenue_report.md"

    elif analysis == "Customer Analysis":

        prompt = build_customer_prompt(
            business_summary
        )

        filename = "customer_report.md"

    elif analysis == "Product Analysis":

        prompt = build_product_prompt(
            business_summary
        )

        filename = "product_report.md"

    elif analysis == "Custom Business Question":

        if not user_question.strip():

            st.warning("Please enter a business question.")

            st.stop()

        prompt = build_custom_prompt(
            business_summary,
            user_question
        )

        filename = "custom_question.md"

    try:
        with st.spinner("Generating business insights..."):
            report = generate_business_report(prompt)
        current_datetime = datetime.now().strftime("%d %B %Y | %I:%M %p")
        metadata = f"""# Business Analysis Report
        **Generated On:** {current_datetime}
        **Analysis Type:** {analysis}---"""
        report = metadata + report
        save_report(report, filename)
        st.success("Report generated successfully!")
        # with st.expander("📄 View Generated Report", expanded=True):
        #     st.markdown(report)
        # st.download_button(label="📥 Download Report",data=report,file_name=filename,mime="text/markdown",
        # use_container_width=True
        tab1, tab2, tab3 = st.tabs(["📄 Report","ℹ️ Metadata","📥 Download"])
        with tab1:
            st.subheader("Generated Business Report")
            st.markdown(report)
        with tab2:
            st.subheader("Report Information")
            st.write("**📅 Generated On:**", current_datetime)
            st.write("**📊 Analysis Type:**", analysis)
        with tab3:
            st.subheader("Download Report")
            st.write("Download the generated report in Markdown format.")
            st.download_button(label="📥 Download Report",data=report,file_name=filename,mime="text/markdown",
        use_container_width=True)
    except Exception as e:
        st.error(f"Error generating report:\n\n{e}")

