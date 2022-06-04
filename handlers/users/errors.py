from aiogram.dispatcher.filters import Command
from loader import dp, db
from aiogram import types


@dp.message_handler(Command("show_rus_test_errors"), state='learning')
async def show_rus_test_errors(message: types.Message):
    user_id = message.from_user.id
    errors = await db.get_rus_test_error(user_id)
    if len(errors) > 0:
        errors = errors.split(",")
        errors = "\n".join(errors)
    await message.answer(errors + '\nПродолжить изучение слов: \n/learn_words')


@dp.message_handler(Command("show_eng_test_errors"), state='learning')
async def show_eng_test_errors(message: types.Message):
    user_id = message.from_user.id
    errors = await db.get_eng_test_error(user_id)
    if len(errors) > 0:
        errors = errors.split(",")
        errors = "\n".join(errors)
    await message.answer(errors + '\nПродолжить изучение слов: \n/learn_words', )


@dp.message_handler(Command("show_def_test_errors"), state='learning')
async def show_def_test_errors(message: types.Message):
    user_id = message.from_user.id
    errors = await db.get_def_test_error(user_id)
    if len(errors) > 0:
        errors = errors.split(",")
        errors = "\n".join(errors)
    await message.answer(errors + '\nПродолжить изучение слов: \n/learn_words')


@dp.message_handler(Command("show_sen_test_errors"), state='learning')
async def show_def_test_errors(message: types.Message):
    user_id = message.from_user.id
    errors = await db.get_sen_test_errors(user_id)
    if len(errors) > 0:
        errors = errors.split(",")
        errors = "\n".join(errors)
    await message.answer(errors + '\nПродолжить изучение слов: \n/learn_words')
