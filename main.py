from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

# ... внутри функции start_handler ...

# Создаем кнопку, которая открывает Mini App
# Вместо 'https://твой-сайт.com' вставь ссылку на свою игру (например, с GitHub Pages)
kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(
        text="Начать играть 
.      ", 
        web_app=WebAppInfo(url="https://kurbanbesleneev21-cloud.github.io/my-tapper-app/")
    )]
])

if existing_user:
    await message.answer(f"С возвращением, {username}!", reply_markup=kb)
else:
    # ... логика начисления бонуса ...
    await message.answer(f"Добро пожаловать в Husky Coin!", reply_markup=kb)
