import json

from app.ai.gemini_service import (
    get_gemini_model
)


def detect_ai_patterns(journal_history):
    """
    Use Gemini to detect emotional
    and behavioral patterns.
    """

    model = get_gemini_model()

    prompt = f"""
You are ANCHA's Pattern Detection Engine.

Analyze the user's recent journal history.

Find recurring:

- emotions
- stress triggers
- habits
- coping strategies
- motivation patterns
- productivity changes
- social influences
- confidence changes

Return ONLY valid JSON.

Example:

{{
    "patterns":[
        {{
            "type":"Exam Stress",
            "description":"The user repeatedly becomes anxious before examinations.",
            "confidence":0.93
        }}
    ]
}}

Journal History:

{journal_history}
"""

    response = model.generate_content(prompt)

    clean_text = (
        response.text
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    return json.loads(clean_text)