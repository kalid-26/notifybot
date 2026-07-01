from telegram import Update
from telegram.ext import ContextTypes

from bot.services.subscribe_service import SubscriberSerivce

service_subscriber = SubscriberSerivce()

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    """
    Handle /help command
    """
    help_text = (
        "Available Commands: \n\n"
        "/start - Subscribe to notifications\n" 
        "/broadcast - Send notifications for all users\n" 
        "/schedule - Send scheduled notifications for all users\n" 
        "/stats - Show total subscribers\n" 
        "/help - Show help information\n" 
        "/unsubscribe - Stop receiving notifications"
    )
    
    await update.message.reply_text(help_text)