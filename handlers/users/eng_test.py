from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from loader import dp, db
from aiogram import types

from states import Word_State
from keyboards.default import test_chooser


@dp.message_handler(text='Тестирование по оригиналу слов', state='learning')
async def test_info(message: types.Message):
    user_id = message.from_user.id
    await message.answer('Вы выбрали прохождение теста по оригиналу слов.', reply_markup=ReplyKeyboardRemove())
    q = await db.get_words_q(user_id)
    word = q[0]
    await message.answer(word + '\nКак переводится это слово?')
    await Word_State.Q1.set()


@dp.message_handler(state=Word_State.Q1)
async def answer_1(message: types.Message, state: FSMContext):
    answer = message.text.lower()
    user_id = message.from_user.id
    q1 = await db.get_words_q(user_id)
    b = await db.select_translate(word=str(q1[0]).replace('[', '').replace(']', ''))
    c = str(b).replace("<Record translate='", '')
    word1 = c.replace("'>", '').replace('[', '').replace(']', '')
    word = q1[1]
    errors = str(await db.get_eng_test_error(user_id))
    if errors == 'None':
        errors = ''
    result = await db.get_result(user_id)
    if answer == word1:
        result += 1
    else:
        errors += q1[0] + ','
    await db.set_eng_test_error(errors, user_id)
    await db.set_result(result, user_id)
    await state.update_data(answer1=answer)
    await message.answer(word + '\nКак переводится это слово?')
    await Word_State.next()


@dp.message_handler(state=Word_State.Q2)
async def answer_2(message: types.Message, state: FSMContext):
    answer = message.text.lower()
    user_id = message.from_user.id
    q2 = await db.get_words_q(user_id)
    b = await db.select_translate(word=str(q2[1]).replace('[', '').replace(']', ''))
    c = str(b).replace("<Record translate='", '')
    word1 = c.replace("'>", '').replace('[', '').replace(']', '')
    q = await db.get_words_q(user_id)
    word = q[2]
    result = await db.get_result(user_id)
    errors = str(await db.get_eng_test_error(user_id))
    if errors == 'None':
        errors = ''
    if answer == word1:
        result += 1
    else:
        errors += q2[1] + ','
    await db.set_eng_test_error(errors, user_id)
    await db.set_result(result, user_id)
    await state.update_data(answer2=answer)
    await message.answer(word + '\nКак переводится это слово?')
    await Word_State.next()


@dp.message_handler(state=Word_State.Q3)
async def answer_3(message: types.Message, state: FSMContext):
    answer = message.text.lower()
    user_id = message.from_user.id
    q3 = await db.get_words_q(user_id)
    b = await db.select_translate(word=str(q3[2]).replace('[', '').replace(']', ''))
    c = str(b).replace("<Record translate='", '')
    word1 = c.replace("'>", '').replace('[', '').replace(']', '')
    q = await db.get_words_q(user_id)
    word = q[3]
    result = await db.get_result(user_id)
    errors = str(await db.get_eng_test_error(user_id))
    if errors == 'None':
        errors = ''
    if answer == word1:
        result += 1
    else:
        errors += q3[2] + ','
    await db.set_eng_test_error(errors, user_id)
    await db.set_result(result, user_id)
    await state.update_data(answer3=answer)
    await message.answer(word + '\nКак переводится это слово?')
    await Word_State.next()


@dp.message_handler(state=Word_State.Q4)
async def answer_4(message: types.Message, state: FSMContext):
    answer = message.text.lower()
    user_id = message.from_user.id
    q4 = await db.get_words_q(user_id)
    b = await db.select_translate(word=str(q4[3]).replace('[', '').replace(']', ''))
    c = str(b).replace("<Record translate='", '')
    word1 = c.replace("'>", '').replace('[', '').replace(']', '')
    q = await db.get_words_q(user_id)
    word = q[4]
    result = await db.get_result(user_id)
    errors = str(await db.get_eng_test_error(user_id))
    if errors == 'None':
        errors = ''
    if answer == word1:
        result += 1
    else:
        errors += q4[3] + ','
    await db.set_eng_test_error(errors, user_id)
    await db.set_result(result, user_id)
    await state.update_data(answer4=answer)
    await message.answer(word + '\nКак переводится это слово?')
    await Word_State.next()


@dp.message_handler(state=Word_State.Q5)
async def answer_5(message: types.Message, state: FSMContext):
    answer = message.text.lower()
    user_id = message.from_user.id
    q5 = await db.get_words_q(user_id)
    b = await db.select_translate(word=str(q5[4]).replace('[', '').replace(']', ''))
    c = str(b).replace("<Record translate='", '')
    word1 = c.replace("'>", '').replace('[', '').replace(']', '')
    q = await db.get_words_q(user_id)
    word = q[5]
    result = await db.get_result(user_id)
    errors = str(await db.get_eng_test_error(user_id))
    if errors == 'None':
        errors = ''
    if answer == word1:
        result += 1
    else:
        errors += q5[4] + ','
    await db.set_eng_test_error(errors, user_id)
    await db.set_result(result, user_id)
    await state.update_data(answer5=answer)
    await message.answer(word + '\nКак переводится это слово?')
    await Word_State.next()


@dp.message_handler(state=Word_State.Q6)
async def answer_6(message: types.Message, state: FSMContext):
    answer = message.text.lower()
    user_id = message.from_user.id
    q6 = await db.get_words_q(user_id)
    b = await db.select_translate(word=str(q6[5]).replace('[', '').replace(']', ''))
    c = str(b).replace("<Record translate='", '')
    word1 = c.replace("'>", '').replace('[', '').replace(']', '')
    q = await db.get_words_q(user_id)
    word = q[6]
    result = await db.get_result(user_id)
    errors = str(await db.get_eng_test_error(user_id))
    if errors == 'None':
        errors = ''
    if answer == word1:
        result += 1
    else:
        errors += q6[5] + ','
    await db.set_eng_test_error(errors, user_id)
    await db.set_result(result, user_id)
    await state.update_data(answer6=answer)
    await message.answer(word + '\nКак переводится это слово?')
    await Word_State.next()


@dp.message_handler(state=Word_State.Q7)
async def answer_7(message: types.Message, state: FSMContext):
    answer = message.text.lower()
    user_id = message.from_user.id
    q7 = await db.get_words_q(user_id)
    b = await db.select_translate(word=str(q7[6]).replace('[', '').replace(']', ''))
    c = str(b).replace("<Record translate='", '')
    word1 = c.replace("'>", '').replace('[', '').replace(']', '')
    q = await db.get_words_q(user_id)
    word = q[7]
    result = await db.get_result(user_id)
    errors = str(await db.get_eng_test_error(user_id))
    if errors == 'None':
        errors = ''
    if answer == word1:
        result += 1
    else:
        errors += q7[6] + ','
    await db.set_eng_test_error(errors, user_id)
    await db.set_result(result, user_id)
    await state.update_data(answer7=answer)
    await message.answer(word + '\nКак переводится это слово?')
    await Word_State.next()


@dp.message_handler(state=Word_State.Q8)
async def answer_8(message: types.Message, state: FSMContext):
    answer = message.text.lower()
    user_id = message.from_user.id
    q8 = await db.get_words_q(user_id)
    b = await db.select_translate(word=str(q8[7]).replace('[', '').replace(']', ''))
    c = str(b).replace("<Record translate='", '')
    word1 = c.replace("'>", '').replace('[', '').replace(']', '')
    q = await db.get_words_q(user_id)
    word = q[8]
    result = await db.get_result(user_id)
    errors = str(await db.get_eng_test_error(user_id))
    if errors == 'None':
        errors = ''
    if answer == word1:
        result += 1
    else:
        errors += q8[7] + ','
    await db.set_eng_test_error(errors, user_id)
    await db.set_result(result, user_id)
    await state.update_data(answer8=answer)
    await message.answer(word + '\nКак переводится это слово?')
    await Word_State.next()


@dp.message_handler(state=Word_State.Q9)
async def answer_9(message: types.Message, state: FSMContext):
    answer = message.text.lower()
    user_id = message.from_user.id
    q9 = await db.get_words_q(id=user_id)
    b = await db.select_translate(word=str(q9[8]).replace('[', '').replace(']', ''))
    c = str(b).replace("<Record translate='", '')
    word = c.replace("'>", '').replace('[', '').replace(']', '')
    result = await db.get_result(id=user_id)
    errors = str(await db.get_eng_test_error(user_id))
    if errors == 'None':
        errors = ''
    if answer == word:
        result += 1
    else:
        errors += q9[8] + ','
    await db.set_eng_test_error(errors, user_id)
    await db.set_result(result, user_id)
    await state.update_data(answer9=answer)
    await state.set_state('learning')
    await message.answer('Спасибо за ваши ответы')
    await message.answer(f'Ошибок: {9 - result} из 9 слов')
    await db.set_user_state(current_state='main', id=message.from_user.id)
    await message.answer('Просмотреть ошибки в данном упражнении. /show_eng_test_errors', reply_markup=test_chooser)
