from app.database.db import get_connection


def memory_exists(user_id, memory_content):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id
        FROM user_memories
        WHERE user_id = ?
        AND memory_content = ?
        """,
        (user_id, memory_content)
    )

    result = cursor.fetchone()

    conn.close()

    return result is not None


def save_memory(
    user_id,
    memory_type,
    memory_content,
    importance_score
):

    if memory_exists(user_id, memory_content):

        print("MEMORY ALREADY EXISTS")

        return

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO user_memories
        (
            user_id,
            memory_type,
            memory_content,
            importance_score
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            user_id,
            memory_type,
            memory_content,
            importance_score
        )
    )

    conn.commit()

    conn.close()

    print("NEW MEMORY SAVED")

def get_memories(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM user_memories
        WHERE user_id = ?
        ORDER BY importance_score DESC
        """,
        (user_id,)
    )

    rows = cursor.fetchall()

    conn.close()

    return rows
