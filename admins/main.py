from aiogram.types import Message
from aiogram import F, Router
from aiogram.filters import CommandStart
from buttons.inlineb.button import menu
from config.config import admins

admin_router = Router()



@admin_router.message(CommandStart(), F.from_user.id == 8316828703)
async def startup(message: Message):
    await message.answer("Salom bro siz adminsiz", reply_markup=menu)
