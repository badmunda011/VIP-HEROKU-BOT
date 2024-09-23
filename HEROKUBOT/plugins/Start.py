from pyrogram import Client, filters

@Client.on_message(filters.command(["start"]))
async def start(client, message):
    await message.reply_text(f"Hello there! I am heroku control bot\n\nHosting Commands: /host\nDelete hosting: /deletehost\n\nCheck hosted apps: /myhost, /heroku.")
        
    
