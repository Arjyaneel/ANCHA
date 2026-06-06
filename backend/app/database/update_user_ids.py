from app.database.db import get_connection

conn = get_connection()

cursor = conn.cursor()

cursor.execute("""
UPDATE journal_entries
SET user_id = 1
WHERE user_id IS NULL
""")

conn.commit()

print("Rows Updated:", cursor.rowcount)

conn.close()