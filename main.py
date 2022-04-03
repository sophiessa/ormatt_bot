#general imports
import dotenv

#aiogram imports
from aiogram.utils import executor as ex

#local imports 
from start_bot import dp, bot
from handlers import admin_handlers, general_handlers, client_handlers
from database import sqlite_db


async def on_startup(_):
    sqlite_db.start_database()
    print('ormatt_bot is up........')

async def on_shutdown(_):
    bot.close()



admin_handlers.register_admin_handlers(dp)
general_handlers.register_general_handlers(dp)
client_handlers.register_client_handlers(dp)

ex.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)