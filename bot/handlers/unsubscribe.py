from telegram import Update
from telegram.ext import ContextTypes

from bot.services.subscribe_service import SubscriberSerivce

service_subscriber = SubscriberSerivce()

async def unsubscribe_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    """
    Handle /unsubscribe command
    """
    
    user = update.effective_user
    
    removed = service_subscriber.unsubscribe_user(
        telegram_id=user.id
    )
    
    
    if removed:
        await update.message.reply_text("Unsubscribed Successfully.")
        
    else:
        await update.message.reply_text("You are not subscribed.")
    