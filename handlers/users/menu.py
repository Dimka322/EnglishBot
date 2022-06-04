from aiogram import types
from aiogram.dispatcher.filters import Command
from keyboards.default.menu import menu
from loader import dp


@dp.message_handler(Command('menu'))
async def show_menu(message: types.Message):
    await message.answer('Выберите действие', reply_markup=menu)


@dp.message_handler(text='Изучение слов')
async def learn_words(message: types.Message):
    await message.answer("Вы выбрали изучение слов")
