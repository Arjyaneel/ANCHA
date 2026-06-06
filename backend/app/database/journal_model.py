from app.database.db import get_connection


def get_recent_entries(user_id, limit=5):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM journal_entries
        WHERE user_id = ?
        ORDER BY created_at DESC
        LIMIT ?
        """,
        (user_id, limit)
    )

    rows = cursor.fetchall()

    conn.close()

    return rows


if __name__ == "__main__":

    entries = get_recent_entries(1)

    print("\nRecent Entries:\n")

    for entry in entries:
        print(dict(entry))