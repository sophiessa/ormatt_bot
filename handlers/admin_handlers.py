#general imports 
import dotenv, os, telegram

#aiogram imports
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

#local imports
from keyboards import admin_keyboards as akbs, general_keyboards as gkbs
from database import sqlite_db
from start_bot import bot
from texts.text import AdminTexts as ats

admins = os.getenv('ADMINS')


class FSMAdmin(StatesGroup):
    name        = State()
    photo       = State()
    description = State()
    price       = State()
    discount    = State()
    categories  = State()

class FSMPost(StatesGroup):
    title = State()
    text  = State()

"""
user
0 - chat_id
1 - username
2 - full_name
3 - phone_number
4 - is_admin
5 - language_code
6 - receive_notifications
"""


#Start of the Finite State Machine
#----------------------------------------------------------------------
async def start_fsm(message: types.Message):
    user = await sqlite_db.read_a_user(message)

    lang = message.from_user.language_code if user == None or user == [] else user[0][5]
    if int(user[0][4]):
        await FSMAdmin.name.set()
        text = ats.upload_product_name(lang)
        cancel_keyboard = akbs.cancel_keyboard_markup(lang)
        await message.answer(text=text, reply_markup=cancel_keyboard)

async def set_name(message: types.Message, state: FSMContext):
    user = await sqlite_db.read_a_user(message)

    lang = message.from_user.language_code if user == None or user == [] else user[0][5]
    if int(user[0][4]):
        async with state.proxy() as data: 
            data['name'] = message.text
        await FSMAdmin.next()
        cancel_keyboard = akbs.cancel_keyboard_markup(lang)
        text = ats.upload_product_photo(lang)
        await message.reply(text=text, reply_markup=cancel_keyboard)

async def set_photo(message: types.Message, state: FSMContext):
    user = await sqlite_db.read_a_user(message)

    lang = message.from_user.language_code if user == None or user == [] else user[0][5]
    if int(user[0][4]):
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMAdmin.next()
        cancel_keyboard = akbs.cancel_keyboard_markup(lang)
        text = ats.upload_product_description(lang)
        await message.reply(text=text, reply_markup=cancel_keyboard)

async def set_description(message: types.Message, state: FSMContext):
    user = await sqlite_db.read_a_user(message)

    lang = message.from_user.language_code if user == None or user == [] else user[0][5]
    if int(user[0][4]):
        async with state.proxy() as data:
            data['description'] = message.text
        await FSMAdmin.next()
        cancel_keyboard = akbs.cancel_keyboard_markup(lang)
        text = ats.upload_product_price(lang)
        await message.reply(text=text, reply_markup=cancel_keyboard)

async def set_price(message: types.Message, state: FSMContext):
    user = await sqlite_db.read_a_user(message)

    lang = message.from_user.language_code if user == None or user == [] else user[0][5]
    if int(user[0][4]):
        async with state.proxy() as data:
            data['price'] = message.text
        await FSMAdmin.next()
        cancel_keyboard = akbs.cancel_keyboard_markup(lang)
        text = ats.upload_product_discount(lang)
        await message.reply(text=text, reply_markup=cancel_keyboard)

async def set_discount(message: types.Message, state: FSMContext):
    user = await sqlite_db.read_a_user(message)

    lang = message.from_user.language_code if user == None or user == [] else user[0][5]
    if int(user[0][4]):
        async with state.proxy() as data:
            data['discount'] = message.text
        await FSMAdmin.next()
        cancel_keyboard = akbs.cancel_keyboard_markup(lang)
        text = ats.upload_product_category(lang)
        await message.reply(text=text, reply_markup=cancel_keyboard)
        
async def set_categories(message: types.Message, state: FSMContext):
    user = await sqlite_db.read_a_user(message)

    lang = message.from_user.language_code if user == None or user == [] else user[0][5]
    if int(user[0][4]):
        async with state.proxy() as data:
            data['categories'] = message.text
        await sqlite_db.add_a_product(state)
        general_keyboard = akbs.start_keyboard_markup(lang)
        text = ats.upload_product_success(lang)
        await message.reply(text=text, reply_markup=general_keyboard)
        await state.finish()

async def cancel_upload(message: types.Message, state: FSMContext):
    user = await sqlite_db.read_a_user(message)

    lang = message.from_user.language_code if user == None or user == [] else user[0][5]
    if int(user[0][4]):
        curr_state = await state.get_state()
        if curr_state is None:
            return
        general_keyboard = akbs.start_keyboard_markup(lang)
        text = ats.upload_product_cancel(lang)
        await state.finish()
        await message.reply(text=text, reply_markup=general_keyboard)
#----------------------------------------------------------------------
#End of the Finite State Machine

#Deleting routine
async def delete_product(message: types.Message):
    user = await sqlite_db.read_a_user(message)

    lang = message.from_user.language_code if user == None or user == [] else user[0][5]
    if int(user[0][4]):
        products = await sqlite_db.read_products_raw()
        for product in products:
            text = ats.delete_product(product[0], product[5], lang)
            delete_product_inline_keyboard = akbs.delete_product_inline_markup(product[0], lang)
            photo_id = product[1]
            await bot.send_photo(user[0][0], photo_id, text, reply_markup=delete_product_inline_keyboard)

async def delete_callback_runner(callback_query: types.CallbackQuery):
    user = await sqlite_db.read_a_user(callback_query)

    lang = callback_query.from_user.language_code if user == None or user == [] else user[0][5]
    await sqlite_db.delete_a_product(callback_query.data.replace('Delete ', ''))
    text = ats.delete_product_callback(callback_query.data.replace('Delete ', ''), lang)
    await callback_query.message.answer(text=text)

#Start posting fsm
async def post_notification(message: types.Message):
    user = await sqlite_db.read_a_user(message)

    lang = message.from_user.language_code if user == None or user == [] else user[0][5]
    if int(user[0][4]):
        await FSMPost.title.set()
        text = ats.set_post_title(lang)
        cancel_post = akbs.cancel_keyboard_markup(lang)
        await message.answer(text=text, reply_markup=cancel_post)

async def set_title(message: types.Message, state: FSMContext):
    user = await sqlite_db.read_a_user(message)

    lang = message.from_user.language_code if user == None or user == [] else user[0][5]
    if int(user[0][4]):
        async with state.proxy() as data:
            data['title'] = message.text
        await FSMPost.next()
        text = ats.set_post_text(lang)
        cancel_post = akbs.cancel_keyboard_markup(lang)
        await message.answer(text=text, reply_markup=cancel_post)

async def set_text(message: types.Message, state: FSMContext):
    user = await sqlite_db.read_a_user(message)
    users = await sqlite_db.read_users()
    lang = message.from_user.language_code if user == None or user == [] else user[0][5]
    if int(user[0][4]):
        async with state.proxy() as data:
            for u in users:
                await bot.send_message(chat_id=u[0], text=f"<b>{data['title']}</b>\n{message.text}")
    
    cancel_post = akbs.cancel_keyboard_markup(lang)
    await state.finish()
    await message.answer('\U00002705', reply_markup=cancel_post)

async def cancel_post(message: types.Message, state: FSMContext):
    curr_state = state.get_state()
    if curr_state is None:
        return
    user = await sqlite_db.read_a_user(message)
    lang = message.from_user.language_code if user == None or user == [] else user[0][5]
    if int(user[0][4]):
        state.finish()
        await message.answer('\U00002716')
#END POSTIMG FSM

async def change_language(message: types.Message):
    change_language_inline_keyboard = akbs.change_language_inline_keyboard()
    await message.answer(text='Выберите язык!\nСhoose a language!\nТил танданыз!', reply_markup=change_language_inline_keyboard)

async def change_language_callback(callback_query: types.CallbackQuery):
    lang = callback_query.data.replace('Alanguage_', '')
    text = ats.change_language(lang)
    await sqlite_db.update_language(callback_query.from_user.id, lang)
    await callback_query.message.answer(text=text, reply_markup=akbs.start_keyboard_markup(lang))
    await callback_query.answer()

async def show_stats(message: types.Message):
    user = await sqlite_db.read_a_user(message)
    lang = message.from_user.language_code if user == None or user == [] else user[0][5]
    number_of_users = await sqlite_db.number_of_users()
    if int(user[0][4]):
        await message.reply(f'# of users: {number_of_users[0][0]}')

def register_admin_handlers(dp: Dispatcher):
    dp.register_message_handler(start_fsm, Text(contains='\U0001F4E5'), state=None)
    dp.register_message_handler(cancel_upload, Text(contains='\U0000274C'), state='*')

    dp.register_message_handler(delete_product, Text(contains='\U0001F4E4'))
    dp.register_callback_query_handler(delete_callback_runner, Text(startswith='Delete'))

    dp.register_message_handler(set_name, state=FSMAdmin.name)
    dp.register_message_handler(set_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(set_description, state=FSMAdmin.description)
    dp.register_message_handler(set_price, state=FSMAdmin.price)
    dp.register_message_handler(set_discount, state=FSMAdmin.discount)
    dp.register_message_handler(set_categories, state=FSMAdmin.categories)

    dp.register_message_handler(cancel_post, Text(contains='\U0000274C'), state='*')
    dp.register_message_handler(post_notification, Text(contains='\U00002709'), state=None)
    dp.register_message_handler(set_title, state=FSMPost.title)
    dp.register_message_handler(set_text, state=FSMPost.text)


    dp.register_message_handler(change_language, Text(contains='\U00003297'))
    dp.register_callback_query_handler(change_language_callback, Text(startswith='Alanguage_'))

    dp.register_message_handler(show_stats, commands=['stats'])

    # dp.register_message_handler(show_clients, commands=['clients'])

