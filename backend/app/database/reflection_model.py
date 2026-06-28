from app.database.db import get_connection


def reflection_exists(
    user_id,
    title
):
    """
    Check whether a reflection
    already exists.
    """

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id
        FROM user_reflections
        WHERE user_id = ?
        AND title = ?
        """,
        (
            user_id,
            title
        )
    )

    result = cursor.fetchone()

    conn.close()

    return result is not None


def save_reflection(
    user_id,
    title,
    reflection,
    confidence
):
    """
    Save a new reflection.
    """

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO user_reflections
        (
            user_id,
            title,
            reflection,
            confidence
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            user_id,
            title,
            reflection,
            confidence
        )
    )

    conn.commit()

    conn.close()


def update_reflection(
    user_id,
    title,
    reflection,
    confidence
):
    """
    Update an existing reflection.
    """

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE user_reflections

        SET reflection = ?,
            confidence = ?,
            updated_at = CURRENT_TIMESTAMP

        WHERE user_id = ?
        AND title = ?
        """,
        (
            reflection,
            confidence,
            user_id,
            title
        )
    )

    conn.commit()

    conn.close()


def get_reflections(
    user_id,
    limit=10
):
    """
    Retrieve reflections
    ordered by confidence.
    """

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *

        FROM user_reflections

        WHERE user_id = ?

        ORDER BY confidence DESC,
                 updated_at DESC

        LIMIT ?
        """,
        (
            user_id,
            limit
        )
    )

    rows = cursor.fetchall()

    conn.close()

    return rows

