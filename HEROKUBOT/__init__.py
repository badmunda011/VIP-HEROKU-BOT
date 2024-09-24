import os
import pyrogram
import logging
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
import pyromod.listen  # Import pyromod listen

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Initialize the bot client
plugins = dict(root="HEROKUBOT/plugins")
app = pyrogram.Client(
    "HEROKUBOT",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=plugins
)