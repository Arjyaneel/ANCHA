from app.database.pattern_model import (
    pattern_exists,
    save_pattern,
    update_pattern
)

from app.database.journal_model import (
    get_recent_entries
)

from app.ai.pattern_detector import (
    detect_ai_patterns
)

from app.database.pattern_model import (
    pattern_exists,
    save_pattern,
    update_pattern
)

from app.database.journal_model import (
    get_recent_entries
)


def detect_emotion_pattern(
    user_id
):
    """
    Detect repeated emotions
    from recent journal entries.
    """

    journals = get_recent_entries(
        user_id,
        limit=5
    )

    if len(journals) < 3:
        return

    latest_emotion = journals[0]["emotion"]

    repeated = all(
        entry["emotion"] == latest_emotion
        for entry in journals[:3]
    )

    if not repeated:
        return

    pattern_name = f"Repeated {latest_emotion}"

    if pattern_exists(
        user_id,
        pattern_name
    ):

        update_pattern(
            user_id,
            pattern_name
        )

    else:

        save_pattern(
            user_id,
            pattern_name,
            (
                f"User has experienced "
                f"{latest_emotion} repeatedly "
                "over recent conversations."
            ),
            0.85
        )

def build_journal_history(journals):
    """
    Convert journal rows into readable text
    for Gemini.
    """

    history = ""

    for journal in journals:

        history += (
            f"Date: {journal['created_at']}\n"
            f"Emotion: {journal['emotion']}\n"
            f"Journal: {journal['user_text']}\n\n"
        )

    return history

def detect_ai_emotional_patterns(user_id):
    """
    Ask Gemini to discover long-term
    emotional patterns.
    """

    journals = get_recent_entries(
        user_id,
        limit=10
    )

    if len(journals) < 5:
        return

    history = build_journal_history(
        journals
    )

    result = detect_ai_patterns(
        history
    )

    for pattern in result["patterns"]:

        if pattern_exists(
            user_id,
            pattern["type"]
        ):

            update_pattern(
                user_id,
                pattern["type"]
            )

        else:

            save_pattern(
                user_id,
                pattern["type"],
                pattern["description"],
                pattern["confidence"]
            )

def process_patterns(
    user_id
):
    """
    Run all pattern detectors.
    """

    detect_emotion_pattern(
        user_id
    )

    detect_ai_emotional_patterns(
        user_id
    )