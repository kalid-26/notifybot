from decouple import config
from pathlib import Path 

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATABASE_DIR = BASE_DIR / "data"
DATABASE_FILE_PATH = DATABASE_DIR / "notifyhub.db"

BOT_TOKEN = config("BOT_TOKEN")

ADMIN_IDS = [
    int(admin_id.strip())
    
    for admin_id in config("ADMIN_IDS", default="").split(",")
    if admin_id.strip()
]