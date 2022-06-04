from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text='Изучение слов'),
    ],
    ],
    resize_keyboard=True
)