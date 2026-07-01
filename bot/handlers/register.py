from telegram.ext import CommandHandler, Application

from bot.handlers.start import start_cmd
from bot.handlers.broadcast import broadcast_cmd
from bot.handlers.help import help_cmd
from bot.handlers.unsubscribe import unsubscribe_cmd
from bot.handlers.stats import stats_cmd
from bot.handlers.schedule import schedule_cmd



def register_handlers(application: Application) -> None:
    
    application.add_handler(CommandHandler("start", start_cmd))
    application.add_handler(CommandHandler("broadcast", broadcast_cmd))
    application.add_handler(CommandHandler("schedule", schedule_cmd))
    application.add_handler(CommandHandler("stats", stats_cmd))
    application.add_handler(CommandHandler("unsubscribe", unsubscribe_cmd))
    application.add_handler(CommandHandler("help", help_cmd))