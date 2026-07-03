# Good Morning Telegram Bot (Python)

A small, **for-fun learning project** to get familiar with:
- Telegram bot basics (Bot API)
- Python project structure
- Using environment variables (`.env`)
- Scheduling a daily message (optional)

This bot sends a simple “Good Morning” message to a specific chat.

---

## Tech Stack
- Python 3.10+
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- python-dotenv

---

## Project Structure
.
├─ src/
│ └─ main.py
├─ .env.example
├─ .gitignore
├─ requirements.txt
└─ README.md

---

## Setup

### 
1) Create a virtual environment
Windows (PowerShell):
```powershell
python -m venv .venv
.venv\Scripts\activate

macOS/Linux:
python3 -m venv .venv
source .venv/bin/activate

2) Install dependencies

pip install -r requirements.txt

3) Configure environment variables

Create a .env file (do NOT commit it). Use .env.example as a template:
BOT_TOKEN=...
CHAT_ID=...

Getting CHAT_ID
Send a message to your bot in Telegram.
Open:
   https://api.telegram.org/bot<BOT_TOKEN>/getUpdates
   
Find:
   "chat": { "id": 123456789 }
   
Run
python src/main.py
Notes
This repository is intentionally minimal and educational.
Do not commit your real bot token or .env file.

---
