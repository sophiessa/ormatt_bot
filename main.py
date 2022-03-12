#general imports
from start_bot import dp

#aiogram imports
from aiogram.utils import executor as ex


async def on_startup(_):
    print('ORMATT_BOT 2 IS RUNNING NOW!')

ex.start_polling(dp, on_startup=on_startup)