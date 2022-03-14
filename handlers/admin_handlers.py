#general imports 
import dotenv, os, telegram

#aiogram imports
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

#local imports
from keyboards import admin_keyboards
from database import sqlite_db
from start_bot import bot

admins = os.getenv('ADMINS')


class FSMAdmin(StatesGroup):
    name        = State()
    photo       = State()
    description = State()
    price       = State()
    discount    = State()
    categories  = State()

#Start of the Finite State Machine
#----------------------------------------------------------------------
async def start_fsm(message: types.Message):
    if message.from_user.username in admins:
        await FSMAdmin.name.set()
        await message.answer('Как называется матрас(аксессуар)?', reply_markup=admin_keyboards.admin_keyboard_cancel)

async def set_name(message: types.Message, state: FSMContext):
    if message.from_user.username in admins:
        async with state.proxy() as data: 
            data['name'] = message.text
        await FSMAdmin.next()
        await message.reply('Теперь загрузите фотографию!', reply_markup=admin_keyboards.admin_keyboard_cancel)

async def set_photo(message: types.Message, state: FSMContext):
    if message.from_user.username in admins:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.reply('Теперь напишите описание!', reply_markup=admin_keyboards.admin_keyboard_cancel)

async def set_description(message: types.Message, state: FSMContext):
    if message.from_user.username in admins:
        async with state.proxy() as data:
            data['description'] = message.text
        await FSMAdmin.next()
        await message.reply('Теперь укажите цену без скидки!', reply_markup=admin_keyboards.admin_keyboard_cancel)

async def set_price(message: types.Message, state: FSMContext):
    if message.from_user.username in admins:
        async with state.proxy() as data:
            data['price'] = message.text
        await FSMAdmin.next()
        await message.reply('Теперь укажите скидку!', reply_markup=admin_keyboards.admin_keyboard_cancel)

async def set_discount(message: types.Message, state: FSMContext):
    if message.from_user.username in admins:
        async with state.proxy() as data:
            data['discount'] = message.text
        await FSMAdmin.next()
        await message.reply('''
<b>Выберите категорию</b>
<code>'all' - Все матрасы</code>
<code>'dsc' - Матрасы со скидками</code>
<code>'chp' - Недорогие матрасы</code>
<code>'hvy' - Для тяжёлых людей</code>
<code>'hrd' - Жёсткие матрасы</code>
<code>'sft' - Мягкие матрасы</code>
<code>'kid' - Детские матрасы</code>
<code>'acs' - Аксессуары</code>
<b>Перечислите все категории через запятую 'dsc, sft, acs'</b>
        ''', parse_mode=telegram.ParseMode.HTML, reply_markup=admin_keyboards.admin_keyboard_cancel)
        
async def set_categories(message: types.Message, state: FSMContext):
    if message.from_user.username in admins:
        async with state.proxy() as data:
            data['categories'] = message.text
        await sqlite_db.add_product(state)
        await message.reply('Продукт успешно добавлен в базу данных!', reply_markup=admin_keyboards.admin_keyboard_upload)
        await state.finish()

async def cancel_upload(message: types.Message, state: FSMContext):
    if message.from_user.username in admins:
        curr_state = await state.get_state()
        if curr_state is None:
            return
        await state.finish()
        await message.reply('Загрузка успешно отменена!', reply_markup=admin_keyboards.admin_keyboard_upload)
#----------------------------------------------------------------------
#End of the Finite State Machine

#Deleting routine
async def delete_product(message: types.Message):
    if message.from_user.username in admins:
        products = await sqlite_db.read_products_raw()
        for product in products:
            await bot.send_photo(message.from_user.id, product[1], f'{product[0]}\nКатегории: {product[5]}', reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f'Удалить {product[0]}', callback_data=f'Delete {product[0]}')))

async def delete_callback_runner(callback_query: types.CallbackQuery):
    await sqlite_db.delete_product(callback_query.data.replace('Delete ', ''))
    await callback_query.answer(text=f"Вы успешно удалили {callback_query.data.replace('Delete ', '')}")

async def show_clients(message: types.Message):
    if message.from_user.username in admins:
        clients = await sqlite_db.read_clients()
        for i in range(len(clients)):
            await message.answer(f"{i+1} -> Name: {clients[i][1]}, USERNAME: {clients[i][0]}")

def register_admin_handlers(dp: Dispatcher):
    dp.register_message_handler(start_fsm, Text(equals='Загрузить'), state=None)
    dp.register_message_handler(cancel_upload, Text(equals='Отменить'), state='*')

    dp.register_message_handler(delete_product, Text(equals='Удалить'))
    dp.register_callback_query_handler(delete_callback_runner, Text(startswith='Delete'))

    dp.register_message_handler(set_name, state=FSMAdmin.name)
    dp.register_message_handler(set_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(set_description, state=FSMAdmin.description)
    dp.register_message_handler(set_price, state=FSMAdmin.price)
    dp.register_message_handler(set_discount, state=FSMAdmin.discount)
    dp.register_message_handler(set_categories, state=FSMAdmin.categories)

    dp.register_message_handler(show_clients, commands=['clients'])

