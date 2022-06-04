from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove
from aiogram.utils.markdown import hbold
from loader import dp, db
from aiogram import types
from keyboards.default import test_chooser
from states import Test_State


@dp.message_handler(text='Тестирование по переводу слов', state='learning')
async def test_info(message: types.Message):
    await message.answer('Вы выбрали прохождение теста по переводу слов.', reply_markup=ReplyKeyboardRemove())
    user_id = message.from_user.id
    q = await db.get_questions(user_id)
    word = q[0]
    await message.answer(word + '\n Как пишется это слово по-английски?')
    await Test_State.Q1.set()


@dp.message_handler(state=Test_State.Q1)
async def answer_1(message: types.Message, state: FSMContext):
    answer = message.text.lower()
    user_id = message.from_user.id
    q1 = await db.get_questions(id=user_id)
    b = await db.select_word(translate=str(q1[0]))
    c = str(b).replace("<Record word='", '')
    word = c.replace("'>", '').replace('[', '').replace(']', '')
    result = await db.get_result(id=user_id)
    errors = str(await db.get_rus_test_error(user_id))
    if errors == 'None':
        errors = ''
    if answer == word:
        result += 1
        await message.answer('Правильно!')
    else:
        errors += word + ','
        await message.answer('Неправильно!')
    await db.set_rus_test_error(errors, user_id)
    await db.set_result(result, user_id)
    await state.update_data(answer1=answer)
    await message.answer(q1[1] + '\nКак пишется это слово по-английски?')
    await Test_State.next()


@dp.message_handler(state=Test_State.Q2)
async def answer_2(message: types.Message, state: FSMContext):
    answer = message.text.lower()
    user_id = message.from_user.id
    q2 = await db.get_questions(id=user_id)
    b = await db.select_word(translate=str(q2[1]).replace('[', '').replace(']', ''))
    c = str(b).replace("<Record word='", '')
    word = c.replace("'>", '').replace('[', '').replace(']', '')
    result = await db.get_result(id=user_id)
    errors = str(await db.get_rus_test_error(user_id))
    if errors == 'None':
        errors = ''
    if answer == word:
        result += 1
        await message.answer('Правильно!')
    else:
        errors += word + ','
        await message.answer('Неправильно!')
    await db.set_rus_test_error(errors, user_id)
    await db.set_result(result, user_id)
    await state.update_data(answer2=answer)
    await message.answer(q2[2] + '\nКак пишется это слово по-английски?')
    await Test_State.next()


@dp.message_handler(state=Test_State.Q3)
async def answer_3(message: types.Message, state: FSMContext):
    answer = message.text.lower()
    user_id = message.from_user.id
    q3 = await db.get_questions(id=user_id)
    b = await db.select_word(translate=str(q3[2]).replace('[', '').replace(']', ''))
    c = str(b).replace("<Record word='", '')
    word = c.replace("'>", '').replace('[', '').replace(']', '')
    result = await db.get_result(id=user_id)
    errors = await db.get_rus_test_error(user_id)
    if errors == 'None':
        errors = ''
    if answer == word:
        result += 1
        await message.answer('Правильно!')
    else:
        errors += word + ','
        await message.answer('Неправильно!')
    await db.set_rus_test_error(errors, user_id)
    await db.set_result(result, user_id)
    await state.update_data(answer3=answer)
    await message.answer(q3[3] + '\nКак пишется это слово по-английски?')
    await Test_State.next()


@dp.message_handler(state=Test_State.Q4)
async def answer_4(message: types.Message, state: FSMContext):
    answer = message.text.lower()
    user_id = message.from_user.id
    q4 = await db.get_questions(id=user_id)
    b = await db.select_word(translate=str(q4[3]).replace('[', '').replace(']', ''))
    c = str(b).replace("<Record word='", '')
    word = c.replace("'>", '').replace('[', '').replace(']', '')
    result = await db.get_result(id=user_id)
    errors = str(await db.get_rus_test_error(user_id))
    if errors == 'None':
        errors = ''
    if answer == word:
        result += 1
        await message.answer('Правильно!')
    else:
        errors += word + ','
        await message.answer('Неправильно!')
    await db.set_rus_test_error(errors, user_id)
    await db.set_result(result, user_id)
    await state.update_data(answer4=answer)
    await message.answer(q4[4] + '\nКак пишется это слово по-английски?')
    await Test_State.next()


@dp.message_handler(state=Test_State.Q5)
async def answer_5(message: types.Message, state: FSMContext):
    answer = message.text.lower()
    user_id = message.from_user.id
    q5 = await db.get_questions(id=user_id)
    b = await db.select_word(translate=str(q5[4]).replace('[', '').replace(']', ''))
    c = str(b).replace("<Record word='", '')
    word = c.replace("'>", '').replace('[', '').replace(']', '')
    result = await db.get_result(id=user_id)
    errors = str(await db.get_rus_test_error(user_id))
    if errors == 'None':
        errors = ''
    if answer == word:
        result += 1
        await message.answer('Правильно!')
    else:
        errors += word + ','
        await message.answer('Неправильно!')
    await db.set_rus_test_error(errors, user_id)
    await db.set_result(result, user_id)
    await state.update_data(answer5=answer)
    await message.answer(q5[5] + '\nКак пишется это слово по-английски?')
    await Test_State.next()


@dp.message_handler(state=Test_State.Q6)
async def answer_6(message: types.Message, state: FSMContext):
    answer = message.text.lower()
    user_id = message.from_user.id
    q6 = await db.get_questions(id=user_id)
    b = await db.select_word(translate=str(q6[5]).replace('[', '').replace(']', ''))
    c = str(b).replace("<Record word='", '')
    word = c.replace("'>", '').replace('[', '').replace(']', '')
    result = await db.get_result(id=user_id)
    errors = str(await db.get_rus_test_error(user_id))
    if errors == 'None':
        errors = ''
    if answer == word:
        result += 1
        await message.answer('Правильно!')
    else:
        errors += word + ','
        await message.answer('Неправильно!')
    await db.set_rus_test_error(errors, user_id)
    await db.set_result(result, user_id)
    await state.update_data(answer6=answer)
    await message.answer(q6[6] + '\nКак пишется это слово по-английски?')
    await Test_State.next()


@dp.message_handler(state=Test_State.Q7)
async def answer_7(message: types.Message, state: FSMContext):
    answer = message.text.lower()
    user_id = message.from_user.id
    q7 = await db.get_questions(id=user_id)
    b = await db.select_word(translate=str(q7[6]).replace('[', '').replace(']', ''))
    c = str(b).replace("<Record word='", '')
    word = c.replace("'>", '').replace('[', '').replace(']', '')
    result = await db.get_result(id=user_id)
    errors = str(await db.get_rus_test_error(user_id))
    if errors == 'None':
        errors = ''
    if answer == word:
        result += 1
        await message.answer('Правильно!')
    else:
        errors += word + ','
        await message.answer('Неправильно!')
    await db.set_rus_test_error(errors, user_id)
    await db.set_result(result, user_id)
    await state.update_data(answer7=answer)
    await message.answer(q7[7] + '\nКак пишется это слово по-английски?')
    await Test_State.next()


@dp.message_handler(state=Test_State.Q8)
async def answer_8(message: types.Message, state: FSMContext):
    answer = message.text.lower()
    user_id = message.from_user.id
    q8 = await db.get_questions(id=user_id)
    b = await db.select_word(translate=str(q8[7]).replace('[', '').replace(']', ''))
    c = str(b).replace("<Record word='", '')
    word = c.replace("'>", '').replace('[', '').replace(']', '')
    result = await db.get_result(id=user_id)
    errors = str(await db.get_rus_test_error(user_id))
    if errors == 'None':
        errors = ''
    if answer == word:
        result += 1
        await message.answer('Правильно!')
    else:
        errors += word + ','
        await message.answer('Неправильно!')
    await db.set_rus_test_error(errors, user_id)
    await db.set_result(result, user_id)
    await state.update_data(answer8=answer)
    await message.answer(q8[8] + '\nКак пишется это слово по-английски?')
    await Test_State.next()


@dp.message_handler(state=Test_State.Q9)
async def answer_9(message: types.Message, state: FSMContext):
    answer = message.text.lower()
    user_id = message.from_user.id
    q9 = await db.get_questions(id=user_id)
    b = await db.select_word(translate=str(q9[8]).replace('[', '').replace(']', ''))
    c = str(b).replace("<Record word='", '')
    word = c.replace("'>", '').replace('[', '').replace(']', '')
    result = await db.get_result(id=user_id)
    errors = str(await db.get_rus_test_error(user_id))
    if errors == 'None':
        errors = ''
    if answer == word:
        result += 1
        await message.answer('Правильно!')
    else:
        errors += word + ','
        await message.answer('Неправильно!')
    await db.set_rus_test_error(errors, user_id)
    await db.set_result(result, user_id)
    await state.update_data(answer9=answer)
    await state.set_state('learning')
    await message.answer('Спасибо за ваши ответы')
    await message.answer(f'Ошибок: {9-result} из 9 слов')
    await message.answer('Просмотреть ошибки в данном упражнении. /show_rus_test_errors', reply_markup=test_chooser)

# @dp.message_handler(state=Test_State.Q1)
# async def answer_1(message: types.Message, state: FSMCont
