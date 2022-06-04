from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

user_level = ReplyKeyboardMarkup(
    keyboard=
    [
        [
            KeyboardButton(text="B1"),
            KeyboardButton(text="B2-C1")
        ],

    ],
    resize_keyboard=True
)