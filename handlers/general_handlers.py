#general imports
import os, dotenv, telegram

#aiogram imports
from aiogram import types, Dispatcher

#local imports
from keyboards import admin_keyboards, client_keyboards
from database import sqlite_db
from utils.classes import User

dotenv.load_dotenv()
admins = os.getenv('ADMINS')

async def start(message: types.Message):
    user = User(message.from_user.username, message.from_user.full_name, '0', message.from_user.id)

    if message.from_user.username is not None and message.from_user.username in admins:
        await message.answer(f'<b>Здравствуйте {message.from_user.username}, вы вошли как админ, добавьтесь к консультантам если не добовлялись используя команду /join_consultants</b>', reply_markup=admin_keyboards.admin_keyboard_upload, parse_mode=telegram.ParseMode.HTML)
        await sqlite_db.add_user(user, 'consultants')
    else:
        await message.answer(f'<b>Здравствуйте {message.from_user.username}, что надо?</b>', reply_markup=client_keyboards.client_keyboard_start, parse_mode=telegram.ParseMode.HTML)
        await sqlite_db.add_user(user, 'clients')

def register_general_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start', 'help'])