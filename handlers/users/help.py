from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from utils.misc import rate_limit


@rate_limit(5, 'help')
@dp.message_handler(CommandHelp(), state='*')
async def bot_help(message: types.Message):
    text = [
        'Список команд: ',
        '/start - Начать диалог',
        '/help - Получить справку',
        '/learn_words - Начать изучение слов',
        '/quantity - Установить количество слов',
        '/rus_test - Пройти тестирование по изученному лексикону'
    ]
    await message.answer('\n'.join(text))
