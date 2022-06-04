from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp, db
from aiogram import types
from states import User_States



@dp.message_handler(Command("change_quantity"), state='main')
async def get_quantity(message: types.Message):
    await message.answer('Введите количество слов для изучения (пожалуйста, используйте цифры)')

    await User_States.Quantity.set()


@dp.message_handler(state=User_States.Quantity)
async def answer_1(message: types.Message, state: FSMContext):
    answer = message.text
    await db.add_quantity(quantity=int(answer), id=message.from_user.id)
    await db.add_const_quantity(const_quantity=int(answer), id=message.from_user.id)
    await message.answer(f'Вы выбрали изучать {answer} слов в день, введите команду /learn_words для изучения слов.')
    await state.update_data(answer1=answer)
    await db.set_user_state(current_state='main', id=message.from_user.id)
    await state.set_state("main")
