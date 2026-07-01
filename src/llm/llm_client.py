import os

from dotenv import load_dotenv
from google import genai


def create_client():
    """
    Create and return a Gemini client.
    """

    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    return client