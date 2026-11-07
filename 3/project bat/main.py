# API - Application Programming Interface - Программный интерфейс приложения. Это набор правил и инструментов,
# которые позволяют различным программным приложениям взаимодействовать друг с другом.
# Telegram Bot API позволяет управлять ботом через код. 

# Handler - Обработчик.
# Например, пользователь отправил /start - сработает нужный обработчик и бот ответит.

# Router - Маршрутизатор. 
# Группирует обработчики.
# Например, один Router отвезает за команды, другой - за меню, третий за работу с профилем.

# Filter - Фильтр.
# Проверяет условие перед запуском обработчика.
# Например, проверяет, что пользователь отправил команду /start или Привет.

# Update - Обновление.
# Событие, полученное ботом от Telegram.
# Это может быть сообщение, нажатие кнопки, изменение чата и т.д.

# Message - Сообщение.
# Объект сообщения пользователя..
# Содержит текст, информацию о пользователе, чате и т.д.

# Command - Команда.
# Специальное сообщение, которое начинается с символа /.
# Примеры: /start, /help, /admin.

# Dispatcher                  - Главный диспетчер, который приниимает обновления и организует их обработку.
# F / Magic Filter            - удобный способ проверять значения и свойства событий.
# CommandStart                - фильтр команды /start.
# Command("help")             - фильтр команды /help.
# F.text                      - Обращение к тексту сообщения через Magic Filter.
# F.text == "Привет"          - проверка, что текст сообщения равен "Привет".
# @router.message()           - Регистрация обработчика событий
# @router.callback_query()    - Регистрация обработчика нажатий inline-кнопок
# async def                   - Объявление асинхронной функции
# await                       - Ожидание результата асинхронной операции
# include_router()            - Подключение Router к Dispatcher или другому Route

# Project Bot — папка проекта
# config.py — настройки бота
# custom_filters.py — собственные фильтры
# main.py — запуск бота
# stats.py — статистика
# handlers — обработчики сообщений
# __init__.py — инициализация пакета
# admin.py — команды администратора
# common.py — основные команды
# fallback.py — обработка остальных сообщений
# games.py — игровые команды
# reactions.py — реакции на сообщения

import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import BotCommand

import config
from handlers import admin, common, fallback, games, reactions

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=config.TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    dp.include_routers(*routers: common.router, admin.router, games.router, reactions.router, fallback.router)
    
    await bot.set_my_commands([
        BotCommand(command="slots", description="🎰 Автомат"),
        BotCommand(command="dice", description="🎲 Кубик"),
        BotCommand(command="darts", description="🎯 Дартс"),
        BotCommand(command="basketball", description="🏀 Баскетбол"),
        BotCommand(command="football", description="⚽ Футбол"),
        BotCommand(command="bowling", description="🎳 Боулинг"),
        BotCommand(command="luck", description="🍀 Удача на сегодня"),
        BotCommand(command="help", description="Что умеет бот"),
    ])
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
    finally:
        print("\n 👋 Лавочка закрыта. Приходи Завтра.")