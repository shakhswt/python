import asyncio
import logging
from aiogram.types import ContentType
from config import kanal_id, bot_token
from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from button import kb, kb2, kb3, loc
from product import FindProduct, PRODUCTS, tolovStates
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters.state import StateFilter

admin = 8316828703

storage = MemoryStorage()
dp = Dispatcher(storage=storage)

bot = Bot(token=bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
logging.basicConfig(level=logging.INFO)


amal_tolov = {}


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        text=(
            "Assalomu alaykum ANOR Marketga xush kelibsiz\n"
            "Kanalimizdan maxsulotlarni ID sini topishingiz mumkin🔴🔴🔴\n\n"
            "👉 https://t.me/anor_market_com"
        ),
        reply_markup=kb,
    )


@dp.message(F.text == "Admin💻")
async def admin_info(message: Message):
    await message.answer(text="Admin yaxshi bola 💻\n👉@shakh_swt1")


@dp.message(F.text == "Maxsulotlar kanali 🛒")
async def kanal(message: Message):
    await message.answer(
        text="""Yaxshi maxsulot topa olasiz\n"Maxsulotni IDsi orqali topish 🆔" ushbu tugmani bosgandan keyin IDni botga yuborishingiz mumkin\n👉 https://t.me/anor_market_com"""
    )


@dp.message(F.text == "Maxsulotni ID orqali topish 🆔")
async def id(message: Message, state: FSMContext):
    await state.set_state(FindProduct.mahsulotlar)
    await message.answer("Maxsulot IDsini yuboring")


@dp.message(FindProduct.mahsulotlar)
async def get_id(message: Message, state: FSMContext):
    msg_id = PRODUCTS.get(message.text)

    if msg_id:
        await bot.copy_message(
            chat_id=message.chat.id, from_chat_id=-1003451178147, message_id=msg_id
        )
        await message.answer("Sotib olishga aminmisiz", reply_markup=kb2)
    else:
        await message.answer("Bunday ID topilmadi\nQayta urinib ko'ring")

    await state.clear()


@dp.callback_query(F.data == "ha")
async def ha(call: CallbackQuery, state: FSMContext):
    await call.message.answer(
        "Iltimos, karta raqamiga to'lovni amalga oshirib, chek (skrinshot)ni shu yerga yuboring.\n\n5614 6841 0675 0548\nDavlatnazarov.Sh"
    )
    await state.set_state(tolovStates.tolov1)


@dp.message(StateFilter(tolovStates.tolov1), F.content_type == ContentType.PHOTO)
async def forward_screenshot(message: Message, state: FSMContext):

    fwd_msg = await message.forward(chat_id=admin)

    amal_tolov[fwd_msg.message_id] = message.from_user.id

    await bot.send_message(
        chat_id=admin,
        text="To'lovni tekshiring",
        reply_to_message_id=fwd_msg.message_id,
        reply_markup=kb3,
    )

    await message.answer("Skrinshot qabul qilindi\nAdmin javobini kuting")
    await state.clear()


@dp.callback_query(F.data == "ok")
async def payment_ok(call: CallbackQuery):
    reply_to = call.message.reply_to_message

    if reply_to and reply_to.message_id in amal_tolov:
        user_id = amal_tolov[reply_to.message_id]

        await call.message.answer(
            "To'lov tasdiqlandi ✅\nFoydalanuvchiga xabar yuborildi"
        )

        await bot.send_message(
            chat_id=user_id,
            text="To'lovingiz tasdiqlandi ✅\n\nIltimos, manzilingizni yuboring 📍",
            reply_markup=loc,
        )

    else:
        await call.message.answer("Xatolik: foydalanuvchi topilmadi.")


@dp.callback_query(F.data == "not")
async def payment_reject(call: CallbackQuery):
    reply_to = call.message.reply_to_message

    if reply_to and reply_to.message_id in amal_tolov:
        user_id = amal_tolov[reply_to.message_id]

        await call.message.answer(
            "To'lov rad etildi ❌\nFoydalanuvchiga xabar yuborildi"
        )

        await bot.send_message(
            chat_id=user_id,
            text="To'lov rad etildi ❌\n\nIltimos, qayta to'lov qiling yoki admin bilan bog'laning: @shakh_swt1",
            reply_markup=kb,
        )

        del amal_tolov[reply_to.message_id]

    else:
        await call.message.answer("Xatolik: foydalanuvchi topilmadi.")


@dp.message(F.content_type == ContentType.LOCATION)
async def locatsiya(message: Message, state: FSMContext):

    await message.forward(chat_id=admin)

    await message.answer(
        "Lokatsiya qabul qilindi ✅\n\nBuyurtmangiz 3 kun ichida BEPUL yetkazib beriladi",
        reply_markup=kb,
    )

    await state.clear()


@dp.callback_query(F.data == "yoq")
async def cancel_order(call: CallbackQuery):
    await call.message.answer(
        "Boshqa tovarlarimiz yoqadi degan umiddamiz", reply_markup=kb
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot to'xtatildi")
