from app.database.db import get_connection


def save_entry(
    user_id,
    user_text,
    emotion,
    energy_level,
    mood_summary,
    support_response,
    tips
):

    print("SAVE ENTRY CALLED")

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO journal_entries
        (
            user_id,
            user_text,
            emotion,
            energy_level,
            mood_summary,
            support_response,
            tips
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            user_id,
            user_text,
            emotion,
            energy_level,
            mood_summary,
            support_response,
            tips
        )
    )

    conn.commit()

    conn.close()

    print("INSERT SUCCESSFUL")




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

def get_journal_count(user_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM journal_entries
        WHERE user_id = ?
        """,
        (user_id,)
    )

    count = cursor.fetchone()[0]

    conn.close()

    return count

def get_weekly_entries(user_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM journal_entries
        WHERE user_id = ?
        AND DATE(created_at)
            >= DATE('now','-6 days')
        ORDER BY created_at ASC
        """,
        (user_id,)
    )

    rows = cursor.fetchall()

    conn.close()

    return rows

def get_latest_emotion(user_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT emotion
        FROM journal_entries
        WHERE user_id = ?
        ORDER BY created_at DESC
        LIMIT 1
        """,
        (user_id,)
    )

    row = cursor.fetchone()

    conn.close()

    return row



if __name__ == "__main__":

    entries = get_recent_entries(1)

    print("\nRecent Entries:\n")

    for entry in entries:
        print(dict(entry))