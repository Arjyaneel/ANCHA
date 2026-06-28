from app.database.db import get_connection


def create_user(
    username,
    password_hash
):
    """
    Create a new user.
    The password should already be hashed before calling this function.
    """

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO users
        (
            username,
            password_hash
        )
        VALUES (?, ?)
        """,
        (
            username,
            password_hash
        )
    )

    conn.commit()

    user_id = cursor.lastrowid

    conn.close()

    return user_id


def get_user_by_username(username):
    """
    Retrieve a user by username.
    """

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE username = ?
        """,
        (username,)
    )

    user = cursor.fetchone()

    conn.close()

    return user


def get_user_by_id(user_id):
    """
    Retrieve a user by ID.
    """

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE id = ?
        """,
        (user_id,)
    )

    user = cursor.fetchone()

    conn.close()

    return user