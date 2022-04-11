from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def start_button():
    return ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('/start'))