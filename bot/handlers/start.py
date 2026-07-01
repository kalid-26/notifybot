from telegram import Update
from telegram.ext import ContextTypes

from bot.services.subscribe_service import SubscriberSerivce


subscribe_service = SubscriberSerivce()

async def start_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """_summary_

    Handle /start command and register users automatically.
    """
    
    user = update.effective_user
    
    if user is None:
        return
    
    subscribed = subscribe_service.subscribe_user(
        telegram_id=user.id,
        username=user.username,
        first_name=user.first_name,
    )
    
    if subscribed:
        await update.message.reply_text(
            "You have successfully subscribed to notifications."
        )
    else:
        await update.message.reply_text(
            "You are already subscribed."
        )