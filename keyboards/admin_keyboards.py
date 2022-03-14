from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

upload_btn = KeyboardButton('Загрузить')
cancel_btn = KeyboardButton('Отменить')
delete_btn = KeyboardButton('Удалить')

join_btn   = KeyboardButton('Добавиться к консультантам')

admin_keyboard_cancel = ReplyKeyboardMarkup(resize_keyboard=True).add(cancel_btn)
admin_keyboard_upload = ReplyKeyboardMarkup(resize_keyboard=True).row(upload_btn, delete_btn)