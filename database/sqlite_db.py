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
    base.execute('CREATE TABLE IF NOT EXISTS clients(username TEXT, full_name TEXT, phone_number TEXT, chat_id TEXT, UNIQUE (chat_id) ON CONFLICT REPLACE)')
    base.execute('CREATE TABLE IF NOT EXISTS consultants(username TEXT, full_name TEXT, phone_number TEXT, chat_id TEXT, UNIQUE (chat_id) ON CONFLICT REPLACE)')
    base.commit()


#productdb
async def demo_add_product(data):
    cur.execute('INSERT INTO products VALUES (?, ?, ?, ?, ?, ?)', tuple(data))
    base.commit()

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
    cur.execute(f"REPLACE INTO {table} VALUES (?, ?, ?, ?)", (user.username, user.full_name, user.phone_number, user.chat_id))
    base.commit()

async def read_clients():
    return cur.execute('SELECT * FROM clients').fetchall()

async def read_consultants():
    return cur.execute('SELECT * FROM consultants').fetchall()

#utils 
async def populate_db():
    for i in range(1, 5):
        await demo_add_product((f'namedschrd{i}', 'AgACAgIAAxkBAAIMj2IutwPjSP27vI2RQOU0WYnt6NmUAAJ_tzEb2QABeEm86LlZdRk4OQEAAwIAA3MAAyME', f'description{i}', i*1000, i*10, 'all, dsc, hrd'))

    for i in range(1, 5):
        await demo_add_product((f'nameacskid{i}', 'AgACAgIAAxkBAAIMj2IutwPjSP27vI2RQOU0WYnt6NmUAAJ_tzEb2QABeEm86LlZdRk4OQEAAwIAA3MAAyME', f'description{i}', i*1000, i*10, 'all, acs, hvy'))