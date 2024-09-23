import os
import logging
import pyrogram
from config import API_ID, API_HASH, BOT_TOKEN
import pyromod.listen   # Import pyromod listen

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

if __name__ == "__main__":
    print("Starting Bot...")
    
    plugins = dict(root="HEROKUBOT/plugins")
    
    # Initialize the bot client
    app = pyrogram.Client(
        "HEROKUBOT",
        bot_token=BOT_TOKEN,
        api_id=API_ID,
        api_hash=API_HASH,
        plugins=plugins
    )
    
    

    # Run the bot
    app.run()
    print("Started Bot.")
