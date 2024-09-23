from pyrogram import Client, filters

@Client.on_message(filters.command(["start"]))
async def start(client, message):
    await message.reply_text("Hello there! I am heroku control bot")
        
    
