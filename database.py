import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "data", "sparesroom.db")

def get_connection():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)

    # CREATE TABLE IF NOT EXISTD makes this safe to call on every connection,
    # not just the first time the app runs. 
    conn.execute(""" 
        CREATE TABLE IF NOT EXISTS parts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        qty INTEGER NOT NULL,
        reorder_point INTEGER NOT NULL,
        description TEXT
        )
    """)
    conn.commit()
    return conn