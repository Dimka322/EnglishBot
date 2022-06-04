from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove

from keyboards.default import answer_yes
from loader import dp, db
from aiogram import types
from states import User_States
from keyboards.default import test_chooser


@dp.message_handler(Command("test"), state='main')
async def test_info(message: types.Message, questions: list = await db.get_questions()):
    if len(questions)==0:
        await message.answer('Пройдено')
    else:
        message.answer(questions[0])
        new_questions = questions.pop(0)
        return test_info(new_questions)
