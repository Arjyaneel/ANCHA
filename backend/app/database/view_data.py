from app.database.db import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
SELECT name
FROM sqlite_master
WHERE type='table'
""")

tables = cursor.fetchall()

print("TABLES:")

for table in tables:
    print(table["name"])

conn.close()