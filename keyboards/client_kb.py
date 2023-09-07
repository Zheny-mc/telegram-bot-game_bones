from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_start = KeyboardButton('/start')
button_about = KeyboardButton('/about')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)  # one_time_keyboard=True # скрыть клаву
kb_client.add(button_start).add(button_about)