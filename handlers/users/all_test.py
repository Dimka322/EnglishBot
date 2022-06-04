from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
import random
from loader import dp, db
from aiogram import types
from states import All_State


@dp.message_handler(Command('all_word_test'), state='learning')
async def test_info(message: types.Message):
    user_id = message.from_user.id
    await message.answer('Вы выбрали прохождение теста. Вы готовы?')
    q = str(await db.get_all_words(user_id))
    b = q.split(',')
    del b[-1]
    await All_State.Start.set()


@dp.message_handler(state=All_State.Start)
async def test(message: types.Message):
    await All_State.Cur_Answer.set()
    user_id = message.from_user.id
    words = str(await db.get_all_words(user_id))
    if words is not None:
        temp = words.split(',')
        del temp[-1]
        question = temp.pop(0)
        i = 0
        await message.answer('Как называется это слово' + question)
        while i < 1:
            answer = message.text
            i += 1
        print(answer)
        if answer != question:
            await message.answer('Нет')
        NewString = ','.join(temp)
        await db.set_all_words(NewString, user_id)
        await All_State.Start.set()
    else:
        await message.answer('Пройдено')
