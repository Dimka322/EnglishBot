from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

test_chooser = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Тестирование по переводу слов'),
        ],
        [
            KeyboardButton(text='Тестирование по оригиналу слов'),
        ],
        [
            KeyboardButton(text='Тестирование по значению слов'),
        ],
        [
            KeyboardButton(text='Тестирование по предложениям'),
        ],
        [
            KeyboardButton(text='Переход к следующим словам')
        ],
    ],
    resize_keyboard=True
)