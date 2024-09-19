import asyncio

from aiogram import Bot, Dispatcher
import logging

from aiogram.client.default import DefaultBotProperties

from core.database.models import async_main
from core.settings import settings
from core.handlers.all import router


async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] -  %(name)s - "
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
    bot = Bot(token=settings.bot.bot_token, default=DefaultBotProperties(parse_mode='HTML'))

    dp = Dispatcher()

    dp.include_router(router)

    await async_main()
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())