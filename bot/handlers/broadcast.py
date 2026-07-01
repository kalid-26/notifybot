from telegram import Update
from telegram.ext import ContextTypes

from bot.services.admin_service import AdminService
from bot.services.subscribe_service import SubscriberSerivce
from bot.services.notification_service import NotificationService

admin_service = AdminService()
subscribe_service = SubscriberSerivce()
notification_service = NotificationService()

async def broadcast_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Admin-only broadcast command.
    """
    
    user = update.effective_user
    
    if user is None:
        return
    
    # admin check 
    if not admin_service.is_admin(user.id):
        await update.message.reply_text("command not available")
        return
    
    # extract message 
    if not context.args:
        await update.message.reply_text("Usage: /broadcast <message>")
        return
    
    message = " ".join(context.args)
    
    # get subscribers 
    subscribers = subscribe_service.get_all_subs()
    
    if not subscribers:
        await update.message.reply_text("No Subscribers found.")
        return
    
    # send broadcast 
    report = await notification_service.broadcast_message(
        context=context,
        subscribers=subscribers,
        message=message,
    )
    
    # report result 
    await update.message.reply_text(
        f"Broadcast completed\n"
        f"Total: {report['total']}\n"
        f"Success: {report['success']}\n"
        f"Failed: {report['failed']}\n"
    )
    
    