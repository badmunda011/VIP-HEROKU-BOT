from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = getenv("API_ID", "")

API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")

HEROKU_API_KEY = getenv("HEROKU_API_KEY", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6815918609 1808943146").split()))
