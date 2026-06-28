import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DATABASE = os.path.join(BASE_DIR, "ancha.db")

print("CREATE_TABLES DATABASE:", DATABASE)

conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()


print("CREATE TABLES DATABASE:", os.path.abspath(DATABASE))

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    username TEXT UNIQUE NOT NULL,

    password_hash TEXT NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS chat_messages (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_id INTEGER NOT NULL,

    role TEXT NOT NULL,

    message TEXT NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(user_id)
    REFERENCES users(id)

)
""")


# JOURNAL ENTRIES TABLE

cursor.execute("""
CREATE TABLE IF NOT EXISTS journal_entries (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_id INTEGER NOT NULL,

    user_text TEXT NOT NULL,

    emotion TEXT,

    energy_level TEXT,

    mood_summary TEXT,

    support_response TEXT,

    tips TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(user_id)
    REFERENCES users(id)

)
""")


# USER MEMORIES TABLE

cursor.execute("""
CREATE TABLE IF NOT EXISTS user_memories (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_id INTEGER NOT NULL,

    memory_type TEXT NOT NULL,

    memory_content TEXT NOT NULL,

    importance_score REAL DEFAULT 1.0,

    source TEXT DEFAULT 'chat',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(user_id)
    REFERENCES users(id)

)
""")

# FOLLOWUPS TABLE

cursor.execute("""
CREATE TABLE IF NOT EXISTS followups (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_id INTEGER NOT NULL,

    title TEXT NOT NULL,

    description TEXT,

    due_date TIMESTAMP NOT NULL,

    status TEXT DEFAULT 'pending',

    priority TEXT DEFAULT 'normal',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    completed_at TIMESTAMP,

    FOREIGN KEY(user_id)
    REFERENCES users(id)

)
""")

# EMOTION PATTERNS TABLE

cursor.execute("""
CREATE TABLE IF NOT EXISTS emotion_patterns (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_id INTEGER NOT NULL,

    pattern_type TEXT NOT NULL,

    pattern_description TEXT NOT NULL,

    confidence REAL DEFAULT 0.50,

    occurrence_count INTEGER DEFAULT 1,

    last_detected TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(user_id)
    REFERENCES users(id)

)
""")


# USER REFLECTIONS TABLE

cursor.execute("""
CREATE TABLE IF NOT EXISTS user_reflections (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_id INTEGER NOT NULL,

    title TEXT NOT NULL,

    reflection TEXT NOT NULL,

    confidence REAL DEFAULT 0.50,

    source TEXT DEFAULT 'ai',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(user_id)
    REFERENCES users(id)

)
""")

conn.commit()

conn.close()

print("Database created successfully.")



