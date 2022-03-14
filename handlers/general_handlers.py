#general imports
import os, dotenv, telegram

#aiogram imports
from aiogram import types, Dispatcher

#local imports
from keyboards import admin_keyboards

dotenv.load_dotenv()
admins = os.getenv('ADMINS')

async def start(message: types.Message):
    if message.from_user.username is not None and message.from_user.username in admins:
        await message.answer(f'<b>Здравствуйте {message.from_user.username}, вы вошли как админ, добавьтесь к консультантам если не добовлялись используя команду /join_consultants</b>', reply_markup=admin_keyboards.admin_keyboard_upload, parse_mode=telegram.ParseMode.HTML)
    else:
        await message.answer(f'<b>Здравствуйте {message.from_user.username}, что надо?</b>', parse_mode=telegram.ParseMode.HTML)

def register_general_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])