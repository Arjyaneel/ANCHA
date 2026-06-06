from app.database.db import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("PRAGMA table_info(users)")

columns = cursor.fetchall()

for column in columns:
    print(dict(column))

conn.close()