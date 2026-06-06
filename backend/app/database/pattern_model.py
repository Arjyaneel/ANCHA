from app.database.db import get_connection


def get_emotion_stats(user_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT emotion,
               COUNT(*) as total
        FROM journal_entries
        WHERE user_id = ?
        GROUP BY emotion
        ORDER BY total DESC
        """,
        (user_id,)
    )

    rows = cursor.fetchall()

    conn.close()

    return rows


if __name__ == "__main__":

    stats = get_emotion_stats(1)

    print("\nEmotion Statistics:\n")

    for stat in stats:
        print(dict(stat))