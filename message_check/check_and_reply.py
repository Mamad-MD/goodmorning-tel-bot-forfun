
import os
import asyncio
from telegram import Bot

async def main():
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    M_CHAT_ID = int(os.getenv("M_CHAT_ID", "2126576569"))
    CHAT_ID = int(os.getenv("CHAT_ID", "1657970895"))

    if not BOT_TOKEN or not CHAT_ID:
        print("❌ Missing BOT_TOKEN or CHAT_ID in environment variables!")
        return

    bot = Bot(token=BOT_TOKEN)

    try:
        updates = await bot.get_updates()
        if not updates:
            print("✉️ No new messages from M_CHAT_ID.")
            return
        last_update_id = 0
        
        for update in updates:
            last_update_id = update.update_id


            if update.message and update.message.chat_id == M_CHAT_ID:
                user_msg = update.message.text or "[non-text message]"
                alert_text = f"✉️ پیام جدید از طرف کاربر ویژه:\n\n{user_msg}"
                await bot.send_message(chat_id=CHAT_ID, text=alert_text)
                print(f"✅ Forwarded from special user: {user_msg}")
                
            elif update.message and update.message.chat_id == CHAT_ID:
                msg_text = update.message.text or ""                
                if msg_text.startswith("/r ") or msg_text.startswith("/reply "):
                    reply_content = msg_text.split(maxsplit=1)[1] if len(msg_text.split(maxsplit=1)) > 1 else ""

                    if reply_content:
                        await bot.send_message(chat_id=M_CHAT_ID, text=reply_content)
                        await bot.send_message(chat_id=CHAT_ID, text=f"✅  پیام شما ارسال شد:\n«{reply_content}»")
                        
                        print(f"✅ Replied to special user: {reply_content}")
                    else:
                        await bot.send_message(chat_id=CHAT_ID, text="⚠️ لطفاً متن پیام خود را بعد از دستور /r یا /reply وارد کنید.")
                        print("⚠️ Reply command received but no content provided.")


        if last_update_id > 0:
            await bot.get_updates(offset=last_update_id + 1)
            print(f"✅ Updated last processed update ID to {last_update_id}")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())