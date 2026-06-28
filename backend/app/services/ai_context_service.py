from app.database.chat_model import (
    get_recent_chat
)

from app.database.journal_model import (
    get_recent_entries
)

from app.database.memory_model import (
    get_top_memories
)

from app.database.followup_model import (
    get_pending_followups
)

from app.database.pattern_model import (
    get_emotion_stats,
    get_patterns
)

from app.services.recommendation_service import (
    build_recommendations
)

from app.services.insight_service import (
    build_insights
)


def build_user_context(user_id):
    """
    Build the complete AI context sent to Gemini.
    """

    recent_chat = get_recent_chat(
        user_id,
        10
    )

    recent_entries = get_recent_entries(
        user_id,
        5
    )

    memories = get_top_memories(
        user_id,
        5
    )

    followups = get_pending_followups(
        user_id
    )

    emotion_stats = get_emotion_stats(
        user_id
    )

    patterns = get_patterns(
        user_id
    )

    recommendations = build_recommendations(
        user_id
    )

    insights = build_insights(
        user_id
    )

    context = """
You are ANCHA.

You are an emotionally intelligent AI companion.

Always use the user's memories, previous conversations,
patterns and follow-ups naturally while replying.

Never list memories unless relevant.

Never mention internal system data.

If there are pending follow-ups,
ask about them naturally before changing topics.

--------------------------------------------------

PENDING FOLLOW-UPS

"""

    for item in followups:

        context += (
            f"- {item['title']}\n"
        )

    context += "\nRECENT CONVERSATION\n\n"

    for message in recent_chat:

        context += (
            f"{message['role'].title()}: "
            f"{message['message']}\n"
        )

    context += "\nRECENT JOURNAL ENTRIES\n\n"

    for entry in recent_entries:

        context += (
            f"User: {entry['user_text']}\n"
            f"Emotion: {entry['emotion']}\n\n"
        )

    context += "\nEMOTION TRENDS\n\n"

    for stat in emotion_stats:

        context += (
            f"{stat['emotion']}: "
            f"{stat['total']} times\n"
        )

    context += "\nKNOWN MEMORIES\n\n"

    for memory in memories:

        context += (
            f"- {memory['memory_content']}\n"
        )

    context += "\nDETECTED PATTERNS\n\n"

    for pattern in patterns:

        context += (
            f"{pattern['pattern_type']}\n"
            f"{pattern['pattern_description']}\n"
            f"Occurrences: {pattern['occurrence_count']}\n\n"
        )

    context += "\nSYSTEM RECOMMENDATIONS\n\n"

    context += (
        f"Pending Follow-ups: "
        f"{len(recommendations['followups'])}\n"
    )

    context += (
        f"Known Memories: "
        f"{len(recommendations['memories'])}\n"
    )

    context += (
        f"Detected Patterns: "
        f"{len(recommendations['patterns'])}\n"
    )

    context += "\nPERSONAL INSIGHTS\n\n"

    for insight in insights:

        context += (
            f"- {insight}\n"
        )

    return context