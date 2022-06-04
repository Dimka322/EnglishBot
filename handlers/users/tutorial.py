from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from loader import dp, db


@dp.message_handler(Command('tutorial'))
async def show_tutor(message:types.Message):
    await message.answer('Для того, чтобы успешно пользоваться ботом нужно знать всего лишь одну последовательность.'
                         '1. После ввода команды /start, введите команду /quantity.'
                         '2. Команда /quantity позволит вам задать количество слов'
                         '3. После /quantity следует ввести /learn_words для изучения нужного количества слов'
                         '4. После /learn_words можно пройти тест /word_test')