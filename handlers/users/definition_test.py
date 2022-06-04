from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove

from loader import dp, db
from aiogram import types
from keyboards.default import test_chooser
from states import Definition_State


@dp.message_handler(text='Тестирование по значению слов', state='learning')
async def test_info(message: types.Message):
    user_id = message.from_user.id
    await message.answer('Вы выбрали прохождение теста по значению слов.', reply_markup=ReplyKeyboardRemove())
    q = await db.get_definiton(user_id)
    definition = q[0]
    await message.answer(definition + '\nЧто означает это выражение? (Введите изученное английское слово)')
    await Definition_State.Q1.set()


@dp.message_handler(state=Definition_State.Q1)
async def answer_1(message: types.Message, state: FSMContext):
    answer = message.text.lower()
    user_id = message.from_user.id
    q1 = await db.get_definiton(user_id)
    b = await db.select_word(definition=str(q1[0]).replace('[', '').replace(']', ''))
    c = str(b).replace("<Record word='", '')
    word = c.replace("'>", '').replace('[', '').replace(']', '')
    word1 = q1[1]
    result = await db.get_result(user_id)
    errors = str(await db.get_def_test_error(user_id))
    if errors == 'None':
        errors = ''
    if answer == word:
        result += 1
    else:
        errors += q1[0] + ','
    await db.set_def_test_error(errors, user_id)
    await db.set_result(result, user_id)
    await state.update_data(answer1=answer)
    await message.answer(word1 + '\nЧто означает это выражение? (Введите изученное английское слово)')
    await Definition_State.next()


@dp.message_handler(state=Definition_State.Q2)
async def answer_2(message: types.Message, state: FSMContext):
    answer = message.text.lower()
    user_id = message.from_user.id
    q2 = await db.get_definiton(user_id)
    b = await db.select_word(definition=str(q2[1]).replace('[', '').replace(']', ''))
    c = str(b).replace("<Record word='", '')
    word1 = c.replace("'>", '').replace('[', '').replace(']', '')
    word = q2[2]
    result = await db.get_result(user_id)
    errors = str(await db.get_def_test_error(user_id))
    if errors == 'None':
        errors = ''
    if answer == word1:
        result += 1
    else:
        errors += q2[1] + ','
    await db.set_def_test_error(errors, user_id)
    await db.set_result(result, user_id)
    await state.update_data(answer2=answer)
    await message.answer(word + '\nЧто означает это выражение? (Введите изученное английское слово)')
    await Definition_State.next()


@dp.message_handler(state=Definition_State.Q3)
async def answer_3(message: types.Message, state: FSMContext):
    answer = message.text.lower()
    user_id = message.from_user.id
    q3 = await db.get_definiton(user_id)
    b = await db.select_word(definition=str(q3[2]).replace('[', '').replace(']', ''))
    c = str(b).replace("<Record word='", '')
    word1 = c.replace("'>", '').replace('[', '').replace(']', '')
    word = q3[3]
    result = await db.get_result(user_id)
    errors = str(await db.get_def_test_error(user_id))
    if errors == 'None':
        errors = ''
    if answer == word1:
        result += 1
    else:
        errors += q3[2] + ','
    await db.set_def_test_error(errors, user_id)
    await db.set_result(result, user_id)
    await state.update_data(answer3=answer)
    await message.answer(word + '\nЧто означает это выражение? (Введите изученное английское слово)')
    await Definition_State.next()


@dp.message_handler(state=Definition_State.Q4)
async def answer_4(message: types.Message, state: FSMContext):
    answer = message.text.lower()
    user_id = message.from_user.id
    q4 = await db.get_definiton(user_id)
    b = await db.select_word(definition=str(q4[3]).replace('[', '').replace(']', ''))
    c = str(b).replace("<Record word='", '')
    word1 = c.replace("'>", '').replace('[', '').replace(']', '')
    word = q4[4]
    result = await db.get_result(user_id)
    errors = str(await db.get_def_test_error(user_id))
    if errors == 'None':
        errors = ''
    if answer == word1:
        result += 1
    else:
        errors += q4[3] + ','
    await db.set_def_test_error(errors, user_id)
    await db.set_result(result, user_id)
    await state.update_data(answer4=answer)
    await message.answer(word + '\nЧто означает это выражение? (Введите изученное английское слово)')
    await Definition_State.next()


@dp.message_handler(state=Definition_State.Q5)
async def answer_5(message: types.Message, state: FSMContext):
    answer = message.text.lower()
    user_id = message.from_user.id
    q5 = await db.get_definiton(user_id)
    b = await db.select_word(definition=str(q5[4]).replace('[', '').replace(']', ''))
    c = str(b).replace("<Record word='", '')
    word1 = c.replace("'>", '').replace('[', '').replace(']', '')
    word = q5[5]
    result = await db.get_result(user_id)
    errors = str(await db.get_def_test_error(user_id))
    if errors == 'None':
        errors = ''
    if answer == word1:
        result += 1
    else:
        errors += q5[4] + ','
    await db.set_def_test_error(errors, user_id)
    await db.set_result(result, user_id)
    await state.update_data(answer5=answer)
    await message.answer(word + '\nЧто означает это выражение? (Введите изученное английское слово)')
    await Definition_State.next()


@dp.message_handler(state=Definition_State.Q6)
async def answer_6(message: types.Message, state: FSMContext):
    answer = message.text.lower()
    user_id = message.from_user.id
    q6 = await db.get_definiton(user_id)
    b = await db.select_word(definition=str(q6[5]).replace('[', '').replace(']', ''))
    c = str(b).replace("<Record word='", '')
    word1 = c.replace("'>", '').replace('[', '').replace(']', '')
    word = q6[6]
    result = await db.get_result(user_id)
    errors = str(await db.get_def_test_error(user_id))
    if errors == 'None':
        errors = ''
    if answer == word1:
        result += 1
    else:
        errors += q6[5] + ','
    await db.set_def_test_error(errors, user_id)
    await db.set_result(result, user_id)
    await state.update_data(answer6=answer)
    await message.answer(word + '\nЧто означает это выражение? (Введите изученное английское слово)')
    await Definition_State.next()


@dp.message_handler(state=Definition_State.Q7)
async def answer_7(message: types.Message, state: FSMContext):
    answer = message.text.lower()
    user_id = message.from_user.id
    q7 = await db.get_definiton(user_id)
    b = await db.select_word(definition=str(q7[6]).replace('[', '').replace(']', ''))
    c = str(b).replace("<Record word='", '')
    word1 = c.replace("'>", '').replace('[', '').replace(']', '')
    word = q7[7]
    result = await db.get_result(user_id)
    errors = str(await db.get_def_test_error(user_id))
    if errors == 'None':
        errors = ''
    if answer == word1:
        result += 1
    else:
        errors += q7[6] + ','
    await db.set_def_test_error(errors, user_id)
    await db.set_result(result, user_id)
    await state.update_data(answer7=answer)
    await message.answer(word + '\nЧто означает это выражение? (Введите изученное английское слово)')
    await Definition_State.next()


@dp.message_handler(state=Definition_State.Q8)
async def answer_8(message: types.Message, state: FSMContext):
    answer = message.text.lower()
    user_id = message.from_user.id
    q8 = await db.get_definiton(user_id)
    b = await db.select_word(definition=str(q8[7]).replace('[', '').replace(']', ''))
    c = str(b).replace("<Record word='", '')
    word1 = c.replace("'>", '').replace('[', '').replace(']', '')
    word = q8[8]
    result = await db.get_result(user_id)
    errors = str(await db.get_def_test_error(user_id))
    if errors == 'None':
        errors = ''
    if answer == word1:
        result += 1
    else:
        errors += q8[7] + ','
    await db.set_def_test_error(errors, user_id)
    await db.set_result(result, user_id)
    await state.update_data(answer8=answer)
    await message.answer(word + '\nЧто означает это выражение? (Введите изученное английское слово)')
    await Definition_State.next()


@dp.message_handler(state=Definition_State.Q9)
async def answer_9(message: types.Message, state: FSMContext):
    answer = message.text.lower()
    user_id = message.from_user.id
    q9 = await db.get_definiton(id=user_id)
    b = await db.select_word(word=str(q9[8]).replace('[', '').replace(']', ''))
    c = str(b).replace("<Record word='", '')
    word = c.replace("'>", '').replace('[', '').replace(']', '')
    result = await db.get_result(id=user_id)
    errors = str(await db.get_def_test_error(user_id))
    if errors == 'None':
        errors = ''
    if answer == word:
        result += 1
    else:
        errors += q9[8] + ','
    await db.set_def_test_error(errors, user_id)
    await db.set_result(result, user_id)
    await state.update_data(answer9=answer)
    await state.set_state('learning')
    await message.answer('Спасибо за ваши ответы')
    await message.answer(f'Ошибок: {9 - result} из 9 слов')
    await db.set_user_state(current_state='main', id=message.from_user.id)
    await message.answer('Просмотреть ошибки в данном упражнении. /show_def_test_errors', reply_markup=test_chooser)