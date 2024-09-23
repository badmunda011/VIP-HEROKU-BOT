import os
import logging
import pyrogram
from config import API_ID, API_HASH, BOT_TOKEN, OWNER_ID

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


if __name__ == "__main__" :
    print("Starting Bot...")
    plugins = dict(root="HEROKUBOT/plugins")
    app = pyrogram.Client(
        "HEROKUBOT",
        bot_token=BOT_TOKEN,
        api_id=API_ID,
        api_hash=API_HASH,
        plugins=plugins
    )
    app.run()
