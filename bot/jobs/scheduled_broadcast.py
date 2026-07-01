import logging
from telegram.ext import ContextTypes

from bot.services.subscribe_service import SubscriberSerivce
from bot.services.notification_service import NotificationService

logger = logging.getLogger(__name__)

subscriber_Service = SubscriberSerivce()
notification_Service = NotificationService()

async def scheduled_broadcast(context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Execute a scheduled broadcast.
    """
    
    job_data = context.job.data
    
    message = job_data["message"]
    
    subscribers = (
        subscriber_Service.get_all_subs()
    )
    
    if not subscribers:
        logger.info(
            "Scheduled broadcast skipped. No subscribers found."
        )
        return

    report = await notification_Service.broadcast_message(
        context=context,
        subscribers=subscribers,
        message=message,
    )
    
    logger.info(
        "Scheduled broadcast completed. "
        f"Success={report['success']} "
        f"Failed={report['failed']}"
    )