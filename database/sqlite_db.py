#general imports 
import sqlite3

#aiogram imports
from aiogram import types

#local imports
from start_bot import bot
from utils.classes import User


def start_database():
    global base, cur

    base = sqlite3.connect('database/main.db')
    cur  = base.cursor()

    if base:
        print('Connected to the main.db')
    
    base.execute('CREATE TABLE IF NOT EXISTS products(name TEXT, photo TEXT, description TEXT, price TEXT, discount TEXT, categories TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS clients(username TEXT, full_name TEXT, phone_number TEXT, chat_id TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS consultants(username TEXT, full_name TEXT, phone_number TEXT, chat_id TEXT)')
    base.commit()


#productdb
async def add_product(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO products VALUES (?, ?, ?, ?, ?, ?)', tuple(data.values()))
        base.commit()

async def delete_product(name):
    cur.execute('DELETE FROM products WHERE name == ?', (name,))
    base.commit()

async def read_products_raw():
    return cur.execute('SELECT * FROM products').fetchall()

#userdb
async def add_user(user: User, table):
    async with user.as_dict() as u:
        cur.execute(f"INSERT INTO {table} VALUES {u['username'], u['full_name'], u['phone_number'], u['chat_id']}")
        base.commit()