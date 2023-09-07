from aiogram import types
from aiogram.dispatcher import Dispatcher
from keyboards import kb_client
from asyncio import sleep
from create_bot import bot
# from data_base import sqlite_db

async def command_start(message: types.Message):
    hello_message = f'Привет {message.from_user.id}. Начинаем игру!'
    await message.answer(message.text, reply_markup=kb_client)
    await sleep(1)

    bot_dice = await bot.send_dice(message.from_user.id)
    bot_data = bot_dice['dice']['value']
    await sleep(5)

    user_dice = await bot.send_dice(message.from_user.id)
    user_data = user_dice['dice']['value']
    await sleep(5)

    if bot_data > user_data:
        await message.answer("Вы проиграли \U0001F635")
    elif bot_data < user_data:
        await message.answer("Вы выйграли \U0001F605")
    else:
        await message.answer("Ничья \U0001F928")




async def command_about(message: types.Message):
    await message.answer("Азартная Онлайн игра 'Кости'. Компьютер кидает кубик, далее игрок кидает кубик с числом от 1 до 6. У кого больше число тот и выиграл.")


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(command_about, commands=['about'])
