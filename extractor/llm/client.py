from google import genai
from config import GOOGLE_API_KEY

# Initialize and return a Gemini LLM client
def get_gemini_client():
    return genai.Client(api_key=GOOGLE_API_KEY)
