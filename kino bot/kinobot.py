import asyncio
import logging
from config import bot_token, kanal_id
from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from inlineb import menu, menu1

link = "https://t.me/kinolar007_uz"
dp = Dispatcher()
bot = Bot(token=bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
logging.basicConfig(level=logging.INFO)


@dp.message(CommandStart())
async def start(message: Message):
    user_status = await bot.get_chat_member(kanal_id, message.from_user.id)
    if user_status.status == "left":
        await message.answer(
            "Assalomu alaykum siz kanalga obuna boling", reply_markup=menu
        )
    else:
        await message.answer("Botga hush kelibsiz", reply_markup=menu1)


@dp.callback_query(F.data == "kod")
async def kod(callback: CallbackQuery):
    await callback.message.answer("Kodni yuboring")
    await callback.answer()


@dp.message()
async def kod1(message: Message):

    a = message.text
    if a == "1":
        await message.answer_video(
            video="https://t.me/multfilmlar_olamiga_sayohatt/219",
            caption="""🖥 Yaxshi bo'lish osonmi 
🔄 QISIM 3
🇺🇿  O'zbek Tilida
⚔️ ➺ Komediya, Oilaviy 
🎦  Formati: 720p/HD
🎬 ➺  (2018)""",
        )
    else:
        print("Mavjud bolmagan kino ")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:

        asyncio.run(main())
    except Exception as err:
        print(err)
