# ☀️ Good Morning Telegram Bot

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

یک پروژه آموزشی و تفننی برای آشنایی با اکوسیستم بات‌های تلگرام و مدیریت پروژه‌های پایتونی. این بات به صورت خودکار هر روز صبح ساعت **۰۵:۰۰** یک پیام انرژی‌بخش ارسال می‌کند.

---

## 🎯 اهداف پروژه (Learning Goals)
این پروژه با هدف یادگیری مفاهیم زیر پیاده‌سازی شده است:
- **Telegram Bot API:** کار با کتابخانه محبوب `python-telegram-bot`.
- **Environment Variables:** مدیریت داده‌های حساس (Token) با استفاده از `.env`.
- **Task Scheduling:** زمان‌بندی اجرای کدها با `APScheduler`.
- **Project Structuring:** رعایت ساختار استاندارد فایل‌بندی در پایتون.

---

## 🛠 ابزارها و تکنولوژی‌ها
- **Language:** Python 3.10+
- **Library:** `python-telegram-bot` (V20+)
- **Scheduler:** `APScheduler`
- **Config:** `python-dotenv`

---

## 🏗 ساختار پروژه
```text
.
├── src/
│   └── main.py          # کد اصلی بات و زمان‌بندی
├── .env.example         # نمونه متغیرهای محیطی
├── .gitignore           # فایل‌های نادیده گرفته شده توسط گیت
├── requirements.txt     # لیست پکیج‌های مورد نیاز
└── README.md            # راهنمای پروژه
