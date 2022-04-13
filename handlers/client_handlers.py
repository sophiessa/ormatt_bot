#general imports
import telegram, os, dotenv, time

#aiogram imports
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

#local imports
from start_bot import dp, bot
from keyboards import client_keyboards as ckbs, general_keyboards as gkbs
from database import sqlite_db
from utils.classes import User
from texts.text import ClientTexts as cts, AdminTexts as ats

#load .env
dotenv.load_dotenv()

managers = os.getenv('MANAGERS')

class FSMReview(StatesGroup):
    user       = State()
    user_id    = State()
    date       = State()
    review     = State()


class FSMBuyProduct(StatesGroup):   
    choice       = State()
    full_name    = State()
    phone_number = State()

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

#Display all the mattress categories
async def see_mattresses(message: types.Message):
    user = await sqlite_db.read_a_user(message)

    lang = message.from_user.language_code if user == None or user == [] else user[0][5]
    text = cts.see_mattress_category(lang)
    mat_cat_kb = ckbs.mattresses_catalog(lang)
    await message.answer(text=text, reply_markup=mat_cat_kb)

#Callback function to respond to a chosen mattress from 'see_mattresses'
async def choose_category_callback(callback_query: types.CallbackQuery):
    category = callback_query.data.replace('category_', '')
    products = await sqlite_db.read_products_raw()
    user = await sqlite_db.read_a_user(callback_query)

    lang = callback_query.from_user.language_code if user == None or user == [] else user[0][5]
    for product in products:
        categories = product[5].lower()
        if category in categories:
            product_inline_keyboard = ckbs.product_inline_keyboard(product[0], lang)
            text = cts.see_mattress(product[0], product[2], float(product[3]), float(product[4]), lang)
            photo_id = product[1]
            await bot.send_photo(user[0][0], photo_id, text, reply_markup=product_inline_keyboard)
            await callback_query.answer()

async def see_accessories(message: types.Message):
    category = 'acs'
    products = await sqlite_db.read_products_raw()
    user = await sqlite_db.read_a_user(message)

    lang = message.from_user.language_code if user == None or user == [] else user[0][5]
    for product in products:
        categories = product[5].lower()
        if category in categories:
            product_inline_keyboard = ckbs.product_inline_keyboard(product[0], lang)
            text = cts.see_accessory(product[0], product[2], float(product[3]), float(product[4]), lang)
            photo_id = product[1]
            await bot.send_photo(user[0][0], photo_id, text, reply_markup=product_inline_keyboard)

#BUY PRODUCT FST START
async def choose_product_callback(callback_query: types.CallbackQuery, state: FSMContext):
    user = await sqlite_db.read_a_user(callback_query)

    lang = callback_query.from_user.language_code if user == None or user == [] else user[0][5]
    product_name = callback_query.data.replace('choose_', '')
    text = cts.question_buyer_name(lang)
    cancel_buy_keyboard = ckbs.cancel_buy_markup(lang)

    await FSMBuyProduct.choice.set()
    async with state.proxy() as data:
        data['choice'] = product_name
    await FSMBuyProduct.next()

    await callback_query.message.answer(text=text, reply_markup=cancel_buy_keyboard)
    

async def set_buyer_name(message: types.Message, state: FSMContext):
    user = await sqlite_db.read_a_user(message)

    lang = message.from_user.language_code if user == None or user == [] else user[0][5]
    text = cts.question_buyer_phone_number(lang)
    # phone_number_buy_keyboard = ckbs.phone_number_buy_markup(lang)
    cancel_buy_keyboard = ckbs.cancel_buy_markup(lang)

    async with state.proxy() as data:
        data['full_name'] = message.text
        await sqlite_db.update_full_name(user[0][0], message.text)
    await FSMBuyProduct.next()
    await message.answer(text=text, reply_markup=cancel_buy_keyboard)

async def set_buyer_phone_number(message: types.Message, state: FSMContext):
    user = await sqlite_db.read_a_user(message)

    lang = message.from_user.language_code if user == None or user == [] else user[0][5]

    product_name = ''
    async with state.proxy() as data:
        data['phone_number'] = message.text
        await sqlite_db.update_phone_number(user[0][0], message.text)
        admins = await sqlite_db.read_admins()
        product_name = data['choice']
        for admin in admins:
            lang_a = admin[5]
            text = ats.order(user[0][1], data['full_name'], data['phone_number'], data['choice'], lang_a)
            await bot.send_message(chat_id=admin[0], text=text)

    text = cts.chosen_product(product_name, lang)
    start_keyboard = ckbs.start_markup(lang)
    await state.finish()
    await message.answer(text=text, reply_markup=start_keyboard)

async def cancel_buy(message: types.Message, state: FSMContext):
    user = await sqlite_db.read_a_user(message)

    lang = message.from_user.language_code if user == None or user == [] else user[0][5]
    text = cts.cancel_buy(lang)
    start_keyboard = ckbs.start_markup(lang)

    curr_state = state.get_state()
    if curr_state is None:
        return
    
    await state.finish()
    await message.answer(text=text, reply_markup=start_keyboard)



async def about_us(message: types.Message):
    user = await sqlite_db.read_a_user(message)

    lang = message.from_user.language_code if user == None or user == [] else user[0][5]
    text = cts.about_us(lang)
    website_link = ckbs.website_inline_keyboard(lang)
    await message.answer(text=text, reply_markup=website_link)


async def our_social_media(message: types.Message):
    user = await sqlite_db.read_a_user(message)

    lang = message.from_user.language_code if user == None or user == [] else user[0][5]
    text = cts.social_media(lang)
    social_media = ckbs.social_media_inline_keyboard(lang)
    await message.answer(text=text, reply_markup=social_media)

#'Leave a review' FSM beginning
async def leave_a_review_start(message: types.Message):
    user = await sqlite_db.read_a_user(message)

    lang = message.from_user.language_code if user == None or user == [] else user[0][5]
    text = cts.review_question_name(lang)
    cancel_keyboard = ckbs.leave_a_review_cancel(lang)
    await FSMReview.user.set()
    await message.answer(text=text, reply_markup=cancel_keyboard)
#set states one by one, skip (id, date)
async def set_review_user(message: types.Message, state: FSMContext):
    user = await sqlite_db.read_a_user(message)

    lang = message.from_user.language_code if user == None or user == [] else user[0][5]
    text = cts.review_question_review(lang)
    cancel_keyboard = ckbs.leave_a_review_cancel(lang)
    async with state.proxy() as data:
        data['user']    = message.text
        data['user_id'] = message.from_user.id
        t = time.localtime()
        data['date']    = f'{t[0]}/{t[1]}/{t[2]} | {t[3]}:{t[4]}'
    await FSMReview.next()
    await FSMReview.next()
    await FSMReview.next()
    await message.answer(text=text, reply_markup=cancel_keyboard)

async def set_review_review(message: types.Message, state: FSMContext):
    user = await sqlite_db.read_a_user(message)
   
    lang = message.from_user.language_code if user == None or user == [] else user[0][5]
    text = cts.review_end(lang)
    start_keyboard = ckbs.start_markup(lang)
    async with state.proxy() as data:
        data['review']    = message.text
    await sqlite_db.add_a_review(state)
    await message.reply(text=text, reply_markup=start_keyboard)
    await state.finish()
#cancel review if needed
async def cancel_review(message: types.Message, state: FSMContext):
    user = await sqlite_db.read_a_user(message)

    lang = message.from_user.language_code if user == None or user == [] else user[0][5]
    text = cts.review_cancel(lang)
    start_keyboard = ckbs.start_markup(lang)
    curr_state = await state.get_state()
    if curr_state is None:
        return
    await state.finish()
    await message.reply(text=text, reply_markup=start_keyboard)
#End of 'Leave a review' FSM

async def see_reviews(message: types.Message):
    reviews = await sqlite_db.see_reviews()
    for review in reviews:
        await message.answer(f'ID: {str(review[1])[:4]}\n{review[2]}\n<b>{review[3]}</b>')


async def change_language(message: types.Message):
    change_language_inline_keyboard = ckbs.change_language_inline_keyboard()
    await message.answer(text='Выберите язык!\nСhoose a language!\nТил танданыз!', reply_markup=change_language_inline_keyboard)

async def change_language_callback(callback_query: types.CallbackQuery):
    lang = callback_query.data.replace('language_', '')
    text = cts.change_language(lang)
    await sqlite_db.update_language(callback_query.from_user.id, lang)
    await callback_query.message.answer(text=text, reply_markup=ckbs.start_markup(lang))
    await callback_query.answer()

async def receive_notifications(message: types.Message):
    user = await sqlite_db.read_a_user(message)

    lang = message.from_user.language_code if user == None or user == [] else user[0][5]
    text = cts.receive_notifications(lang)
    receive_yes_no_keyboard = ckbs.receive_notifications_yes_not_markup(lang)
    await message.answer(text=text, reply_markup=receive_yes_no_keyboard)

async def receive_notifications_callback(callback_query: types.CallbackQuery):
    user = await sqlite_db.read_a_user(callback_query)

    lang = callback_query.from_user.language_code if user == None or user == [] else user[0][5]
    receive = callback_query.data.replace('receive_notifications_', '')
    text = cts.receive_notification_yes_no(receive, lang)
    start_keyboard = ckbs.start_markup(lang)
    await sqlite_db.update_receive_notifications(user[0][0], int(receive))
    await callback_query.message.answer(text=text, reply_markup=start_keyboard)
    await callback_query.answer('Updated')
    


async def contact_consultant(message: types.Message):
    await message.answer('<b>https://t.me/toktokozhoev</b>', parse_mode=telegram.ParseMode.HTML)

def register_client_handlers(dp: Dispatcher):
    #show mattresses
    dp.register_message_handler(see_mattresses, Text(contains='\U0001F6CF'))
    dp.register_callback_query_handler(choose_category_callback, Text(startswith='category_'))

    #show accessories
    dp.register_message_handler(see_accessories, Text(contains='\U0001F45C'))

    #start buy product fsm
    dp.register_callback_query_handler(choose_product_callback, Text(startswith='choose_'), state=None)
    dp.register_message_handler(cancel_buy, Text(contains='\U0001F554'), state='*')
    dp.register_message_handler(set_buyer_name, state=FSMBuyProduct.full_name)
    dp.register_message_handler(set_buyer_phone_number, state=FSMBuyProduct.phone_number)
    
    
    
    #start a review fsm
    dp.register_message_handler(leave_a_review_start, Text(contains='\U0001F4DD'), state=None)
    dp.register_message_handler(cancel_review, Text(contains='\U0001F555'), state='*')
    dp.register_message_handler(set_review_user, state=FSMReview.user)
    dp.register_message_handler(set_review_review, state=FSMReview.review)
    #end review fsm

    #see the reviews
    dp.register_message_handler(see_reviews, Text(contains='\U0001F4D6'))

    #show about us page
    dp.register_message_handler(about_us, Text(contains='\U0001F4F0'))
    #show social media
    dp.register_message_handler(our_social_media, Text(contains='\U0001F4E8'))
    #change language
    dp.register_message_handler(change_language, Text(contains='\U0001F524'))
    dp.register_callback_query_handler(change_language_callback, Text(startswith='language_'))
    #receive notifications
    dp.register_message_handler(receive_notifications, Text(contains='\U0001F523'))
    dp.register_callback_query_handler(receive_notifications_callback, Text(startswith='receive_notifications_'))
    