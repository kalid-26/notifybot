from sqlite3 import IntegrityError
from typing import Optional

from bot.database.connection import get_connection


class subs_repository:
    """
        Handle all subscribers operation
    """
    
    @staticmethod
    def create(
        telegram_id: int,
        username: str | None,
        first_name: str | None,
    ) -> bool:
        
        """
        Inserts a subscriber. 
        If inserted: True 
        If already exists: False
        """
        
        conn = get_connection()
        try:
            cursor = conn.cursor()
            
            cursor.execute(
                """ INSERT INTO Subscribers
                (telegram_id, username, first_name)
                VALUES(?, ?, ?) 
                """,
                (telegram_id, username, first_name),
            )
            
            conn.commit()
            return True
        except IntegrityError:
            return False
        finally:
            conn.close()
            
    @staticmethod
    def get_by_telegram_id(telegram_id: int,):
        
        """
        Get subscriber by telegram_id 
        """
        
        conn = get_connection()
        
        try:
            cursor = conn.cursor()
            
            cursor.execute(
                """
                SELECT * FROM Subscribers WHERE telegram_id = ?
                """,
                (telegram_id,),
            )
            
            return cursor.fetchone()
        
        finally:
            conn.close()
        
    
    @staticmethod
    def count() -> int:
        """
        List all subscribers(Total Subscribers). 
        """
        conn = get_connection()
        
        try: 
            cursor = conn.cursor()
            
            cursor.execute(
                """
                SELECT COUNT(*) FROM Subscribers
                """
            )
            return cursor.fetchone()[0] 

        finally:
            conn.close()
            
    @staticmethod
    def get_all():
        """
        Getting all subscribers lists
        """
        conn = get_connection()
        
        try:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT * FROM Subscribers 
                """
            )
            return cursor.fetchall()
        finally:
            conn.close()
    @staticmethod
    def delete(telegram_id: int) -> bool:
        """
        Unsubscirbe or delete subscriber from database (Remove subscriber)
        """
        
        conn = get_connection()
        
        try: 
            cursor = conn.cursor()
            cursor.execute(
                """
                DELETE FROM Subscribers WHERE telegram_id = ? 
                """,
                (telegram_id,),
            )
            
            conn.commit()
            return cursor.rowcount > 0
        
        finally:
            conn.close()