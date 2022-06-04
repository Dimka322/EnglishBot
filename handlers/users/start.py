from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove, ContentType, InputFile

from loader import dp, db, bot

from keyboards.default import user_level


#@dp.message_handler(content_types=ContentType.VIDEO)
#async def get_file_id_v(message: types.Message):
#    await message.reply(message.video_file_id)


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, state: FSMContext):
    video_bytes = InputFile(path_or_bytesio=
                            "IMG_0148.mp4")
    await bot.send_video(chat_id=message.from_user.id,
                         video=video_bytes)
    name = message.from_user.full_name
    await db.delete_users()
    await db.set_all_words('', message.from_user.id)
    try:
        await db.add_user(id=message.from_user.id, name=name)
        await db.set_user_state(current_state='main', id=message.from_user.id)
        await message.answer(f'Привет, {message.from_user.full_name}!')
        await message.answer(
            'Выберите ваш уровень знания английского языка. (Одна из кнопок вспомогательного меню)\n'
            'Вам предложено изучать 9 слов за *', reply_markup=user_level)
        await state.set_state('level')
    except Exception:
        await message.answer('Вы уже с нами!')
        await state.set_state('main')


@dp.message_handler(text='B1', state='level')
async def b1(message: types.Message, state: FSMContext):
    await db.set_user_level(level=message.text, id=message.from_user.id)
    await message.answer('Для того, чтобы было проще начать - введите /help. \n'
                         'Чтобы начать изучение слов, введите или нажмите на /learn_words\n',
                         reply_markup=ReplyKeyboardRemove())
    await state.set_state('main')


@dp.message_handler(text='B2-C1', state='level')
async def b2(message: types.Message, state: FSMContext):
    await db.set_user_level(level=message.text, id=message.from_user.id)
    await message.answer('Для того, чтобы было проще начать - введите /help. \n'
                         'Чтобы начать изучение слов, введите или нажмите на /learn_words\n',
                         reply_markup=ReplyKeyboardRemove())
    await state.set_state('main')
