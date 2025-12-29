from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    KeyboardButton,
    WebAppInfo,
)

kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Maxsulotni ID orqali topish 🆔"),
            KeyboardButton(text="Admin💻"),
        ],
        [
            KeyboardButton(text="Maxsulotlar kanali 🛒"),
            KeyboardButton(
                text="Bot nima orqali yaratildi",
                web_app=WebAppInfo(url="https://code.visualstudio.com/"),
            ),
        ],
    ],
    resize_keyboard=True,
)


kb2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅", callback_data="ha"),
            InlineKeyboardButton(text="❌", callback_data="yoq"),
        ],
    ]
)


kb3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅", callback_data="ok"),
            InlineKeyboardButton(text="❌", callback_data="not"),
        ],
    ]
)

loc = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Joriy lokatsiyani yuborish📍", request_location=True)]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
