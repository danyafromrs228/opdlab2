from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("BOT_TOKEN")

motivational_images = [
    'https://i.pinimg.com/736x/e1/88/e0/e188e027260b4d1c1506af9932576bf0.jpg',
    'https://i.pinimg.com/736x/95/82/3b/95823bc031a5da2e4bf57c993824ce8a.jpg',
    'https://avatars.mds.yandex.net/i?id=63122f849da3bfd538f58b1d3678d711_l-3452879-images-thumbs&n=13',

]

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)