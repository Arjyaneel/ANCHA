import json

from app.ai.gemini_service import model


def generate_reflections(
    journals,
    memories,
    patterns
):
    """
    Ask Gemini to generate long-term
    reflections about the user.
    """

    prompt = f"""
You are ANCHA.

Below is information about a user.

Recent Journals:
{journals}

Known Memories:
{memories}

Detected Patterns:
{patterns}

Your job is NOT to summarize.

Instead identify long-term insights
about the user.

Generate between 1 and 3 reflections.

Return ONLY valid JSON.

Format:

{{
    "reflections":[
        {{
            "title":"",
            "reflection":"",
            "confidence":0.90
        }}
    ]
}}
"""

    try:

        response = model.generate_content(
            prompt
        )

        clean = (
            response.text
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        return json.loads(clean)

    except Exception as e:

        print(
            "REFLECTION GENERATION ERROR:",
            e
        )

        return {
            "reflections":[]
        }
    
if __name__ == "__main__":

    journals = """
    User feels anxious before exams.
    User felt confident after finishing.
    """

    memories = """
    User wants to become a software engineer.
    """

    patterns = """
    Repeated Anxiety
    """

    result = generate_reflections(
        journals,
        memories,
        patterns
    )

    print(result)