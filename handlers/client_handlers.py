#general imports
from math import prod
import telegram

#aiogram imports
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text

#local imports
from start_bot import dp, bot
from keyboards import client_keyboards
from database import sqlite_db

async def see_catalog(message: types.Message):
    await message.answer('<b>Выберите категорию</b>', reply_markup=client_keyboards.mattresses_catalog, parse_mode=telegram.ParseMode.HTML)

async def choose_category_callback(callback_query: types.CallbackQuery):
    category = callback_query.data.replace('category_', '')
    print(category)
    products = await sqlite_db.read_products_raw()
    for product in products:
        if category in product[5]:
            await bot.send_photo(callback_query.from_user.id, product[1], 
            f'''
<b>{product[0]}</b>
Описание: {product[2]}
Цена: <s>{product[3]}</s> {float(product[3]) * (100 - float(product[4])) / 100} сом
            ''', 
            reply_markup=InlineKeyboardMarkup().row(InlineKeyboardButton(f'Оформить заказ', callback_data=f'choose {product[0]}'), InlineKeyboardButton('Написать консультанту', url='https://t.me/toktokozhoev')), parse_mode=telegram.ParseMode.HTML)
        await callback_query.answer()

async def choose_product_callback(callback_query: types.CallbackQuery):
    await callback_query.message.answer(f"Вы выбрали {callback_query.data.replace('choose ', '')}, наши консультанты свяжутся с вами в ближайщее время!")
    consultants = await sqlite_db.read_consultants()
    for consultant in consultants:
        await bot.send_message(chat_id=consultant[3], text=f"Здравствуйте, {consultant[1]}. {callback_query.from_user.full_name} хочет заказать  '{callback_query.data.replace('choose ', '')}'")


async def go_to_website(message: types.Message):
    await message.answer('<a href=\'ormatt.kg\'>Посетить оффициальный сайт</a>', parse_mode=telegram.ParseMode.HTML)

async def contact_consultant(message: types.Message):
    await message.answer('<a href=\'t.me/toktokozhoev\'>Связаться с консультантом</a>', parse_mode=telegram.ParseMode.HTML)

def register_client_handlers(dp: Dispatcher):
    dp.register_message_handler(see_catalog, Text(equals='Посмотреть каталог матрасов'))
    dp.register_message_handler(go_to_website, Text(equals='Посетить официальный сайт'))
    dp.register_message_handler(contact_consultant, Text(equals='Связаться с консультантом'))
    dp.register_callback_query_handler(choose_category_callback, Text(startswith='category'))
    dp.register_callback_query_handler(choose_product_callback, Text(startswith='choose'))