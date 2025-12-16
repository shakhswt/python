import asyncio
from aiogram import Bot, Dispatcher
from config.config import bot_token
import logging
from handler.main import router
from admins.main import admin_router

bot = Bot(token=bot_token)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)
dp.include_router(admin_router)
dp.include_router(router)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:

        asyncio.run(main())
    except Exception as err:
        print(err)
