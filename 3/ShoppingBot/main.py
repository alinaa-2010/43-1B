
import asyncio
import os

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from dotenv import load_dotenv

from database import add_user, add_product, get_products, delete_product

load_dotenv()

bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher()


keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="➕ Добавить товар")],
        [KeyboardButton(text="🛒 Мои товары")],
        [KeyboardButton(text="🗑 Удалить товар")]
    ],
    resize_keyboard=True
)


class Shopping(StatesGroup):
    name = State()
    quantity = State()
    delete = State()


@dp.message(Command("start"))
async def start(message: types.Message):
    add_user(message.from_user.id)

    await message.answer(
        "Привет. Это бот для списка покупок 🛒",
        reply_markup=keyboard
    )


@dp.message(F.text == "➕ Добавить товар")
async def add_start(message: types.Message, state: FSMContext):
    await state.set_state(Shopping.name)
    await message.answer("Введите название товара:")


@dp.message(Shopping.name)
async def product_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Shopping.quantity)
    await message.answer("Введите количество товара:")


@dp.message(Shopping.quantity)
async def product_quantity(message: types.Message, state: FSMContext):
    if not message.text.isdigit() or int(message.text) <= 0:
        await message.answer("Введите положительное число:")
        return

    data = await state.get_data()

    add_product(
        message.from_user.id,
        data["name"],
        int(message.text)
    )

    await state.clear()
    await message.answer("Товар успешно добавлен. ✅", reply_markup=keyboard)


@dp.message(F.text == "🛒 Мои товары")
async def my_products(message: types.Message):
    products = get_products(message.from_user.id)

    if not products:
        await message.answer("Ваш список покупок пуст.")
        return

    text = "🛒 Ваш список покупок:\n\n"

    for product in products:
        text += f"🆔 ID: {product[0]}\n"
        text += f"📦 Товар: {product[2]}\n"
        text += f"🔢 Количество: {product[3]}\n\n"

    await message.answer(text)


@dp.message(F.text == "🗑️ Удалить товар")
async def delete_start(message: types.Message, state: FSMContext):
    products = get_products(message.from_user.id)

    if not products:
        await message.answer("Список покупок пуст.")
        return

    text = "Выберите ID товара для удаления:\n\n"

    for product in products:
        text += f"ID: {product[0]} — {product[2]}\n"

    await state.set_state(Shopping.delete)
    await message.answer(text)


@dp.message(Shopping.delete)
async def delete(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Введите ID числом.")
        return

    delete_product(
        int(message.text),
        message.from_user.id
    )

    await state.clear()
    await message.answer("Операция выполнена.", reply_markup=keyboard)


# Запуск
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
