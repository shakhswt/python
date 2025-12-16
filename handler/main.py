from aiogram.types import Message
from aiogram import F, Router
from aiogram.filters import CommandStart
from buttons.inlineb.button import menu

router = Router()


@router.message(CommandStart())
async def startup(message: Message):
    await message.answer("Salom bro", reply_markup=menu)
