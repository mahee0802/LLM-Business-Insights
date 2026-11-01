import os
import time

from google.genai import errors

from src.llm.llm_client import create_client

DEFAULT_MODEL = "gemini-3.8-flash"
MAX_RETRIES = 4
SERVER_ERRORS = {500, 502, 503, 504}


def _should_retry(e: errors.APIError) -> bool:
    """Retry temporary server errors and per-minute limits, but not an exhausted daily quota."""
    if e.code == 429:
        return "per day" not in str(e).lower()
    return e.code in SERVER_ERRORS


def generate_business_report(prompt: str) -> str:
    """
    Sends a prompt to Gemini and returns the generated response.
    Retries with exponential backoff on temporary errors.
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
            if not _should_retry(e) or attempt == MAX_RETRIES:
                raise
            wait = 2 ** attempt * 5  # 10s, 20s, 40s
            print(f"Gemini busy ({e.code}). Retry {attempt}/{MAX_RETRIES - 1} in {wait}s...")
            time.sleep(wait)