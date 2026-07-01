from bot.repositories.subs_repo import subs_repository

class SubscriberSerivce:
    """ 
    Business Logic for subscribers.
    """
    
    def __init__(self):
        self.repository = subs_repository()
    
    
    def subscribe_user(
        self, 
        telegram_id: int, 
        username: bool | None, 
        first_name: bool | None
    ) -> bool:
        
        """
        Subscribe new users.  
        Returns: 
            True if new subscriber
            False if already in registerd
        """
        
        existing_users = (self.repository.get_by_telegram_id(telegram_id))
        
        if existing_users:
            return False
        
        return self.repository.create(
            telegram_id=telegram_id,
            username=username,
            first_name=first_name,
        )
        
        
    def unsubscribe_user(self, telegram_id: int) -> bool:
        """
        Unsubscribe user
        Returns:
            True if user is removed
            False if user not found
        """
        return self.repository.delete(telegram_id)
    
    
    def total_subscribers(self) -> int:
        """
        List and Count all subscribers
        """
        return self.repository.count()
    
    
    def get_all_subs(self) -> None:
        """
        Return all subscribers.
        """
        return self.repository.get_all()