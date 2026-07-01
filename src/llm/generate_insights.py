from src.llm.llm_client import create_client


def generate_business_report(prompt):
    """
    Send prompt to Gemini and return the response.
    """

    client = create_client()

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text