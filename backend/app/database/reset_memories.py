from app.database.db import get_connection

conn = get_connection()

cursor = conn.cursor()

cursor.execute("""
DELETE FROM user_memories
WHERE user_id = 1
""")

conn.commit()

conn.close()

print("Memories deleted successfully")