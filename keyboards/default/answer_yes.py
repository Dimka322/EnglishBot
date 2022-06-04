from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

answer_yes = ReplyKeyboardMarkup(
    keyboard=
    [
        [
            KeyboardButton(text="Да")
        ],
    ],
    resize_keyboard=True
)