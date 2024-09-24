
import re
from os import getenv

from dotenv import load_dotenv

load_dotenv()


# Get it from my.telegram.org

API_ID = getenv("API_ID", "")

API_HASH = getenv("API_HASH")


## Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")


# Database to save your chats and stats... Get MongoDB:-  https://telegra.ph/How-To-get-Mongodb-URI-04-06
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

HEROKU_API_KEY = getenv("HEROKU_API_KEY", "")

OWNER_ID = getenv("OWNER_ID", "1808943146")
    
