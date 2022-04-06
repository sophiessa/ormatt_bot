#general imports
import os, dotenv, telegram, json
from re import A

#aiogram imports
from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup

#local imports
from keyboards import admin_keyboards as akbs, client_keyboards as ckbs
from database import sqlite_db
from utils.classes import User
from texts.text import GeneralTexts as gts

#load .env
dotenv.load_dotenv()
admins = os.getenv('ADMINS')

async def start(message: types.Message):
    #Store the data of a user in a User object and save it to the database
    #TODO change language in the process
    chat_id       = message.from_user.id
    username      = message.from_user.username
    full_name     = message.from_user.full_name
    phone_number  = '0'
    is_admin      = message.from_user.username is not None and message.from_user.username in admins
    language_code = message.from_user.language_code
    receive_notifications = False

    user = User(chat_id=chat_id, username=username, full_name=full_name, phone_number=phone_number, is_admin=is_admin, language_code=language_code, receive_notifications=receive_notifications)

    await sqlite_db.add_a_user(user)
    #TODO get language code from the database not from the message | or think about it more
    if user.is_admin:
        upload_delete_keyboard = akbs.upload_delete_markup(user.language_code) #akbs is admin_keyboards
        text                   = gts.text_start_admin(user.language_code, user.full_name) #gts is GeneralTexts
        
        await message.answer(text=text, reply_markup=upload_delete_keyboard)
    else:
        start_keyboard = ckbs.start_markup(user.language_code) #ckbs is client_keyboards
        text           = gts.text_start_client(user.language_code, user.full_name)

        await message.answer(text=text, reply_markup=start_keyboard)

def register_general_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start',  'restart'])