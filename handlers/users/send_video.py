from aiogram.dispatcher.filters import Command
from aiogram.types import ContentType, Message, InputFile

from loader import dp, bot


@dp.message_handler(content_types=ContentType.VIDEO, state='*')
async def get_file_id_v(message: Message):
    await message.reply(message.video.file_id)


@dp.message_handler(Command("get_video"), state='*')
async def send(message: Message):
    video_file_id = '..'
    video_url = ""
    video_bytes = InputFile(path_or_bytesio=
                            "IMG_0148.mp4")
    await bot.send_video(chat_id=message.from_user.id,
                         video=video_bytes,)
