import logging
from telegram.ext import ApplicationBuilder

from bot.config.settings import BOT_TOKEN
from bot.database.schema import initialize_database

from bot.handlers.register import register_handlers
from bot.utils.logger import setup_logging

# from bot.services.subscribe_service import SubscriberSerivce

logger = logging.getLogger(__name__)

def main() -> None:
    
    """
    Application Entry Point
    """
    setup_logging()
    initialize_database()
    
    application = (ApplicationBuilder().token(BOT_TOKEN).build())
    
    register_handlers(application)
    
    logger.info("NotifyBot is running...")
    
    application.run_polling()
    
if __name__ == "__main__":
    main()