#general imports 
import dotenv, os

#aiogram imports 
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

dotenv.load_dotenv()

token   = os.getenv('TOKEN')
storage = MemoryStorage()


bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp  = Dispatcher(bot, storage=storage)