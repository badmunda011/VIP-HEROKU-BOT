import importlib
import asyncio
import os
from HEROKUBOT import app, SUDOERS
from pyrogram import idle
from config import OWNER_ID
async def main():
    print("Starting Bot.....")
    await app.start()
    for id in OWNER_ID:
        SUDOERS.add(id)
    print("Bot Started.....")

    for file in os.listdir("HEROKUBOT/plugins"):
        if file.endswith(".py") and not file.startswith("__"):
            module_name = file[:-3]
            importlib.import_module(f"HEROKUBOT.plugins.{module_name}")

    await idle()
    print("Bot Stopped.....")
    await app.stop()


if __name__ == "__main__":
    loop = asyncio.get_event_loop_policy().get_event_loop()
    loop.run_until_complete(main())
