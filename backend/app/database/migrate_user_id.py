from app.database.db import get_connection

conn = get_connection()

cursor = conn.cursor()

try:
    cursor.execute("""
    ALTER TABLE journal_entries
    ADD COLUMN user_id INTEGER
    """)

    print("user_id column added.")

except Exception as e:
    print("Already exists or error:", e)

conn.commit()
conn.close()