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
import core.database.requests as rq
from core.settings import settings


router = Router()