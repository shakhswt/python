from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Menu", callback_data="menu"),
            InlineKeyboardButton(text="Admin", callback_data="admin"),
        ],
        [InlineKeyboardButton(text="Poddershka", callback_data='poddershka')]
    ]
)
