from http.client import responses
from sqlite3 import IntegrityError

import sqlalchemy
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery
from aiogram import Bot, Router, F
import core.keyboards.inline as ikb
import core.keyboards.reply as rkb
from core.settings import settings
import requests


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message,):
    await message.answer("Привет! это бот Freenance!", reply_markup=rkb.main)


@router.message(F.text == "🪄проверить backend🪄")
async def check_back(message: Message):
    response = requests.get('https://qa.freenance.store/api/v1/currency/')
    if response.status_code == 200:
        await message.answer("backend работает корректно")
    else:
        # await message.answer("ендпоинт <a href='https://qa.freenance.store/api/v1/currency/'>currency</a> ответил ")
        await message.answer("backend не работает!")