from app.database.db import get_connection

conn = get_connection()

cursor = conn.cursor()

cursor.execute("""
DELETE FROM chat_messages
WHERE user_id = 4
""")

conn.commit()

conn.close()

print("Chat history cleared")