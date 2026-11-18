
import asyncio
import os

from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()
router = Router()

# Клавиатура
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="⭐ Топ фильмов")],
        [KeyboardButton(text="ℹ️ Помощь")]
    ],
    resize_keyboard=True
)


# /start
@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Привет! 🎬 Я Кино-бот!\n"
        "Помогу выбрать фильм для просмотра.\n"
        "Используй кнопки или команды!",
        reply_markup=keyboard
    )


# /help и кнопка помощи
@router.message(Command("help"))
@router.message(F.text == "ℹ️ Помощь")
async def help(message: Message):
    await message.answer(
        "📌 Доступные команды:\n"
        "/start - начало работы\n"
        "/help - помощь\n"
        "/top - популярные фильмы"
    )


# /top и кнопка топа
@router.message(Command("top"))
@router.message(F.text == "⭐ Топ фильмов")
async def top(message: Message):
    await message.answer(
        "⭐ Популярные фильмы:\n\n"
        "1. Интерстеллар\n"
        "2. Начало\n"
        "3. Побег из Шоушенка\n"
        "4. Зеленая миля\n"
        "5. Форрест Гамп"
    )


# Приветствие
@router.message(F.text.lower() == "привет")
async def hello(message: Message):
    await message.answer("Привет! 👋 Рад тебя видеть.")


# Спасибо
@router.message(F.text.lower() == "спасибо")
async def thanks(message: Message):
    await message.answer("Всегда пожалуйста. 😊")


# Ловец всего остального
@router.message()
async def other(message: Message):
    await message.answer(
        "🤔 Кажется, я не совсем понял тебя.\n"
        "Попробуй /help"
    )


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
