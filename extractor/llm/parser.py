import json
import re
from llm.client import get_gemini_client
from llm.prompt import build_prompt
from config import GEMINI_MODEL

# Parse AD text using Gemini LLM and return structured data
def parse_ad_with_llm(text: str) -> dict:
    client = get_gemini_client()
    prompt = build_prompt(text)

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt
    )

    raw = response.text or ""

    cleaned = re.sub(r"^```json|```$", "", raw).strip()

    return json.loads(cleaned)
