import json
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_emotion(text, context=""):

    prompt = f"""
You are Ancha, an emotionally intelligent AI companion.

User Emotional History:

{context}

Current Journal Entry:

{text}

Analyze the current emotional state while considering
the user's recent emotional patterns and history.

Return ONLY valid JSON in this format:

{{
    "emotion": "",
    "energy_level": "",
    "mood_summary": "",
    "support_response": "",
    "tips": []
}}
"""

    response = model.generate_content(prompt)

    clean_text = (
        response.text
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    return json.loads(clean_text)