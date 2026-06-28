from app.database.db import get_connection


def followup_exists(
    user_id,
    title
):
    """
    Check whether a pending followups with the same title already exists.
    """

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id
        FROM followups
        WHERE user_id = ?
        AND title = ?
        AND status = 'pending'
        """,
        (
            user_id,
            title
        )
    )

    result = cursor.fetchone()

    conn.close()

    return result is not None


def save_followup(
    user_id,
    title,
    description,
    due_date,
    priority="normal"
):
    """
    Save a new followups.
    """

    if followup_exists(
        user_id,
        title
    ):
        return

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO followups
        (
            user_id,
            title,
            description,
            due_date,
            priority
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            user_id,
            title,
            description,
            due_date,
            priority
        )
    )

    conn.commit()

    conn.close()


def get_pending_followups(
    user_id,
    limit=3
):
    """
    Return pending followups.
    """

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM followups
        WHERE user_id = ?
        AND status = 'pending'
        ORDER BY due_date ASC
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


def get_due_followups(
    user_id
):
    """
    Return followups that are due.
    """

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM followups
        WHERE user_id = ?
        AND status = 'pending'
        AND due_date <= CURRENT_TIMESTAMP
        ORDER BY due_date ASC
        """,
        (user_id,)
    )

    rows = cursor.fetchall()

    conn.close()

    return rows


def complete_followup(
    user_id,
    title
):
    """
    Mark a followups as completed.
    """

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE followups
        SET
            status = 'completed',
            completed_at = CURRENT_TIMESTAMP
        WHERE user_id = ?
        AND title = ?
        AND status = 'pending'
        """,
        (
            user_id,
            title
        )
    )

    conn.commit()

    conn.close()