from app.database.pattern_model import (
    get_patterns
)

from app.database.journal_model import (
    get_recent_entries
)


def build_insights(user_id):
    """
    Generate simple personalized insights
    from the user's emotional patterns
    and recent journals.
    """

    insights = []

    patterns = get_patterns(user_id)

    journals = get_recent_entries(
        user_id,
        limit=5
    )

    # Insights from detected patterns

    for pattern in patterns:

        insights.append(
            pattern["pattern_description"]
        )

    # Insight from recent journals

    if len(journals) >= 3:

        latest_emotion = journals[0]["emotion"]

        repeated = all(
            journal["emotion"] == latest_emotion
            for journal in journals[:3]
        )

        if repeated:

            insights.append(
                f"You have been feeling '{latest_emotion}' for your last three journal entries."
            )

    # If nothing is detected

    if not insights:

        insights.append(
            "No significant emotional patterns have been detected yet."
        )

    return insights