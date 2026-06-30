from app.database.db import get_connection


def create_user(
    username,
    email,
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
            email,
            password_hash
        )
        VALUES (?, ?, ?)
        """,
        (
            username,
            email,
            password_hash
        )
    )
    conn.commit()

    user_id = cursor.lastrowid

    conn.close()

    return user_id



def get_user_by_email(email):
    conn = get_connection()
    cursor = conn.cursor()

    print("=" * 50)

    cursor.execute("PRAGMA table_info(users)")
    print(cursor.fetchall())

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    cursor.execute("PRAGMA table_info(users)")

    for row in cursor.fetchall():
        print(dict(row))

    cursor.execute("SELECT * FROM users LIMIT 1")
    row = cursor.fetchone()

    if row:
        print(dict(row))

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE email = ?
        """,
        (email,)
    )

    user = cursor.fetchone()

    conn.close()

    return user


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