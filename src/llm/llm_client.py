import os

from dotenv import load_dotenv
from google import genai
from google.genai import types


def create_client():
    """
    Create and return a Gemini client with a request timeout.
    """

    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(
        api_key=api_key,
        http_options=types.HttpOptions(timeout=120_000),  # milliseconds
    )
    return client