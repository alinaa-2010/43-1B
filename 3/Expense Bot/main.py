
import asyncio
import os

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher()

expenses = []

categories = ["🍔 Еда", "🚕 Транспорт", "🎮 Развлечения", "🛍 Покупки", "📦 Другое"]

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="➕ Добавить расход")],
        [KeyboardButton(text="📋 Мои расходы")],
        [KeyboardButton(text="📂 Категории")],
        [KeyboardButton(text="🗑️ Удалить расход")],
        [KeyboardButton(text="💰 Общая сумма")]
    ],
    resize_keyboard=True
)


class Expense(StatesGroup):
    name = State()
    amount = State()
    category = State()
    date = State()
    delete = State()


# Старт
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "Привет. 💰\nЭто бот для учёта твоих расходов.",
        reply_markup=keyboard
    )


@dp.message(F.text == "➕ Добавить расход")
async def add_start(message: types.Message, state: FSMContext):
    await state.set_state(Expense.name)
    await message.answer("Введите название покупки:")


@dp.message(Expense.name)
async def expense_name(message: types.Message, state: FSMContext):
    if not message.text:
        await message.answer("Введите название текстом.")
        return

    await state.update_data(name=message.text)
    await state.set_state(Expense.amount)
    await message.answer("Введите сумму расхода:")


@dp.message(Expense.amount)
async def expense_amount(message: types.Message, state: FSMContext):
    try:
        amount = float(message.text.replace(",", "."))
        if amount <= 0:
            raise ValueError
    except (ValueError, AttributeError):
        await message.answer("Введите корректную сумму.")
        return

    await state.update_data(amount=amount)
    await state.set_state(Expense.category)

    category_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=category)]
            for category in categories
        ],
        resize_keyboard=True
    )

    await message.answer("Выберите категорию:", reply_markup=category_keyboard)


@dp.message(Expense.category)
async def expense_category(message: types.Message, state: FSMContext):
    if message.text not in categories:
        await message.answer("Выберите категорию кнопкой.")
        return

    await state.update_data(category=message.text)
    await state.set_state(Expense.date)

    await message.answer("Введите дату расхода (ДД.ММ.ГГГГ):")


@dp.message(Expense.date)
async def expense_date(message: types.Message, state: FSMContext):
    from datetime import datetime

    try:
        date = datetime.strptime(message.text, "%d.%m.%Y").strftime("%d.%m.%Y")
    except (ValueError, TypeError):
        await message.answer("Введите дату в формате ДД.ММ.ГГГГ!")
        return

    data = await state.get_data()

    expense = {
        "id": len(expenses) + 1,
        "user_id": message.from_user.id,
        "name": data["name"],
        "amount": data["amount"],
        "category": data["category"],
        "date": date
    }

    expenses.append(expense)

    await state.clear()
    await message.answer(
        "Расход успешно добавлен. ✅",
        reply_markup=keyboard
    )


# Показать все расходы
@dp.message(F.text == "📋 Мои расходы")
async def show_expenses(message: types.Message):
    user_expenses = [
        expense for expense in expenses
        if expense["user_id"] == message.from_user.id
    ]

    if not user_expenses:
        await message.answer("У тебя пока нет расходов.")
        return

    text = "📋 Твои расходы:\n\n"

    for expense in user_expenses:
        text += (
            f"🆔 ID: {expense['id']}\n"
            f"📦 Покупка: {expense['name']}\n"
            f"💰 Сумма: {expense['amount']}\n"
            f"📂 Категория: {expense['category']}\n"
            f"📅 Дата: {expense['date']}\n\n"
        )

    await message.answer(text)


# Категории
@dp.message(F.text == "📂 Категории")
async def show_categories(message: types.Message):
    category_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=category)]
            for category in categories
        ],
        resize_keyboard=True
    )

    await message.answer(
        "Выбери категорию:",
        reply_markup=category_keyboard
    )


@dp.message(F.text.in_(categories))
async def category_expenses(message: types.Message):
    user_expenses = [
        expense for expense in expenses
        if expense["user_id"] == message.from_user.id
        and expense["category"] == message.text
    ]

    if not user_expenses:
        await message.answer("В этой категории пока нет расходов.")
        return

    text = f"📂 Расходы: {message.text}\n\n"

    for expense in user_expenses:
        text += (
            f"🆔 ID: {expense['id']}\n"
            f"📦 {expense['name']}\n"
            f"💰 {expense['amount']}\n"
            f"📅 {expense['date']}\n\n"
        )

    await message.answer(text)


# Удаление расхода
@dp.message(F.text == "🗑️ Удалить расход")
async def delete_start(message: types.Message, state: FSMContext):
    user_expenses = [
        expense for expense in expenses
        if expense["user_id"] == message.from_user.id
    ]

    if not user_expenses:
        await message.answer("Нет расходов для удаления.")
        return

    text = "Выбери ID расхода для удаления:\n\n"

    for expense in user_expenses:
        text += f"ID: {expense['id']} — {expense['name']} ({expense['amount']})\n"

    await state.set_state(Expense.delete)
    await message.answer(text)


@dp.message(Expense.delete)
async def delete_expense(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Введите ID числом.")
        return

    expense_id = int(message.text)

    for expense in expenses:
        if expense["id"] == expense_id and expense["user_id"] == message.from_user.id:
            expenses.remove(expense)
            await state.clear()
            await message.answer("Расход удалён. ✅", reply_markup=keyboard)
            return

    await message.answer("Расход с таким ID не найден.")


# Общая сумма
@dp.message(F.text == "💰 Общая сумма")
async def total_expenses(message: types.Message):
    user_expenses = [
        expense for expense in expenses
        if expense["user_id"] == message.from_user.id
    ]

    total = sum(expense["amount"] for expense in user_expenses)

    await message.answer(
        f"💰 Общая сумма расходов: {total:.2f} сом"
    )


# Запуск
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
