#aiogram imports
from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, ReplyKeyboardRemove



def start_markup(lang='ru'):
    mattresses_btn = {
        'ru': KeyboardButton('Матрасы \U0001F6CF'),
        'en': KeyboardButton('Mattresses \U0001F6CF'),
        'kg': KeyboardButton('Матрацтар \U0001F6CF'),
    } #display inline buttons with mattresses' categories

    accessories_btn = {
        'ru': KeyboardButton('Аксессуары \U0001F45C'),
        'en': KeyboardButton('Accessories \U0001F45C'),
        'kg': KeyboardButton('Аксессуарлар \U0001F45C'),
    } #display accessories
    about_us_btn = {
        'ru': KeyboardButton('О нас  \U0001F4F0'),
        'en': KeyboardButton('About Us  \U0001F4F0'),
        'kg': KeyboardButton('Биз жөнүндө  \U0001F4F0'),
    } #send about us text and a website link
    social_media_btn = {
        'ru': KeyboardButton('Мы в социальных сетях \U0001F4E8'),
        'en': KeyboardButton('Our social media \U0001F4E8'),
        'kg': KeyboardButton('Биздин социалдык тармактар \U0001F4E8'),
    } #send another markup with social media links
    leave_review_btn = {
        'ru': KeyboardButton('Оставить отзыв \U0001F4DD'),
        'en': KeyboardButton('Leave a review \U0001F4DD'),
        'kg': KeyboardButton('Пикир калтыруу \U0001F4DD'),
    } #ask for a review in an FSM and store it
    reviews_btn = {
        'ru': KeyboardButton('Отзывы \U0001F4D6'),
        'en': KeyboardButton('Reviews \U0001F4D6'),
        'kg': KeyboardButton('Пикирлер \U0001F4D6'),
    } #shows available reviews
    change_language_btn = {
        'ru': KeyboardButton('Поменять язык \U0001F524'),
        'en': KeyboardButton('Change language \U0001F524'),
        'kg': KeyboardButton('Тилди өзгөртүү \U0001F524'),
    } #shows abailable languages
    receive_notifications_btn = {
        'ru': KeyboardButton('Получать сообщения о скидках \U0001F523'),
        'en': KeyboardButton('Receive notifications about discounts \U0001F523'),
        'kg': KeyboardButton('Арзандатуулар жөнүндө информация билип туруу \U0001F523'),
    }
    return ReplyKeyboardMarkup(resize_keyboard=True).add(mattresses_btn[lang], accessories_btn[lang]).add(about_us_btn[lang]).add(social_media_btn[lang]).add(leave_review_btn[lang], reviews_btn[lang], change_language_btn[lang]).add(receive_notifications_btn[lang])

def mattresses_catalog(lang='ru'):
    #The following inline buttons show up when 'see_mattrasses' is called
    all_mattresses = {
        'ru': InlineKeyboardButton('Все матрасы \U0001F30D',         callback_data='category_all'),
        'en': InlineKeyboardButton('All the mattresses \U0001F30D',         callback_data='category_all'),
        'kg': InlineKeyboardButton('Бардык матрацтар \U0001F30D',         callback_data='category_all'),
    }
    big_discount_mattresses = {
        'ru': InlineKeyboardButton('Матрасы со скидками \U0001F4B2', callback_data='category_dsc'),
        'en': InlineKeyboardButton('Discounted Mattresses \U0001F4B2', callback_data='category_dsc'),
        'kg': InlineKeyboardButton('Арзандатуулар менен матрацтар \U0001F4B2', callback_data='category_dsc'),
    }
    cheap_mattresses = {
        'ru': InlineKeyboardButton('Недорогие матрасы \U0001F495',   callback_data='category_chp'),
        'en': InlineKeyboardButton('Inexpensive mattresses \U0001F495',   callback_data='category_chp'),
        'kg': InlineKeyboardButton('Арзан матрацтар \U0001F495',   callback_data='category_chp'),
    }
    heavy_mattresses = {
        'ru': InlineKeyboardButton('Для тяжёлых людей \U0001F62C',   callback_data='category_hvy'),
        'en': InlineKeyboardButton('For heavy people \U0001F62C',   callback_data='category_hvy'),
        'kg': InlineKeyboardButton('Оор адамдар үчүн \U0001F62C',   callback_data='category_hvy'),
    }
    hard_mattresses = {
        'ru': InlineKeyboardButton('Жёсткие матрасы \U0001F5FF',     callback_data='category_hrd'),
        'en': InlineKeyboardButton('Hard mattresses \U0001F5FF',     callback_data='category_hrd'),
        'kg': InlineKeyboardButton('Катуу матрацтар \U0001F5FF',     callback_data='category_hrd'),
    }
    soft_mattresses = {
        'ru': InlineKeyboardButton('Мягкие матрасы \U0001F607',      callback_data='category_sft'),
        'en': InlineKeyboardButton('Soft mattresses \U0001F607',      callback_data='category_sft'),
        'kg': InlineKeyboardButton('Жумшак матрацтар \U0001F607',      callback_data='category_sft'),
    }
    kid_mattresses = {
        'ru': InlineKeyboardButton('Детские матрасы \U0001F476',     callback_data='category_kid'),
        'en': InlineKeyboardButton('Kid mattresses \U0001F476',     callback_data='category_kid'),
        'kg': InlineKeyboardButton('Балдар үчүн матрацтар \U0001F476',     callback_data='category_kid'),
    }
    return InlineKeyboardMarkup().add(all_mattresses[lang]).add(big_discount_mattresses[lang]).add(cheap_mattresses[lang]).add(heavy_mattresses[lang]).add(kid_mattresses[lang]).add(hard_mattresses[lang], soft_mattresses[lang])

def product_inline_keyboard(product_name: str, lang='ru'):
    place_order = {
        'ru': InlineKeyboardButton('Оформить заказ', callback_data=f'choose_{product_name}'),
        'en': InlineKeyboardButton('Place an order', callback_data=f'choose_{product_name}'),
        'kg': InlineKeyboardButton('Заказ кылуу', callback_data=f'choose_{product_name}'),
    }

    text_manager = {
        'ru': InlineKeyboardButton('Написать консультанту', url='https://t.me/toktokozhoev'),
        'en': InlineKeyboardButton('Text a manager', url='https://t.me/toktokozhoev'),
        'kg': InlineKeyboardButton('Менеджерге жазуу', url='https://t.me/toktokozhoev'),
    }

    return InlineKeyboardMarkup().row(place_order[lang], text_manager[lang])

def website_inline_keyboard(lang='ru'):
    website_link_button = {
        'ru': InlineKeyboardButton('Перейти на сайт', url='https://www.ormatt.kg/'),
        'en': InlineKeyboardButton('Go to the website', url='https://www.ormatt.kg/'),
        'kg': InlineKeyboardButton('Сайтка шилтеме', url='https://www.ormatt.kg/'),
    }
    return InlineKeyboardMarkup().add(website_link_button[lang])

def social_media_inline_keyboard(lang='ru'):
    instagram_inline_btn = {
        'ru': InlineKeyboardButton(text='Инстаграм',         url='https://www.instagram.com/ormatt.kg'),
        'en': InlineKeyboardButton(text='Instagram',         url='https://www.instagram.com/ormatt.kg'),
        'kg': InlineKeyboardButton(text='Инстаграм',         url='https://www.instagram.com/ormatt.kg'),
    }
    facebook_inline_btn = {
        'ru': InlineKeyboardButton(text='Фейсбук',           url='https://www.facebook.com/ormattmattresses/'),
        'en': InlineKeyboardButton(text='Facebook',           url='https://www.facebook.com/ormattmattresses/'),
        'kg': InlineKeyboardButton(text='Фейсбук',           url='https://www.facebook.com/ormattmattresses/'),
    }
    email_inline_btn = {
        'ru': InlineKeyboardButton(text='E-mail \U0001F4E7', url='mailto:ormatt.kg@gmail.com'),
        'en': InlineKeyboardButton(text='E-mail \U0001F4E7', url='mailto:ormatt.kg@gmail.com'),
        'kg': InlineKeyboardButton(text='E-mail \U0001F4E7', url='mailto:ormatt.kg@gmail.com'),
    }

    return InlineKeyboardMarkup().add(instagram_inline_btn[lang]).add(facebook_inline_btn[lang]).add(email_inline_btn[lang])

def change_language_inline_keyboard():
    return InlineKeyboardMarkup().add(InlineKeyboardButton('КЫР', callback_data='language_kg'), InlineKeyboardButton('РУС', callback_data='language_ru'), InlineKeyboardButton('ENG', callback_data='language_en'))

def leave_a_review_cancel(lang='ru'):
    cancel = {
        'ru': KeyboardButton('Отмена \U0001F555'),
        'en': KeyboardButton('Cancel \U0001F555'),
        'kg': KeyboardButton('Жокко чыгаруу \U0001F555'),
    }
    return ReplyKeyboardMarkup(resize_keyboard=True).add(cancel[lang])

def cancel_buy_markup(lang='ru'):
    cancel = {
        'ru': KeyboardButton('Отмена \U0001F554'),
        'en': KeyboardButton('Cancel \U0001F554'),
        'kg': KeyboardButton('Жокко чыгаруу \U0001F554'),
    }
    return ReplyKeyboardMarkup(resize_keyboard=True).add(cancel[lang])

def phone_number_buy_markup(lang='ru'):
    text = {
        'ru': KeyboardButton('Номер', request_contact=True),
        'en': KeyboardButton('Number', request_contact=True),
        'kg': KeyboardButton('Номер', request_contact=True),
    }
    return ReplyKeyboardMarkup(resize_keyboard=True).add(text[lang])

def receive_notifications_yes_not_markup(lang='ru'):
    yes = {
        'ru': InlineKeyboardButton('Да', callback_data='receive_notifications_1'),
        'en': InlineKeyboardButton('Yes', callback_data='receive_notifications_1'),
        'kg': InlineKeyboardButton('Ооба', callback_data='receive_notifications_1'),
    }

    no = {
        'ru': InlineKeyboardButton('Нет', callback_data='receive_notifications_0'),
        'en': InlineKeyboardButton('No', callback_data='receive_notifications_0'),
        'kg': InlineKeyboardButton('Жок', callback_data='receive_notifications_0'),
    }

    return InlineKeyboardMarkup().add(yes[lang], no[lang])

contact_link_button = InlineKeyboardButton('Написать консультанту', url='https://www.t.me/toktokozhoev')
contact_markup = InlineKeyboardMarkup().add(contact_link_button)