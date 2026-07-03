import os
import asyncio
from dotenv import load_dotenv
from telegram import Bot, Update
from apscheduler.schedulers.asyncio import AsyncIOScheduler

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is not found")
if not CHAT_ID:
    raise ValueError("CHAT_ID is not found")

bot = Bot(token=BOT_TOKEN)

async def send_good_morning():
    try:
        message = "Good morning! ☀️ Have a wonderful and productive day!"
        await bot.send_message(chat_id=CHAT_ID, text=message)
        print(f"Sent message to chat ID {CHAT_ID}: {message}")
    except Exception as e:
        print(f"❌ Error sending morning message: {e}")

async def send_good_night():
    try:
        message = "Good night! 🌙 Sleep tight and have sweet dreams!"
        await bot.send_message(chat_id=CHAT_ID, text=message)
        print("🌙 Good night message sent successfully!")
    except Exception as e:
        print(f"❌ Error sending night message: {e}")

async def main():
    try:
        me = await bot.get_me()
        print(f"🤖 Bot @{me.username} is successfully connected and running...")
    except Exception as e:
        print(f"❌ Connection to Telegram failed: {e}")
        return

    scheduler = AsyncIOScheduler(timezone="Asia/Tehran")


    scheduler.add_job(send_good_morning, 'cron', hour=5, minute=0)

    scheduler.add_job(send_good_night, 'cron', hour=22, minute=0)
    
    scheduler.start()
    
    print("📅 Scheduler initialized and active:")
    print("   - Morning message scheduled for 05:00 AM (Asia/Tehran)")
    print("   - Night message scheduled for 10:00 PM (Asia/Tehran)")
    print("💡 Keep this terminal open to let the bot send messages on time.\n")

    try:
        while True:
            await asyncio.sleep(3600)  
    except (KeyboardInterrupt, SystemExit):
        print("\n👋 Bot stopped by user.")

if __name__ == "__main__":
    asyncio.run(main())