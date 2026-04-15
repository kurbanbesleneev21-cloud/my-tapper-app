import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# 1. ЗАМЕНИ ЭТОТ ТОКЕН (получи новый в @BotFather, старый удали!)
TOKEN = 'ТВОЙ_НОВЫЙ_ТОКЕН'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Ссылка на твое лого (можно загрузить в GitHub и скопировать ссылку)
    photo_url = "https://raw.githubusercontent.com/ТВОЙ_ЛОГИН/ТВОЙ_РЕПО/main/logo.png"
    
    # Текст как в Boinkers
    caption = (
        "**HASKOIN** · Киберпанк Тапалка 🚀\n"
        "▬▬▬▬▬▬▬▬▬▬▬▬\n"
        "Добро пожаловать в мир будущего! \n\n"
        "💰 **Майни HASK** простым тапом\n"
        "🚀 **Прокачивай** силу клика и энергию\n"
        "💎 **Выводи TON** прямо на кошелек\n"
        "▬▬▬▬▬▬▬▬▬▬▬▬\n"
        "Нажми кнопку ниже, чтобы начать путь легенды! 👇"
    )

    # Кнопки под сообщением
    keyboard = [
        [
            InlineKeyboardButton(
                text="🕹 ИГРАТЬ В HASKOIN", 
                web_app=WebAppInfo(url="https://ТВОЙ_ПРОЕКТ.vercel.app") # Твоя ссылка на игру
            )
        ],
        [
            InlineKeyboardButton(text="💬 Канал", url="https://t.me/твой_канал"),
            InlineKeyboardButton(text="🤝 Поддержка", url="https://t.me/твой_аккаунт")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_photo(
        photo=photo_url,
        caption=caption,
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Бот запущен...")
    app.run_polling()
