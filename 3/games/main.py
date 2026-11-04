
import asyncio
import os
import random

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

dp = Dispatcher()

games = [
    "🎮 The Witcher 3\nЖанр: RPG\nИнтересный сюжет, открытый мир и монстры.",
    
    "👻 Resident Evil 4\nЖанр: Horror, Action\nЗомби, загадки и выживание.",

    "🌻 Stardew Valley\nЖанр: Симулятор\nФерма, рыбалка и уютная атмосфера.",

    "🚇 Metro Exodus\nЖанр: Survival, Shooter\nПостапокалиптический мир и захватывающая история.",

    "🤖 Detroit: Become Human\nЖанр: Interactive Movie\nТвои решения влияют на сюжет."
]


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Привет! 🎮\n"
        "Я GameBot — бот, который поможет найти интересную игру!\n\n"
        "Напиши /games, чтобы получить рекомендацию."
    )


@dp.message(Command("help"))
async def help(message: Message):
    await message.answer(
        "📌 Доступные команды:\n\n"
        "/start — запуск бота\n"
        "/help — список команд\n"
        "/games — случайная рекомендация игры"
    )


@dp.message(Command("games"))
async def recommend_game(message: Message):
    game = random.choice(games)
    await message.answer(
        "🍿 Вот игра, которую я тебе рекомендую:\n\n" + game
    )


async def main():
    bot = Bot(token=os.getenv("BOT_TOKEN"))
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
