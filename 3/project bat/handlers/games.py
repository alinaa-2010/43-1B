import asyncio
import random
from datetime import date

from aiogram import F, Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message

import stats

router = Router()

GAMES = {
    ""
}