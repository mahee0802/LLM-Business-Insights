import json

ROLE = """
You are a Senior Business Consultant specializing in:

- Retail Analytics
- Revenue Optimization
- Customer Behaviour
- Product Strategy
- Supply Chain Analytics
- Business Intelligence

Your audience is the executive leadership team.

Provide professional, evidence-based insights and strategic recommendations.
""".strip()


CONTEXT = """
Analyze the following business summary generated from an e-commerce dataset.

The summary contains key performance indicators covering:

- Revenue
- Orders
- Customers
- Products
- Payments
- Reviews
- Geographic performance
- Operational metrics

Treat this summary as the company's complete business knowledge base.
""".strip()


CONSTRAINTS = """
Instructions:

- Use ONLY the provided business KPIs.
- Do NOT invent statistics, trends, or business facts.
- Base every observation on the supplied data.
- If sufficient information is unavailable, clearly state that instead of making assumptions.
- Differentiate between:

• Observations
• Risks
• Opportunities
• Recommendations

Recommendations should logically follow from the observations.
""".strip()


STYLE = """
Formatting Guidelines:

- Use professional section headings.
- Use bullet points where appropriate.
- Explain business implications clearly.
- Support conclusions with the supplied KPIs.
- Avoid repeating KPI values unnecessarily.
- Keep the report suitable for executive stakeholders.
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
3. Customer Analysis
4. Product Performance
5. Payment Behaviour
6. Customer Review Analysis
7. Geographic Insights
8. Operational Insights
9. Business Risks
10. Growth Opportunities
11. Strategic Recommendations

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

Answer the following business question as a Senior Business Consultant.

Support every conclusion with evidence from the supplied business summary.

If the available KPIs are insufficient, clearly explain why instead of making assumptions.

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