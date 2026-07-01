from telegram import Update
from telegram.ext import ContextTypes

from bot.services.admin_service import AdminService
from bot.jobs.scheduled_broadcast import scheduled_broadcast

admin_service = AdminService()


async def schedule_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Schedule a future broadcast.
    """
    
    user = update.effective_user
    
    if user is None:
        return
    
    if not admin_service.is_admin(user.id):
        await update.message.reply_text("Anavailable Command")
        return
    # arugument validation 
    if len(context.args) < 2:
        await update.message.reply_text(
            "Usage: /schedule <seconds> <message>"
        )
        return
    
    try:
        seconds = int(
            context.args[0]
        )
        
    except ValueError:
        await update.message.reply_text(
            "seconds must be a number"
        )
        return
    
    message = " ".join(
        context.args[1:]
    )
    
    # create a job 
    context.job_queue.run_once(
        callback=scheduled_broadcast,
        when=seconds,
        data={
            "message": message,
        },
    )
    
    print(context.job_queue)
    await update.message.reply_text(
        f"Broadcast scheduled in "
        f"{seconds} seconds"
    )