import json
import os

import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()

print(
    "API KEY FOUND:",
    bool(os.getenv("GEMINI_API_KEY"))
)

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def get_gemini_model():
    """
    Return the shared Gemini model instance.
    """

    return model

def analyze_emotion(
    text,
    context=""
):

    prompt = f"""
You are ANCHA, an emotionally intelligent AI companion for students.

Your priorities are:

1. If there are pending follow-ups in the context,
   naturally ask about them first.

2. Use conversation history and memories
   to make the response feel personal.

3. Be warm, supportive and conversational.

4. Then analyze the user's emotional state.

USER CONTEXT:

{context}

CURRENT MESSAGE:

{text}

Return ONLY valid JSON.

Format:

{{
    "emotion": "",
    "energy_level": "",
    "mood_summary": "",
    "support_response": "",
    "tips": []
}}
"""

    try:

        response = model.generate_content(
            prompt
        )

        clean_text = (
            response.text
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        print(
            "\nRAW GEMINI RESPONSE:\n"
        )
        print(clean_text)

        data = json.loads(
            clean_text
        )

        return data

    except json.JSONDecodeError as e:

        print(
            "JSON PARSE ERROR:",
            e
        )

        print(
            "RAW RESPONSE:",
            clean_text
        )

        return {
            "emotion": "Unknown",
            "energy_level": "Unknown",
            "mood_summary":
                "Could not parse Gemini response.",
            "support_response":
                clean_text,
            "tips": []
        }

    except Exception as e:

        print(
            "GEMINI ERROR:",
            e
        )

        return {
            "emotion": "Error",
            "energy_level": "Unknown",
            "mood_summary":
                "Something went wrong while generating a response.",
            "support_response":
                "I'm having trouble responding right now. Please try again.",
            "tips": []
        }
    
def stream_ancha_response(
    text,
    context=""
):

    prompt = f"""
You are ANCHA, an emotionally intelligent AI companion.

USER CONTEXT:

{context}

CURRENT MESSAGE:

{text}

Respond naturally and conversationally.
"""

    response = model.generate_content(
        prompt,
        stream=True
    )

    for chunk in response:

        if chunk.text:

            yield chunk.text