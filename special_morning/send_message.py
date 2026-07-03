import os
import asyncio
from telegram import Bot, Update


async def main():

    BOT_TOKEN = os.getenv("BOT_TOKEN")
    M_CHAT_ID = os.getenv("M_CHAT_ID")

    if not BOT_TOKEN or not M_CHAT_ID:
        raise ValueError("BOT_TOKEN or M_CHAT_ID is not found")
        return
    try:
        bot = Bot(token=BOT_TOKEN)
        message = "سلام عزیزم صبحت بخیر ♥️☀️"
        await bot.send_message(chat_id=CHAT_ID, text=message)
    except Exception as e:
        print(f"❌ Error sending morning message: {e}")

if __name__ == "__main__":
    asyncio.run(main())