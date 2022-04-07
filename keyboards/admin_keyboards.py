#aiogram imports
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


# admin_keyboard_cancel = ReplyKeyboardMarkup(resize_keyboard=True).add(cancel_btn)
def upload_delete_markup(lang: str):
    upload_btn = {
        'ru': KeyboardButton('Загрузить'),
        'en': KeyboardButton('Upload'),
        'kg': KeyboardButton('Жүктөө'),
    }
    cancel_btn = {
        'ru': KeyboardButton('Отменить'),
        'en': KeyboardButton('Cancel'),
        'kg': KeyboardButton('Жокко чыгаруу'),
    }
    delete_btn = {
        'ru': KeyboardButton('Удалить'),
        'en': KeyboardButton('Delete'),
        'kg': KeyboardButton('Жок кылуу'),
    }

    join_btn = {
        'ru': KeyboardButton('Добавиться к консультантам'),
        'en': KeyboardButton('Join consultants'),
        'kg': KeyboardButton('Менеджерлерге кошулуу'),
    }
    return ReplyKeyboardMarkup(resize_keyboard=True).add(upload_btn[lang], delete_btn[lang])