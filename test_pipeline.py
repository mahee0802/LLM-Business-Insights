import os
import json
from dotenv import load_dotenv
from google import genai
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
with open(
    "outputs/business_summary.json",
    "r"
) as file:

    business_summary = json.load(file)

prompt = f"""
You are a Senior Business Analyst working for a global e-commerce consulting firm.

Analyze the following business KPIs extracted from an online retail dataset.

Business KPIs:
{json.dumps(business_summary, indent=4)}

Generate a professional report with the following sections:

1. Executive Summary
2. Revenue Analysis
3. Customer Behavior Insights
4. Product Performance
5. Potential Business Risks
6. Growth Opportunities
7. Three Actionable Recommendations

Use headings and bullet points where appropriate.
Keep the report concise, data-driven, and suitable for presentation to senior management.
"""
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)
business_report = response.text
print("\n")
print("=" * 70)
print("BUSINESS INSIGHTS REPORT")
print("=" * 70)
print("\n")
print(business_report)
output_path = "outputs/business_insights.md"
with open(output_path, "w", encoding="utf-8") as file:
    file.write(business_report)
print("\n")
print("=" * 70)
print(f"Report saved successfully to:\n{output_path}")
print("=" * 70)