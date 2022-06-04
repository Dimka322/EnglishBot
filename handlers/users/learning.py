from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove

from keyboards.default import answer_yes
from loader import dp, db
from aiogram import types
from states import User_States
from keyboards.default import test_chooser


@dp.message_handler(Command('learn_words'), state='main')
async def learn_words(message: types.Message):
    level = await db.get_user_level(message.from_user.id)
    quantity = await db.get_quantity(message.from_user.id)
    if str(level).replace('   ', '') == 'B1' and quantity < 963:
        await message.answer('Вы выбрали изучение слов, готовы начать?', reply_markup=answer_yes)
        await User_States.Learning.set()
    else:
        rus_errors = await db.get_rus_test_error(message.from_user.id)
        def_errors = await db.get_def_test_error(message.from_user.id)
        sen_errors = await db.get_sen_test_errors(message.from_user.id)
        eng_errors = await db.get_eng_test_error(message.from_user.id)
        errors = []
        if rus_errors:
            errors += rus_errors.split(',')
        if def_errors:
            errors += def_errors.split(',')
        if sen_errors:
            errors += sen_errors.split(',')
        if eng_errors:
            errors += eng_errors.split(',')

        errors = list(set(errors))

        if len(errors) > 0:
            await message.answer('Вам следует повторить слова, в которых были допущены ошибки\n')
            errors = "\n".join(errors)
            await message.answer(errors)

        await message.answer('К сожалению ваш уровень не предполагает изучение слов :(' + '\n' + "Зато теперь будут "
                                                                                                 "доступны задания на распознавание")
        await db.set_user_level('B2-C1', message.from_user.id)
        print(level)


@dp.message_handler(text="Да", state=User_States.Learning)
async def learning(message: types.Message, state: FSMContext):
    await message.answer('Начинаем!', reply_markup=ReplyKeyboardRemove())
    user_id = message.from_user.id
    isEnd = False
    quantity = await db.get_quantity(id=user_id)
    # b = str(a).replace('<Record quantity_words=', '').replace('>', '')

    previous_quantity = await db.get_prev_quantity(user_id)
    # v = str(s).replace('<Record previous_quantity=', '').replace('>', '')
    if quantity > 963:
        await state.set_state('finish')
        isEnd = True
    all_words = str(await db.get_all_words(user_id))
    if all_words == 'None':
        all_words = ''
    words = []
    words1 = []
    words2 = []
    words3 = []
    for i in range(1 + previous_quantity, quantity + 1):
        dictator = {}
        b = await db.select_cur_word(id=i)
        word = b[0][1]
        dictator['Слово'] = word
        transcription = str(b[0][2])
        dictator['Транскрипция'] = transcription.replace('\n', '')

        translate = str(b[0][3])
        dictator['Перевод'] = translate

        word_type = str(b[0][4])
        dictator['Часть речи'] = word_type

        definition = str(b[0][5])
        dictator['Значение'] = definition.replace('"', '')

        sentence = str(b[0]['sentences'])
        dictator['Предложение'] = sentence
        await message.answer(
            'Слово: ' + dictator['Слово'] + '\nТранскрипция: ' + dictator['Транскрипция'] + '\nПеревод: ' +
            dictator[
                'Перевод'] + '\nЧасть речи: ' + dictator['Часть речи'] + '\nЗначение: ' + dictator['Значение'])
        all_words += word + ','
        words.append(dictator['Перевод'])
        words1.append(dictator['Слово'])
        words2.append(dictator['Значение'])
        words3.append(dictator['Предложение'])
        await db.set_questions(words, user_id)
        await db.set_words(words1, user_id)
        await db.set_definition(words2, user_id)
        await db.set_sentences(words3, user_id)
        dictator.clear()
    await db.set_all_words(all_words, user_id)
    await db.update_prev_quantity(quantity, user_id)
    await db.update_quantity(quantity + 9, user_id)
    await message.answer('Вам доступны несколько видов тестирования!', reply_markup=test_chooser)
    await db.set_user_state(current_state='learning', id=message.from_user.id)
    await state.set_state("learning")
    # await message.answer(await db.select_word(id=i))
