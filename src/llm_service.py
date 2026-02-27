import os
from google import genai

client = genai(
    api_key=os.getenv("GENAI_API_KEY"),
)

MODEL = "gemini-1.5-flash"  # free & good


def generate_llm_reply(message, emotion):

    prompt = f"""
You are a supportive close friend.

User message: {message}
Detected emotion: {emotion}

Rules:
- Be warm and human
- Validate feelings first3
- Keep replies short (1–3 sentences)
- Do not sound like a therapist
- Do not give heavy advice immediately
- Ask gentle follow-up sometimes
"""
    res = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return res.choices[0].message.content