def save_report(report, output_path="outputs/business_insights.md"):
    """
    Save the generated report.
    """

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(report)

    print(f"Report saved successfully to {output_path}")