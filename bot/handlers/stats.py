from telegram import Update
from telegram.ext import ContextTypes

from bot.services.subscribe_service import SubscriberSerivce
from bot.services.admin_service import AdminService

admin_service = AdminService()
service_subscriber = SubscriberSerivce()

async def stats_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    """
    Show subscriber statistics.
    """
    user = update.effective_user 
    
    if user is None:
        return
    
    if not admin_service.is_admin(user.id):
        await update.message.reply_text("Command is not available!")
        return
    
    total_subs = (service_subscriber.total_subscribers())
    await update.message.reply_text(f"Total Subscribers: {total_subs}")