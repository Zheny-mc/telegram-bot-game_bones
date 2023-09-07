from aiogram import types
from aiogram.dispatcher import Dispatcher
from keyboards import kb_client
# from data_base import sqlite_db

async def command_start(message: types.Message):
    await message.answer(message.text, reply_markup=kb_client)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
