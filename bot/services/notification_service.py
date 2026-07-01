import logging
import asyncio
from telegram.ext import ContextTypes 

from bot.utils.telegram_safe import TelegramSafeSender

logger = logging.getLogger(__name__)


class NotificationService:
    """
    Responsible for sending messages to multiple users safely. 
    """
    
    async def broadcast_message(
        self, 
        context: ContextTypes.DEFAULT_TYPE, 
        subscribers: list, 
        message: str
    ) -> dict:
        
        """
        Sends message to all subscribers.

        Returns:
            dict: delivery report (success, failed)
        """
        
        success = 0
        failed = 0
        
        for subscriber in subscribers:
            chat_id = subscriber["telegram_id"]
            
            result = await TelegramSafeSender.send_message(
                bot=context.bot,
                chat_id=chat_id,
                text=message,
            )

            if result:
                success += 1
            else:
                failed += 1
            
            # rate limiting
            await asyncio.sleep(0.05)
        return {
            "success": success,
            "failed": failed,
            "total": len(subscribers)
        }
    
    
    