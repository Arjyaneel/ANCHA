import sqlite3

conn = sqlite3.connect("ancha.db")

cursor = conn.cursor()

# USERS TABLE

cursor.execute("""
CREATE TABLE IF NOT EXISTS user_memories (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_id INTEGER NOT NULL,

    memory_type TEXT,

    memory_content TEXT,

    importance_score INTEGER DEFAULT 1,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(user_id) REFERENCES users(id)

)
""")

# JOURNAL TABLE

cursor.execute("""
CREATE TABLE IF NOT EXISTS journal_entries (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_text TEXT NOT NULL,

    emotion TEXT,

    energy_level TEXT,

    mood_summary TEXT,

    support_response TEXT,

    tips TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)
""")

conn.commit()
conn.close()

print("Database created successfully")