import os
import asyncio
from datetime import datetime
import pytz
from dotenv import load_dotenv
from telegram import Bot, Update
#from apscheduler.schedulers.asyncio import AsyncIOScheduler

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
        message = "☀️ صبح بخیر محمد عزیز! خورشید دوباره طلوع کرده تا بهت یادآوری کنه که امروز فرصت‌های جدیدی برای ساختن و یادگیری داری. امیدوارم روزی پر از انرژی، کد زدن‌های موفق و پیشرفت در پروژه‌هات داشته باشی. موفق باشی! 🚀"
        await bot.send_message(chat_id=CHAT_ID, text=message)
        print(f"Sent message to chat ID {CHAT_ID}: {message}")
    except Exception as e:
        print(f"❌ Error sending morning message: {e}")

async def send_good_night():
    try:
        message = "🌙 شب بخیر، زمان استراحت! یک روز دیگه هم گذشت و کلی تجربه به دانش برنامه‌نویسی‌ت اضافه شد. یادت باشه که استراحت کافی، سوخت مغز برای الگوریتم‌های پیچیده فرداست. آرامش مهمون لحظه‌هات باشه. شب آرومی داشته باشی. ✨"
        await bot.send_message(chat_id=CHAT_ID, text=message)
        print("🌙 Good night message sent successfully!")
    except Exception as e:
        print(f"❌ Error sending night message: {e}")

async def main():
#    try:
#       me = await bot.get_me()
#       print(f"🤖 Bot @{me.username} is successfully connected and running...")
#   except Exception as e:
#       print(f"❌ Connection to Telegram failed: {e}")
#        return

#    scheduler = AsyncIOScheduler(timezone="Asia/Tehran")


#    scheduler.add_job(send_good_morning, 'cron', hour=5, minute=0)
#    scheduler.add_job(send_good_night, 'cron', hour=22, minute=0)
    
 #   scheduler.start()
    
  #  print("📅 Scheduler initialized and active:")
   # print("   - Morning message scheduled for 05:00 AM (Asia/Tehran)")
    #print("   - Night message scheduled for 10:00 PM (Asia/Tehran)")
#    print("💡 Keep this terminal open to let the bot send messages on time.\n")

#    try:
#        while True:
#            await asyncio.sleep(3600)  
#    except (KeyboardInterrupt, SystemExit):
#        print("\n👋 Bot stopped by user.")

    iran_tz = pytz.timezone("Asia/Tehran")
    now_iran = datetime.now(iran_tz)
    current_hour = now_iran.hour

    print(f"Current time in Tehran: {now_iran.strftime('%Y-%m-%d %H:%M:%S')}")

    if 5 <= current_hour < 10:
        await send_good_morning()
    elif 21 <= current_hour <= 23:
        await send_good_night()
    else:
        # Fallback for manual trigger (workflow_dispatch) at other times
        print("Manual execution triggered outside standard schedule. Sending both as a test.")
        await send_good_morning()
        await send_good_night()



if __name__ == "__main__":
    asyncio.run(main())