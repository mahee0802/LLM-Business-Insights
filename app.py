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
def display_menu():
    """
    Display the analysis menu.
    """

    print("\n" + "=" * 50)
    print("        BUSINESS INSIGHTS GENERATOR")
    print("=" * 50)
    print("1. Generate Full Business Report")
    print("2. Revenue Analysis")
    print("3. Customer Analysis")
    print("4. Product Analysis")
    print("5. Ask a Custom Business Question")
    print("0. Exit")
    print("=" * 50)

def get_prompt(choice, business_summary):
    """
    Returns the appropriate prompt and output filename.
    """

    if choice == "1":
        return (
            build_business_report_prompt(business_summary),
            "business_report.md"
        )

    elif choice == "2":
        return (
            build_revenue_prompt(business_summary),
            "revenue_report.md"
        )

    elif choice == "3":
        return (
            build_customer_prompt(business_summary),
            "customer_report.md"
        )

    elif choice == "4":
        return (
            build_product_prompt(business_summary),
            "product_report.md"
        )

    elif choice == "5":
        question = input("\nEnter your business question:\n\n").strip()

        if not question:
            print("\nQuestion cannot be empty.\n")
            return None, None

        return (
            build_custom_prompt(business_summary, question),
            "custom_question.md"
        )

    else:
        return None, None

def main():

    business_summary = load_business_summary()

    while True:

        display_menu()

        choice = input("\nChoose an option: ").strip()

        if choice == "0":
            print("\nExiting Business Insights Generator...")
            break

        prompt, filename = get_prompt(choice, business_summary)

        if prompt is None:
            print("\nInvalid choice. Please try again.\n")
            continue

        print("\nGenerating insights...\n")

        report = generate_business_report(prompt)

        print(report)

        save_report(report, filename)

        print("\nReport generated successfully!\n")

if __name__ == "__main__":
    main()