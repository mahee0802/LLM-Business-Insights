import os

from src.llm.llm_client import create_client

DEFAULT_MODEL = "gemini-3.8-flash"


def generate_business_report(prompt: str) -> str:
    """
    Sends a prompt to Gemini and returns the generated response.
    The model can be overridden with the GEMINI_MODEL environment variable.
    """

    client = create_client()
    model = os.getenv("GEMINI_MODEL", DEFAULT_MODEL)

    response = client.models.generate_content(
        model=model,
        contents=prompt
    )

    return response.text