from pyrogram import Client, filters

@Client.on_message(filters.command(["start"]))
async def start(client, message):
    await client.send_message(message.chat.id, "Hello there! I am heroku control bot")
        
    
