from aiogram.filters import Filter
from config import kanal_id
from aiogram import Bot
from aiogram.types import Message


class CheckUp(Filter):
    async def __call__(self, message:Message,bot:Bot):
        user_status= await bot.get_chat_member(kanal_id, message.from_user.id)
        if user_status.status in ['creator','member','administrator']:
            return 1
        return 0