#general imports

#aiogram imports
from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, ReplyKeyboardRemove

#local imports


all_mattresses = InlineKeyboardButton('Все матрасы \U0001F30D', callback_data='category_all')
big_discount_mattresses = InlineKeyboardButton('Матрасы со скидками \U0001F4B2', callback_data='category_dsc')
cheap_mattresses = InlineKeyboardButton('Недорогие матрасы \U0001F495', callback_data='category_chp')
heavy_mattresses = InlineKeyboardButton('Для тяжёлых людей \U0001F62C', callback_data='category_hvy')
hard_mattresses = InlineKeyboardButton('Жёсткие матрасы \U0001F5FF', callback_data='category_hrd')
soft_mattresses = InlineKeyboardButton('Мягкие матрасы \U0001F607', callback_data='category_sft')
kid_mattresses = InlineKeyboardButton('Детские матрасы \U0001F476', callback_data='category_kid')
accessories = InlineKeyboardButton('Аксессуары \U0001F492', callback_data='category_acs')
mattresses_catalog = InlineKeyboardMarkup().add(all_mattresses).add(big_discount_mattresses).add(cheap_mattresses).add(heavy_mattresses).add(hard_mattresses).add(soft_mattresses).add(kid_mattresses).add(accessories)