import sqlite3
from datetime import datetime

db = sqlite3.connect("memory.db", check_same_thread=False)
cur = db.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS memory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source TEXT,
    format TEXT,
    intent TEXT,
    metadata TEXT,
    timestamp TEXT,
    conversation_id TEXT
)''')
db.commit()

def store_memory(source, format, intent, metadata, conversation_id=None):
    cur.execute("INSERT INTO memory (source, format, intent, metadata, timestamp, conversation_id) VALUES (?, ?, ?, ?, ?, ?)",
                (source, format, intent, metadata, datetime.now().isoformat(), conversation_id))
    db.commit()

def read_memory():
    cur.execute("SELECT * FROM memory")
    return cur.fetchall()
