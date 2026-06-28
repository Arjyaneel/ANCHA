from app.database.pattern_model import get_emotion_stats
from Backend.app.services.ai_context_service import get_memories


def get_dashboard_data(user_id):

    emotion_stats = get_emotion_stats(user_id)

    memories = get_memories(user_id)

    return {
        "emotion_stats": [
            {
                "emotion": stat["emotion"],
                "count": stat["total"]
            }
            for stat in emotion_stats
        ],

        "memories": [
            memory["memory_content"]
            for memory in memories
        ]
    }