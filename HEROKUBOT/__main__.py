from HEROKUBOT import app
import importlib

async def main():
    print("Starting Bot.....")
    await app.start()
    print("Bot Started.....")
    for file in os.listdir("HEROKUBOT.plugins")
        importlib.import_module(f"HEROKUBOT.plugins.{file}")
    await idle()
    await app.stop()


if __name__ == "__main__":
    loop = asyncio.get_event_loop_policy().get_event_loop()
    loop.run_until_complete(main())