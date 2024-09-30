import logging
import os

import pyromod.listen  # Import pyromod listen
from pyrogram import Client, filters

from config import API_HASH, API_ID, BOT_TOKEN, OWNER_ID

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.ERROR
)
filters.sudo = filters.create(
    lambda _, __, m: bool(m.from_user and (m.from_user.id in OWNER_ID)),
    "SudoFilter",
)
# Initialize the bot client
plugins = dict(root="HEROKUBOT/plugins")
app = Client(
    "HEROKUBOT",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
)

filters.user = filters.user()
