from app.database.db import get_connection

conn = get_connection()

cursor = conn.cursor()

cursor.execute("""
SELECT memory_content
FROM user_memories
WHERE user_id = ?
""")

conn.commit()
conn.close()

print("Memories table created successfully")