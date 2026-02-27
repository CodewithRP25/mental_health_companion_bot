import os
from dotenv import load_dotenv
from google import genai
from pathlib import Path
# Load .env from root folder
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)
print("Gemini Key Loaded:", bool(api_key))

MODEL = "gemini-1.5-flash"  # fast & good


def generate_llm_reply(message, emotion):

    prompt = f"""
You are a supportive close friend.

User message: {message}
Detected emotion: {emotion}

Rules:
- Be warm and human
- Validate feelings first
- Keep replies short (1–3 sentences)
- Do not sound like a therapist
- Do not give heavy advice immediately
- Ask gentle follow-up sometimes
"""

    model = genai.GenerativeModel(MODEL)

    res = model.generate_content(prompt)

    return res.text