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


