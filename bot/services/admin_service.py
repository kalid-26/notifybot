from bot.config.settings import ADMIN_IDS

class AdminService:
    """ 
    Handles admin authorization.
    """
    @staticmethod
    def is_admin(telegram_id: int,) -> bool:
        """
        Check if the user is admin 
        """
        return telegram_id in ADMIN_IDS