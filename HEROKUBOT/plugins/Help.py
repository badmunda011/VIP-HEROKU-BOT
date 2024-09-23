from pyrogram import filters
from pyrogram import Client as VIP
@VIP.on_message(filters.command(["start"]))
async def start(client, message):
    await message.reply_text(f"Hello there! I am heroku control bot\n\nHosting Commands: /host\nDelete hosting: /deletehost\n\nCheck hosted apps: /myhost, /heroku.")
        
    
