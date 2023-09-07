from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button = KeyboardButton('/Меню')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)  # one_time_keyboard=True # скрыть клаву
kb_client.add(button)