import json

ROLE = """
You are a Senior Business Analyst working for a global e-commerce consulting firm.
""".strip()


CONTEXT = """
Analyze the following business KPIs extracted from an online retail dataset.
""".strip()


CONSTRAINTS = """
Instructions:

- Use ONLY the provided business KPIs.
- Do NOT invent statistics, trends, or business facts.
- Base every observation on the supplied data.
- If sufficient information is unavailable, clearly state that instead of making assumptions.
""".strip()


STYLE = """
Formatting Guidelines:

- Use clear headings and subheadings.
- Use bullet points where appropriate.
- Keep the report concise, professional, and data-driven.
- Write for senior management and business stakeholders.
""".strip()

def build_base_prompt(business_summary):
    """
    Builds the common prompt shared by all analyses.
    """

    return f"""
{ROLE}

{CONTEXT}

Business KPIs:

{json.dumps(business_summary, indent=4)}

{CONSTRAINTS}

{STYLE}
""".strip()

def build_business_report_prompt(business_summary):
    """
    Generates a comprehensive business performance report.
    """

    prompt = build_base_prompt(business_summary)

    prompt += """

Task:

Generate a comprehensive business performance report.

Report Structure:

1. Executive Summary
2. Revenue Analysis
3. Customer Behavior Insights
4. Product Performance
5. Potential Business Risks
6. Growth Opportunities
7. Three Actionable Recommendations

Ensure every recommendation is supported by the provided KPIs.
"""

    return prompt

def build_revenue_prompt(business_summary):
    """
    Generates a revenue-focused report.
    """

    prompt = build_base_prompt(business_summary)

    prompt += """

Task:

Analyze ONLY the company's revenue performance.

Report Structure:

1. Revenue Overview
2. Revenue Trends
3. Key Revenue Drivers
4. Revenue Risks
5. Revenue Growth Recommendations

Do not include customer or product analysis unless it directly impacts revenue.
"""

    return prompt

def build_customer_prompt(business_summary):
    """
    Generates customer insights.
    """

    prompt = build_base_prompt(business_summary)

    prompt += """

Task:

Analyze customer behaviour using the available KPIs.

Report Structure:

1. Customer Overview
2. Purchasing Behaviour
3. Customer Retention Insights
4. Customer Risks
5. Customer Growth Opportunities
6. Customer Recommendations

Focus only on customer-related insights.
"""

    return prompt

def build_product_prompt(business_summary):
    """
    Generates product performance insights.
    """

    prompt = build_base_prompt(business_summary)

    prompt += """

Task:

Analyze product performance using the available KPIs.

Report Structure:

1. Product Performance Overview
2. Best Performing Products or Categories
3. Weak Performing Products or Categories
4. Product Risks
5. Product Growth Opportunities
6. Product Strategy Recommendations

Focus only on product-related insights.
"""

    return prompt

def build_custom_prompt(business_summary, user_question):
    """
    Answers a user-defined business question.
    """

    prompt = build_base_prompt(business_summary)

    prompt += f"""

Task:

Answer the following business question using ONLY the supplied business KPIs.

Business Question:

{user_question}

Response Structure:

1. Answer
2. Supporting Evidence
3. Business Implications
4. Recommendation

If the available KPIs are insufficient to answer the question confidently,
clearly mention the limitation instead of making assumptions.
"""

    return prompt