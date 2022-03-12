#general imports 
import dotenv, os

#aiogram imports 
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

dotenv.load_dotenv()

token   = os.getenv('TOKEN')
storage = MemoryStorage()


bot = Bot(token=token)
dp  = Dispatcher(bot, storage=storage)