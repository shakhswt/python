from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Kanalga obuna bo'ling",
                url="https://t.me/kinolar007_uz"
            )
        ]
    ]
)


menu1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Film kodini yuboring",
                callback_data="kod"
            )
        ]
    ]
)