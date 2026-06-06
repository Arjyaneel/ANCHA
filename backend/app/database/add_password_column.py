from app.database.db import get_connection

conn = get_connection()

cursor = conn.cursor()

cursor.execute("""
ALTER TABLE users
ADD COLUMN password TEXT
""")

conn.commit()

conn.close()

print("Password column added successfully")