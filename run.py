from aiogram import Bot, Dispatcher, F
import asyncio
import logging
from config import TOKEN
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
import keyboards as kb
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    # await async_main()
    # dp.include_router(router=router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("выход")