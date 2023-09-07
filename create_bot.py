from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher


storage = MemoryStorage()

with open('token.txt') as f:
    TOKEN = f.readline().strip()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)