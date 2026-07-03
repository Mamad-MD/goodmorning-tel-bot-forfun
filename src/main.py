import os
from dotenv import load_dotenv
from telegram import Bot, Update

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is not found")
if not CHAT_ID:
    raise ValueError("CHAT_ID is not found")

bot = Bot(token=BOT_TOKEN)

def send_good_morning_message():
    message = "Good morning! ☀️"
    bot.send_message(chat_id=CHAT_ID, text=message)
    print(f"Sent message to chat ID {CHAT_ID}: {message}")

if __name__ == "__main__":
    send_good_morning_message()