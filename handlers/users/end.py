from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
import random
from loader import dp, db
from aiogram import types
from states import All_State


@dp.message_handler(text='Переход к следующим словам', state='learning')
async def go_further(message: types.Message, state: FSMContext):
    await state.set_state('main')
    await message.answer('Переходим к следующим словам\n'
                         'Используйте команду: /learn_words')
