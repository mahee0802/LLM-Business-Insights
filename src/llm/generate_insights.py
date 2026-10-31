import os
import time

from google.genai import errors

from src.llm.llm_client import create_client

DEFAULT_MODEL = "gemini-3.8-flash"
MAX_RETRIES = 5
RETRYABLE_CODES = {429, 500, 502, 503, 504}


def generate_business_report(prompt: str) -> str:
    """
    Sends a prompt to Gemini and returns the generated response.
    Retries with exponential backoff on temporary server errors.
    The model can be overridden with the GEMINI_MODEL environment variable.
    """

    client = create_client()
    model = os.getenv("GEMINI_MODEL", DEFAULT_MODEL)

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = client.models.generate_content(
                model=model,
                contents=prompt
            )
            return response.text
        except errors.APIError as e:
            if e.code not in RETRYABLE_CODES or attempt == MAX_RETRIES:
                raise
            wait = 2 ** attempt * 5  # 10s, 20s, 40s, 80s
            print(f"Gemini busy ({e.code}). Retry {attempt}/{MAX_RETRIES - 1} in {wait}s...")
            time.sleep(wait)