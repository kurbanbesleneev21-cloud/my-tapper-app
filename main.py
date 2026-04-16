import asyncio
import sqlite3
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from database import init_db

# Настройка логирования, чтобы видеть ошибки в консоли
logging.basicConfig(level=logging.INFO)

# Твой токен
API_TOKEN = '8777742433:AAE9WxsbpYbxR1q3ZRj02l49DTZn0EIDK1k'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Инициализируем базу данных при запуске бота
init_db()

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username or "User"
    
    # Пытаемся достать ID реферера из команды /start (например, /start 1234567)
    args = message.text.split()
    referrer_id = None
    if len(args) > 1 and args[1].isdigit():
        referrer_id = int(args[1])

    # Подключаемся к базе
    conn = sqlite3.connect('husky_game.db')
    cursor = conn.cursor()

    # 1. Проверяем, есть ли такой пользователь уже в базе
    cursor.execute("SELECT user_id FROM users WHERE user_id = ?", (user_id,))
    user_in_db = cursor.fetchone()

    if user_in_db:
        # Если пользователь уже есть — просто приветствуем
        await message.answer(f"Привет, {username}! С возвращением в Husky Coin.")
    else:
        # 2. Если пользователя нет, регистрируем его
        # Проверяем, не является ли он рефералом и не пригласил ли сам себя
        if referrer_id and referrer_id != user_id:
            # Даем бонус пригласившему
            cursor.execute("UPDATE users SET balance = balance + 5000 WHERE user_id = ?", (referrer_id,))
            # Добавляем нового пользователя с пометкой пригласившего
            cursor.execute("INSERT INTO users (user_id, referrer_id, balance) VALUES (?, ?, ?)", (user_id, referrer_id, 1000))
            await message.answer(f"Добро пожаловать! Ты зашел по приглашению и получил 1000 монет!")
            
            # (Опционально) Можно отправить сообщение пригласившему, что у него новый реферал
            try:
                await bot.send_message(referrer_id, f"Ура! По твоей ссылке зашел новый игрок. Тебе начислено 5000 монет!")
            except:
                pass 
        else:
            # Обычный вход без рефералки
            cursor.execute("INSERT INTO users (user_id, balance) VALUES (?, ?)", (user_id, 0))
            await message.answer(f"Добро пожаловать в Husky Coin, {username}!")

    conn.commit()
    conn.close()

async def main():
    print("Бот запущен и готов к работе...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")
