
import asyncio
import os
import random

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Привет. 🎲\n"
        "Я бот, который поможет тебе сделать выбор.\n\n"
        "Напиши два варианта через слово «или».\n"
        "Например: пицца или суши?\n\n"
    )


@dp.message(Command("help"))
async def help(message: Message):
    await message.answer(
        "📌 Мои команды:\n\n"
        "/start — запуск бота\n"
        "/help — помощь\n"
        "/choose — как пользоваться ботом\n"
        "/random — случайный выбор"
    )


@dp.message(Command("choose"))
async def choose(message: Message):
    await message.answer(
        "Напиши два варианта через слово «или».\n"
        "Например: пицца или суши?\n\n"
    )


@dp.message(Command("random"))
async def random_choice(message: Message):
    result = random.choice(["Да!", "Нет!"])
    await message.answer(result)


@dp.message()
async def answer(message: Message):
    if not message.text:
        return

    text = message.text.lower()

    if "или" in text:
        options = text.split("или")

        if len(options) == 2 and options[0].strip() and options[1].strip():
            result = random.choice(options).strip()

            await message.answer(
                "🎲 Мой выбор: " + result
            )
        else:
            await message.answer("Напиши только два варианта!")

    else:
        await message.answer(
            "Напиши два варианта через слово «или»."
        )


async def main():
    bot = Bot(token=os.getenv("BOT_TOKEN"))
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
