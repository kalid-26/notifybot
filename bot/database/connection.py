import sqlite3
from bot.config.settings import DATABASE_FILE_PATH

def get_connection() -> sqlite3.Connection:
    """
        create and returns SQLite connection.
    """
    
    connection = sqlite3.connect(DATABASE_FILE_PATH)
    connection.row_factory = sqlite3.Row
    
    return connection