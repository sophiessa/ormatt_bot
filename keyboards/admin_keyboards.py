from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

upload_btn = KeyboardButton('Загрузить')
cancel_btn = KeyboardButton('Отменить')

join_btn   = KeyboardButton('Добавиться к консультантам')

admin_keyboard_cancel = ReplyKeyboardMarkup(resize_keyboard=True).add(cancel_btn).add(join_btn)
admin_keyboard_upload = ReplyKeyboardMarkup(resize_keyboard=True).add(upload_btn).add(join_btn)