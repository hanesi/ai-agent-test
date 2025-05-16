import sqlite3
from datetime import datetime

DB_PATH = "user_memory.db"

# Create table if it doesn't exist
def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS user_memory (
                user_id TEXT PRIMARY KEY,
                behavior_summary TEXT,
                last_suggestion TEXT,
                last_updated TIMESTAMP
            )
        """)
        conn.commit()

# Get stored memory for a user
def get_user_memory(user_id: str):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT behavior_summary, last_suggestion FROM user_memory WHERE user_id = ?", (user_id,))
        row = cursor.fetchone()
        return {"behavior_summary": row[0], "last_suggestion": row[1]} if row else None

# Save or update memory
def save_user_memory(user_id: str, behavior_summary: str, last_suggestion: str):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            INSERT INTO user_memory (user_id, behavior_summary, last_suggestion, last_updated)
            VALUES (?, ?, ?, ?)
            ON CONFLICT(user_id) DO UPDATE SET
                behavior_summary=excluded.behavior_summary,
                last_suggestion=excluded.last_suggestion,
                last_updated=excluded.last_updated
        """, (user_id, behavior_summary, last_suggestion, datetime.utcnow()))
        conn.commit()
