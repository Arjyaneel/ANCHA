import json

# Reuse the already configured Gemini model
from app.ai.gemini_service import model


def extract_memory(user_text):

    prompt = f"""
You are a memory extraction system.

Analyze the user's message.

Determine whether it contains:

- a long-term goal
- a habit
- a personal interest
- a recurring concern
- a personal preference
- an important fact about the user

If yes, extract it.

If not, return should_save as false.

Return ONLY valid JSON.

Examples:

User:
I have been learning DSA for 6 months.

Output:
{{
    "should_save": true,
    "memory_type": "goal",
    "memory_content": "User is learning DSA",
    "importance_score": 4
}}

User:
I feel stressed today.

Output:
{{
    "should_save": false,
    "memory_type": "",
    "memory_content": "",
    "importance_score": 0
}}

User Message:

{user_text}
"""

    response = model.generate_content(prompt)

    clean_text = (
        response.text
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    return json.loads(clean_text)


# -------------------------
# TEST SECTION
# -------------------------

if __name__ == "__main__":

    result = extract_memory(
        "I have been learning DSA for 6 months."
    )

    print("\nMEMORY RESULT:\n")
    print(result)