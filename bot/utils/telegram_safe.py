import logging

logger = logging.getLogger(__name__)

class TelegramSafeSender:
    """
    Centralized safe Telegram messaging wrapper.
    """
    
    @staticmethod
    async def send_message(bot, chat_id: int, text: str) -> bool:
        try:
            await bot.send_message(
                chat_id=chat_id,
                text=text,
            )
            return True
        except Exception as e:
            logger.warning(f"message faild for {chat_id}: {e}")
            return False