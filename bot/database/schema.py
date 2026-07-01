from bot.database.connection import get_connection


subscribers_table = """
    CREATE TABLE IF NOT EXISTS Subscribers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id  INTEGER NOT NULL UNIQUE,
        username TEXT,
        first_name TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
"""

def initialize_database() -> None:
    """
        Create all required tables
    """
    
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(subscribers_table)
        conn.commit()
    finally:
        conn.close()