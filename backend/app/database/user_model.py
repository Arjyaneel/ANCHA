from app.database.db import get_connection


def create_user(username, password):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO users
        (
            username,
            password
        )
        VALUES (?, ?)
        """,
        (
            username,
            password
        )
    )

    conn.commit()

    user_id = cursor.lastrowid

    conn.close()

    return user_id


def get_user_by_username(username):

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


if __name__ == "__main__":

    user_id = create_user(
        "Tanmay",
        "123456"
    )

    print("User Created:", user_id)