from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove

from loader import dp, db
from aiogram import types
from keyboards.default import test_chooser
from states import Sentence_State
import re


@dp.message_handler(text='Тестирование по предложениям', state='learning')
async def test_info(message: types.Message):
    user_id = message.from_user.id
    await message.answer('Вы выбрали прохождение теста по выбору слов в предложение.',
                         reply_markup=ReplyKeyboardRemove())
    q = await db.get_sentences(user_id)
    c = await db.get_all_words(id=user_id)
    sentence = q[0]
    await db.set_cur_sen(sentence=sentence, id=user_id)
    new_sentence = []
    for word in sentence.split():
        d = word.rstrip()
        opt = re.sub(r'[^\w\s]', '', d)
        new_sentence.append(opt)
    # print(new_sentence)
    # final = set()
    for word in c.split(",")[:-1]:

        for sen_word in new_sentence:
            if word[:2] in sen_word:
                new_sen = " ".join(new_sentence).replace(sen_word, "_")
                break
                # print(sen_word)
    # print(new_sen)
    # print(c.split(",")[:-1])
    await db.set_cur_sen_question(sentence=new_sen, id=user_id)
    await message.answer(new_sen + '\nЧто подставим? (Введите изученное английское слово)\n'
                                   '<i>В некоторых случаях понадобится изменять время глагола или же'
                                   'изменять часть речи слова и т.д.</i>', parse_mode=types.ParseMode.HTML)
    await Sentence_State.Q1.set()


@dp.message_handler(state=Sentence_State.Q1)
async def answer_1(message: types.Message, state: FSMContext):
    answer = message.text.lower()
    user_id = message.from_user.id
    q = await db.get_sentences(user_id)
    c = await db.get_all_words(id=user_id)
    q1 = await db.get_cur_sen(user_id)
    a1 = await db.get_cur_sen_question(user_id)
    sentence = q[1]
    new_sentence = []
    result = await db.get_result(user_id)
    errors = str(await db.get_sen_test_error(user_id))

    if errors == 'None':
        errors = ''
    # сделать столбец текекущего вопроса
    if q1.lower().strip() == a1.replace('_', answer).lower():
        result += 1
        await message.answer('yes!')
    else:
        errors += q1 + ','
    for word in sentence.split():
        d = word.rstrip()
        opt = re.sub(r'[^\w\s]', '', d)
        new_sentence.append(opt)
    for word in c.split(",")[:-1]:

        for sen_word in new_sentence:
            if word[:2] in sen_word:
                new_sen = " ".join(new_sentence).replace(sen_word, "_")
                break
    await db.set_sen_test_error(errors, user_id)
    await db.set_result(result, user_id)
    await db.set_cur_sen(sentence=sentence, id=user_id)
    await db.set_cur_sen_question(sentence=new_sen, id=user_id)
    await state.update_data(answer1=answer)
    await message.answer(new_sen + '\nЧто подставим? (Введите изученное английское слово)\n'
                                   '<i>В некоторых случаях понадобится изменять время глагола или же'
                                   'изменять часть речи слова и т.д.</i>', parse_mode=types.ParseMode.HTML)
    await Sentence_State.next()


@dp.message_handler(state=Sentence_State.Q1)
async def answer_1(message: types.Message, state: FSMContext):
    answer = message.text.lower()
    user_id = message.from_user.id
    q = await db.get_sentences(user_id)
    c = await db.get_all_words(id=user_id)
    q1 = await db.get_cur_sen(user_id)
    a1 = await db.get_cur_sen_question(user_id)
    sentence = q[1]
    new_sentence = []
    result = await db.get_result(user_id)
    errors = str(await db.get_sen_test_error(user_id))

    if errors == 'None':
        errors = ''
    # сделать столбец текекущего вопроса
    if q1.lower().strip() == a1.replace('_', answer).lower():
        result += 1
        await message.answer('yes!')
    else:
        errors += q1 + ','
    for word in sentence.split():
        d = word.rstrip()
        opt = re.sub(r'[^\w\s]', '', d)
        new_sentence.append(opt)
    for word in c.split(",")[:-1]:

        for sen_word in new_sentence:
            if word[:2] in sen_word:
                new_sen = " ".join(new_sentence).replace(sen_word, "_")
                break
    await db.set_sen_test_error(errors, user_id)
    await db.set_result(result, user_id)
    await db.set_cur_sen(sentence=sentence, id=user_id)
    await db.set_cur_sen_question(sentence=new_sen, id=user_id)
    await state.update_data(answer1=answer)
    await message.answer(new_sen + '\nЧто подставим? (Введите изученное английское слово)\n'
                                   '<i>В некоторых случаях понадобится изменять время глагола или же'
                                   'изменять часть речи слова и т.д.</i>', parse_mode=types.ParseMode.HTML)
    await Sentence_State.next()


@dp.message_handler(state=Sentence_State.Q1)
async def answer_1(message: types.Message, state: FSMContext):
    answer = message.text.lower()
    user_id = message.from_user.id
    q = await db.get_sentences(user_id)
    c = await db.get_all_words(id=user_id)
    q1 = await db.get_cur_sen(user_id)
    a1 = await db.get_cur_sen_question(user_id)
    sentence = q[1]
    new_sentence = []
    result = await db.get_result(user_id)
    errors = str(await db.get_sen_test_error(user_id))

    if errors == 'None':
        errors = ''
    # сделать столбец текекущего вопроса
    if q1.lower().strip() == a1.replace('_', answer).lower():
        result += 1
        await message.answer('yes!')
    else:
        errors += q1 + ','
    for word in sentence.split():
        d = word.rstrip()
        opt = re.sub(r'[^\w\s]', '', d)
        new_sentence.append(opt)
    for word in c.split(",")[:-1]:

        for sen_word in new_sentence:
            if word[:2] in sen_word:
                new_sen = " ".join(new_sentence).replace(sen_word, "_")
                break
    await db.set_sen_test_error(errors, user_id)
    await db.set_result(result, user_id)
    await db.set_cur_sen(sentence=sentence, id=user_id)
    await db.set_cur_sen_question(sentence=new_sen, id=user_id)
    await state.update_data(answer1=answer)
    await message.answer(new_sen + '\nЧто подставим? (Введите изученное английское слово)\n'
                                   '<i>В некоторых случаях понадобится изменять время глагола или же'
                                   'изменять часть речи слова и т.д.</i>', parse_mode=types.ParseMode.HTML)
    await Sentence_State.next()


@dp.message_handler(state=Sentence_State.Q2)
async def answer_2(message: types.Message, state: FSMContext):
    answer = message.text.lower()
    user_id = message.from_user.id
    q = await db.get_sentences(user_id)
    c = await db.get_all_words(id=user_id)
    q1 = await db.get_cur_sen(user_id)
    a1 = await db.get_cur_sen_question(user_id)
    sentence = q[2]
    new_sentence = []
    result = await db.get_result(user_id)
    errors = str(await db.get_sen_test_error(user_id))

    if errors == 'None':
        errors = ''
    # сделать столбец текекущего вопроса
    if q1.lower().strip() == a1.replace('_', answer).lower():
        result += 1
        await message.answer('yes!')
    else:
        errors += q1 + ','
    for word in sentence.split():
        d = word.rstrip()
        opt = re.sub(r'[^\w\s]', '', d)
        new_sentence.append(opt)
    for word in c.split(",")[:-1]:

        for sen_word in new_sentence:
            if word[:2] in sen_word:
                new_sen = " ".join(new_sentence).replace(sen_word, "_")
                break
    await db.set_sen_test_error(errors, user_id)
    await db.set_result(result, user_id)
    await db.set_cur_sen(sentence=sentence, id=user_id)
    await db.set_cur_sen_question(sentence=new_sen, id=user_id)
    await state.update_data(answer1=answer)
    await message.answer(new_sen + '\nЧто подставим? (Введите изученное английское слово)\n'
                                   '<i>В некоторых случаях понадобится изменять время глагола или же'
                                   'изменять часть речи слова и т.д.</i>', parse_mode=types.ParseMode.HTML)
    await Sentence_State.next()


@dp.message_handler(state=Sentence_State.Q3)
async def answer_3(message: types.Message, state: FSMContext):
    answer = message.text.lower()
    user_id = message.from_user.id
    q = await db.get_sentences(user_id)
    c = await db.get_all_words(id=user_id)
    q1 = await db.get_cur_sen(user_id)
    a1 = await db.get_cur_sen_question(user_id)
    sentence = q[2]
    new_sentence = []
    result = await db.get_result(user_id)
    errors = str(await db.get_sen_test_error(user_id))

    if errors == 'None':
        errors = ''
    # сделать столбец текекущего вопроса
    if q1.lower().strip() == a1.replace('_', answer).lower():
        result += 1
        await message.answer('yes!')
    else:
        errors += q1 + ','
    for word in sentence.split():
        d = word.rstrip()
        opt = re.sub(r'[^\w\s]', '', d)
        new_sentence.append(opt)
    for word in c.split(",")[:-1]:

        for sen_word in new_sentence:
            if word[:2] in sen_word:
                new_sen = " ".join(new_sentence).replace(sen_word, "_")
                break
    await db.set_sen_test_error(errors, user_id)
    await db.set_result(result, user_id)
    await db.set_cur_sen(sentence=sentence, id=user_id)
    await db.set_cur_sen_question(sentence=new_sen, id=user_id)
    await state.update_data(answer1=answer)
    await message.answer(new_sen + '\nЧто подставим? (Введите изученное английское слово)\n'
                                   '<i>В некоторых случаях понадобится изменять время глагола или же'
                                   'изменять часть речи слова и т.д.</i>', parse_mode=types.ParseMode.HTML)
    await Sentence_State.next()


@dp.message_handler(state=Sentence_State.Q4)
async def answer_4(message: types.Message, state: FSMContext):
    answer = message.text.lower()
    user_id = message.from_user.id
    q = await db.get_sentences(user_id)
    c = await db.get_all_words(id=user_id)
    q1 = await db.get_cur_sen(user_id)
    a1 = await db.get_cur_sen_question(user_id)
    sentence = q[3]
    new_sentence = []
    result = await db.get_result(user_id)
    errors = str(await db.get_sen_test_error(user_id))

    if errors == 'None':
        errors = ''
    # сделать столбец текекущего вопроса
    if q1.lower().strip() == a1.replace('_', answer).lower():
        result += 1
        await message.answer('yes!')
    else:
        errors += q1 + ','
    for word in sentence.split():
        d = word.rstrip()
        opt = re.sub(r'[^\w\s]', '', d)
        new_sentence.append(opt)
    for word in c.split(",")[:-1]:

        for sen_word in new_sentence:
            if word[:2] in sen_word:
                new_sen = " ".join(new_sentence).replace(sen_word, "_")
                break
    await db.set_sen_test_error(errors, user_id)
    await db.set_result(result, user_id)
    await db.set_cur_sen(sentence=sentence, id=user_id)
    await db.set_cur_sen_question(sentence=new_sen, id=user_id)
    await state.update_data(answer1=answer)
    await message.answer(new_sen + '\nЧто подставим? (Введите изученное английское слово)\n'
                                   '<i>В некоторых случаях понадобится изменять время глагола или же'
                                   'изменять часть речи слова и т.д.</i>', parse_mode=types.ParseMode.HTML)
    await Sentence_State.next()


@dp.message_handler(state=Sentence_State.Q5)
async def answer_5(message: types.Message, state: FSMContext):
    answer = message.text.lower()
    user_id = message.from_user.id
    q = await db.get_sentences(user_id)
    c = await db.get_all_words(id=user_id)
    q1 = await db.get_cur_sen(user_id)
    a1 = await db.get_cur_sen_question(user_id)
    sentence = q[4]
    new_sentence = []
    result = await db.get_result(user_id)
    errors = str(await db.get_sen_test_error(user_id))

    if errors == 'None':
        errors = ''
    # сделать столбец текекущего вопроса
    if q1.lower().strip() == a1.replace('_', answer).lower():
        result += 1
        await message.answer('yes!')
    else:
        errors += q1 + ','
    for word in sentence.split():
        d = word.rstrip()
        opt = re.sub(r'[^\w\s]', '', d)
        new_sentence.append(opt)
    for word in c.split(",")[:-1]:

        for sen_word in new_sentence:
            if word[:2] in sen_word:
                new_sen = " ".join(new_sentence).replace(sen_word, "_")
                break
    await db.set_sen_test_error(errors, user_id)
    await db.set_result(result, user_id)
    await db.set_cur_sen(sentence=sentence, id=user_id)
    await db.set_cur_sen_question(sentence=new_sen, id=user_id)
    await state.update_data(answer1=answer)
    await message.answer(new_sen + '\nЧто подставим? (Введите изученное английское слово)\n'
                                   '<i>В некоторых случаях понадобится изменять время глагола или же'
                                   'изменять часть речи слова и т.д.</i>', parse_mode=types.ParseMode.HTML)
    await Sentence_State.next()


@dp.message_handler(state=Sentence_State.Q6)
async def answer_6(message: types.Message, state: FSMContext):
    answer = message.text.lower()
    user_id = message.from_user.id
    q = await db.get_sentences(user_id)
    c = await db.get_all_words(id=user_id)
    q1 = await db.get_cur_sen(user_id)
    a1 = await db.get_cur_sen_question(user_id)
    sentence = q[5]
    new_sentence = []
    result = await db.get_result(user_id)
    errors = str(await db.get_sen_test_error(user_id))

    if errors == 'None':
        errors = ''
    # сделать столбец текекущего вопроса
    if q1.lower().strip() == a1.replace('_', answer).lower():
        result += 1
        await message.answer('yes!')
    else:
        errors += q1 + ','
    for word in sentence.split():
        d = word.rstrip()
        opt = re.sub(r'[^\w\s]', '', d)
        new_sentence.append(opt)
    for word in c.split(",")[:-1]:

        for sen_word in new_sentence:
            if word[:2] in sen_word:
                new_sen = " ".join(new_sentence).replace(sen_word, "_")
                break
    await db.set_sen_test_error(errors, user_id)
    await db.set_result(result, user_id)
    await db.set_cur_sen(sentence=sentence, id=user_id)
    await db.set_cur_sen_question(sentence=new_sen, id=user_id)
    await state.update_data(answer1=answer)
    await message.answer(new_sen + '\nЧто подставим? (Введите изученное английское слово)\n'
                                   '<i>В некоторых случаях понадобится изменять время глагола или же'
                                   'изменять часть речи слова и т.д.</i>', parse_mode=types.ParseMode.HTML)
    await Sentence_State.next()


@dp.message_handler(state=Sentence_State.Q7)
async def answer_7(message: types.Message, state: FSMContext):
    answer = message.text.lower()
    user_id = message.from_user.id
    q = await db.get_sentences(user_id)
    c = await db.get_all_words(id=user_id)
    q1 = await db.get_cur_sen(user_id)
    a1 = await db.get_cur_sen_question(user_id)
    sentence = q[6]
    new_sentence = []
    result = await db.get_result(user_id)
    errors = str(await db.get_sen_test_error(user_id))

    if errors == 'None':
        errors = ''
    # сделать столбец текекущего вопроса
    if q1.lower().strip() == a1.replace('_', answer).lower():
        result += 1
        await message.answer('yes!')
    else:
        errors += q1 + ','
    for word in sentence.split():
        d = word.rstrip()
        opt = re.sub(r'[^\w\s]', '', d)
        new_sentence.append(opt)
    for word in c.split(",")[:-1]:

        for sen_word in new_sentence:
            if word[:2] in sen_word:
                new_sen = " ".join(new_sentence).replace(sen_word, "_")
                break
    await db.set_sen_test_error(errors, user_id)
    await db.set_result(result, user_id)
    await db.set_cur_sen(sentence=sentence, id=user_id)
    await db.set_cur_sen_question(sentence=new_sen, id=user_id)
    await state.update_data(answer1=answer)
    await message.answer(new_sen + '\nЧто подставим? (Введите изученное английское слово)\n'
                                   '<i>В некоторых случаях понадобится изменять время глагола или же'
                                   'изменять часть речи слова и т.д.</i>', parse_mode=types.ParseMode.HTML)
    await Sentence_State.next()


@dp.message_handler(state=Sentence_State.Q8)
async def answer_8(message: types.Message, state: FSMContext):
    answer = message.text.lower()
    user_id = message.from_user.id
    q = await db.get_sentences(user_id)
    c = await db.get_all_words(id=user_id)
    q1 = await db.get_cur_sen(user_id)
    a1 = await db.get_cur_sen_question(user_id)
    sentence = q[7]
    new_sentence = []
    result = await db.get_result(user_id)
    errors = str(await db.get_sen_test_error(user_id))

    if errors == 'None':
        errors = ''
    # сделать столбец текекущего вопроса
    if q1.lower().strip() == a1.replace('_', answer).lower():
        result += 1
        await message.answer('yes!')
    else:
        errors += q1 + ','
    for word in sentence.split():
        d = word.rstrip()
        opt = re.sub(r'[^\w\s]', '', d)
        new_sentence.append(opt)
    for word in c.split(",")[:-1]:

        for sen_word in new_sentence:
            if word[:2] in sen_word:
                new_sen = " ".join(new_sentence).replace(sen_word, "_")
                break
    await db.set_sen_test_error(errors, user_id)
    await db.set_result(result, user_id)
    await db.set_cur_sen(sentence=sentence, id=user_id)
    await db.set_cur_sen_question(sentence=new_sen, id=user_id)
    await state.update_data(answer1=answer)
    await message.answer(new_sen + '\nЧто подставим? (Введите изученное английское слово)\n'
                                   '<i>В некоторых случаях понадобится изменять время глагола или же'
                                   'изменять часть речи слова и т.д.</i>', parse_mode=types.ParseMode.HTML)
    await Sentence_State.next()


@dp.message_handler(state=Sentence_State.Q9)
async def answer_9(message: types.Message, state: FSMContext):
    answer = message.text.lower()
    user_id = message.from_user.id
    q = await db.get_sentences(user_id)
    c = await db.get_all_words(id=user_id)
    q1 = await db.get_cur_sen(user_id)
    a1 = await db.get_cur_sen_question(user_id)
    sentence = q[8]
    new_sentence = []
    result = await db.get_result(user_id)
    errors = str(await db.get_sen_test_error(user_id))

    if errors == 'None':
        errors = ''
    # сделать столбец текекущего вопроса
    if q1.lower().strip() == a1.replace('_', answer).lower():
        result += 1
        await message.answer('yes!')
    else:
        errors += q1 + ','
    for word in sentence.split():
        d = word.rstrip()
        opt = re.sub(r'[^\w\s]', '', d)
        new_sentence.append(opt)
    for word in c.split(",")[:-1]:

        for sen_word in new_sentence:
            if word[:2] in sen_word:
                new_sen = " ".join(new_sentence).replace(sen_word, "_")
                break
    await db.set_sen_test_error(errors, user_id)
    await db.set_result(result, user_id)

    await db.set_def_test_error(errors, user_id)
    await db.set_result(result, user_id)
    await state.update_data(answer9=answer)
    await state.set_state('learning')
    await message.answer('Спасибо за ваши ответы')
    await message.answer(f'Ошибок: {9 - result} из 9 слов')
    await db.set_user_state(current_state='main', id=message.from_user.id)
    await message.answer('Просмотреть ошибки в данном упражнении. /show_def_test_errors', reply_markup=test_chooser)

