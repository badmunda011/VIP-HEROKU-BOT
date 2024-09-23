from pyrogram import Client, filters

@Client.on_message(filters.command(["start"]))
async def start(client, message):
    await client.send_message(chat_id=message.chat.id, "Hello there!\n\n I am heroku control bot")
        
    
