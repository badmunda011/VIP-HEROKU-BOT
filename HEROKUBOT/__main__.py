import os
import logging
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
import pyromod.listen  # Import pyromod listen

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Initialize the bot client
class HEROKUBot(Client):
    def __init__(self):
        super().__init__(
            "HEROKUBOT",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins=dict(root="HEROKUBOT/plugins"),
        )

    # Run the bot
    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.mention = self.me.mention
        print("Started Bot.")

# To run the bot

app = HEROKUBot()
    
