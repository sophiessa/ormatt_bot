#aiogram imports
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup



upload_btn = {
    'ru': KeyboardButton('Загрузить товар \U0001F4E5'),
    'en': KeyboardButton('Upload a product \U0001F4E5'),
    'kg': KeyboardButton('Товар жүктөө \U0001F4E5'),
}

delete_btn = {
    'ru': KeyboardButton('Удалить товар \U0001F4E4'),
    'en': KeyboardButton('Delete a product \U0001F4E4'),
    'kg': KeyboardButton('Товар жок кылуу \U0001F4E4'),
}

cancel_btn = {
    'ru': KeyboardButton('Отменить загрузку \U0000274C'),
    'en': KeyboardButton('Cancel \U0000274C'),
    'kg': KeyboardButton('Жокко чыгаруу \U0000274C'),
}

# join_btn = {
#     'ru': KeyboardButton('Добавиться к консультантам \U0000270A'),
#     'en': KeyboardButton('Join consultants \U0000270A'),
#     'kg': KeyboardButton('Менеджерлерге кошулуу \U0000270A'),
# }

post_btn = {
    'ru': KeyboardButton('Загрузить пост \U00002709'),
    'en': KeyboardButton('Post something \U00002709'),
    'kg': KeyboardButton('Пост чыгаруу \U00002709'),
}

change_language_btn = {
    'ru': KeyboardButton('Поменять язык \U00003297'),
    'en': KeyboardButton('Change the language \U00003297'),
    'kg': KeyboardButton('Тилди которуу \U00003297'),
}


def change_language_inline_keyboard():
    return InlineKeyboardMarkup().add(InlineKeyboardButton('КЫР', callback_data='Alanguage_kg'), InlineKeyboardButton('РУС', callback_data='Alanguage_ru'), InlineKeyboardButton('ENG', callback_data='Alanguage_en'))

def start_keyboard_markup(lang='ru'):
    return ReplyKeyboardMarkup(resize_keyboard=True).add(upload_btn[lang], delete_btn[lang]).add(post_btn[lang]).add(change_language_btn[lang])

def cancel_keyboard_markup(lang='ru'):
    return ReplyKeyboardMarkup(resize_keyboard=True).add(cancel_btn[lang])

def delete_product_inline_markup(product_name: str, lang='ru'):
    return {
        'ru': InlineKeyboardMarkup().add(InlineKeyboardButton(f'Удалить {product_name}', callback_data=f'Delete {product_name}')),
        'en': InlineKeyboardMarkup().add(InlineKeyboardButton(f'Delete {product_name}', callback_data=f'Delete {product_name}')),
        'kg': InlineKeyboardMarkup().add(InlineKeyboardButton(f'{product_name} өчүрүү', callback_data=f'Delete {product_name}')),
    }[lang]