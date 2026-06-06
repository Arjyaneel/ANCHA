from app.database.journal_model import get_recent_entries
from app.database.pattern_model import get_emotion_stats
from app.database.db import get_connection


def get_memories(user_id):
    print("GET_MEMORIES USER ID:", user_id)
    
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
SELECT memory_content
FROM user_memories
WHERE user_id = ?
""",
(user_id,)
)
    memories = cursor.fetchall()

    conn.close()

    return memories




def build_user_context(user_id):

    recent_entries = get_recent_entries(user_id, 5)

    emotion_stats = get_emotion_stats(user_id)
    print("USER ID:", user_id)

    memories = get_memories(user_id)

    context = "\nRecent Journal Entries:\n"

    for entry in recent_entries:
        context += f"""
User: {entry['user_text']}
Emotion: {entry['emotion']}
"""

    context += "\nEmotion Trends:\n"
    context += "\nKnown Memories:\n\n"

    for memory in memories:

        context += f"{memory['memory_content']}\n"
        memories = get_memories(user_id)
        print("MEMORIES:", memories)

    for stat in emotion_stats:
        context += f"""
{stat['emotion']}: {stat['total']}
"""

    return context