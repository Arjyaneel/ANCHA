from app.database.db import get_connection


def normalize_memory(text):
    """
    Normalize memory text before storing/searching.
    """

    return (
        text
        .strip()
        .lower()
        .rstrip(".!?")
    )


def memory_exists(user_id, memory_content):
    """
    Check whether a memory already exists.
    """

    memory_content = normalize_memory(
        memory_content
    )

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id
        FROM user_memories
        WHERE user_id = ?
        AND LOWER(memory_content) = ?
        """,
        (
            user_id,
            memory_content
        )
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
    """
    Save a new memory.
    """

    memory_content = normalize_memory(
        memory_content
    )

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


def get_memories(user_id):
    """
    Return all memories ordered by importance.
    """

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


def get_top_memories(
    user_id,
    limit=5
):
    """
    Return the most important memories.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            memory_content,
            importance_score
        FROM user_memories
        WHERE user_id = ?
        ORDER BY importance_score DESC
        LIMIT ?
        """,
        (
            user_id,
            limit
        )
    )

    memories = cursor.fetchall()

    conn.close()

    return memories