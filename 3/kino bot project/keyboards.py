from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from .texts import HYPE_TEXT

GENRES = ["😂 Комедия", "🧨 Боевик", "😱 Ужасы", "🚀 Фантастика", "🎭 Драма", "🧸 Мульт"]
PAGE_SIZE = 5

BTN_ADD = "➕ Добавить фильм"
BTN_LIST = "📋 Мои фильмы"
BTN_RANDOM = "🎲 Что смотреть?"

class OpenFilm(CallbackData, prefix="film"):
    id:         int
    page:       int

class Page(CallbackData, prefix="page"):
    n:          int   

class Act(CallbackData, prefix="act"):
    action:     str
    id:         int
    page:       int = 0
    v:          int = 0

class GenrePick(CallbackData, prefix="genre"):
    i:          int

class HypePick(CallbackData, prefix="hype"):
    v:          int

def main_menu():
    builder = ReplyKeyboardBuilder()
    builder.button(text=BTN_ADD)
    builder.button(text=BTN_LIST)
    builder.button(text=BTN_RANDOM)
    builder.adjust(1, 2)
    return builder.as_markup(resize_keyboard=True, input_field_placeholder="Выберите в меню👇")

def films_kb(films):
    builder = InLIneKeyboardBuilder()
    for i in films:
        icon = "✅" if i["watched"] else "🍿"
        builder.button(text=f"{icon} {i['title']}", callback_data=OpenFilm(id=i["id"], page=0).pack())

    
        