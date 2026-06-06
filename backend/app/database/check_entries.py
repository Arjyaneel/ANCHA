from app.database.db import get_connection

from app.database.db import DATABASE_NAME

print("DATABASE:", DATABASE_NAME)

conn = get_connection()

cursor = conn.cursor()

cursor.execute("SELECT * FROM journal_entries")

rows = cursor.fetchall()

for row in rows:
    print(dict(row))

conn.close()