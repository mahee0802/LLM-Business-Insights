import json
def build_prompt(business_summary):
    """
    Build the prompt for Gemini.
    """

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

    return prompt