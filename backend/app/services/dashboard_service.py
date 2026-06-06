from app.database.journal_model import get_recent_entries
from app.database.pattern_model import get_emotion_stats
from app.database.memory_model import get_memories


def get_dashboard_data(user_id):

    emotions = get_emotion_stats(user_id)

    memories = get_memories(user_id)

    journals = get_recent_entries(user_id, 10)

    return {

        "emotion_stats": [
            dict(x)
            for x in emotions
        ],

        "memories": [
            dict(x)
            for x in memories
        ],

        "recent_entries": [
            dict(x)
            for x in journals
        ]
    }