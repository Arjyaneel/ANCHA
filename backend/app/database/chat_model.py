from app.database.db import get_connection

def get_checkin_count(user_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM chat_messages
        WHERE user_id = ?
        AND role = 'user'
        """,
        (user_id,)
    )

    count = cursor.fetchone()[0]

    conn.close()

    return count


def save_message(
    user_id,
    role,
    message
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO chat_messages
        (
            user_id,
            role,
            message
        )
        VALUES (?, ?, ?)
        """,
        (
            user_id,
            role,
            message
        )
    )

    conn.commit()

    conn.close()

    print(
        f"{role.upper()} MESSAGE SAVED"
    )


def search_messages(
    user_id,
    keyword
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM chat_messages
        WHERE user_id = ?
        AND message LIKE ?
        ORDER BY created_at DESC
        """,
        (
            user_id,
            f"%{keyword}%"
        )
    )

    rows = cursor.fetchall()

    conn.close()

    return rows

def get_today_messages(user_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM chat_messages
        WHERE user_id = ?
        AND DATE(created_at) = DATE('now')
        """,
        (user_id,)
    )

    rows = cursor.fetchall()

    conn.close()

    return rows



def get_recent_chat(
    user_id,
    limit=10
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM chat_messages
        WHERE user_id = ?
        ORDER BY created_at DESC
        LIMIT ?
        """,
        (
            user_id,
            limit
        )
    )

    rows = cursor.fetchall()

    conn.close()

    return rows[::-1]