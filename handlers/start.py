from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import Router
import random
from c_bot import motivational_images

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет! Нажмите /motivation, чтобы получить мотивационное изображение!")

@router.message(Command('motivation'))
async def get_motivation(message: Message):
    image_url = random.choice(motivational_images)
    await message.reply_photo(photo=image_url)