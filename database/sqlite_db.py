#general imports 
import sqlite3

#aiogram imports
from aiogram import types

#local imports
from start_bot import bot
from utils.classes import User


def start_products_database():
    global base_product, cur_product

    base_product = sqlite3.connect('database/products.db')
    cur_product  = base_product.cursor()

    if base_product:
        print('connected to the products.db.........')
    
    base_product.execute('CREATE TABLE IF NOT EXISTS products(name TEXT, photo TEXT, description TEXT, price TEXT, discount TEXT, categories TEXT)')
    base_product.commit()


def start_users_database():
    global base_user, cur_user

    base_user = sqlite3.connect('database/users.db')
    cur_user  = base_user.cursor()

    if base_user:
        print('connected to the users.db...........')
    
    base_user.execute('CREATE TABLE IF NOT EXISTS users (chat_id TEXT, username TEXT, full_name TEXT, phone_number TEXT, is_admin TEXT, language_code TEXT, receive_notifications INTEGER, UNIQUE (chat_id) ON CONFLICT REPLACE)')
    base_user.commit()

def start_reviews_database():
    global base_review, cur_review

    base_review = sqlite3.connect('database/reviews.db')
    cur_review  = base_review.cursor()

    if base_review:
        print('connected to the reviews.db...........')

    base_review.execute('CREATE TABLE IF NOT EXISTS reviews (user TEXT, user_id INTEGET, date TEXT, review TEXT)')
    base_review.commit()

# def start_posts_database():
#     global base_post, cur_post

#     base_post = sqlite3.connect('database/posts.db')
#     cur_post  = base_post.cursor()

#     if base_post:
#         print('connected to the posts.db...........')

#     base_post.execute('CREATE TABLE IF NOT EXISTS posts (user TEXT, date TEXT, text TEXT)')
#     base_post.commit()

#products.db
async def add_a_product(state):
    async with state.proxy() as data:
        cur_product.execute('INSERT INTO products VALUES (?, ?, ?, ?, ?, ?)', tuple(data.values()))
        base_product.commit()

async def delete_a_product(name):
    cur_product.execute('DELETE FROM products WHERE name == ?', (name,))
    base_product.commit()

async def read_products_raw():
    return cur_product.execute('SELECT * FROM products').fetchall()

#users.db
async def add_a_user(user: User):
    cur_user.execute(f'INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?)', (user.chat_id, user.username, user.full_name, user.phone_number, user.is_admin, user.language_code, user.recieve_notifications))
    base_user.commit()

async def delete_a_user(chat_id):
    cur_user.execute(f'DELETE FROM users WHERE chat_id == {chat_id}').fetchall()
    base_user.commit()

async def read_a_user(chat_id):
    return cur_user.execute(f'SELECT * FROM users WHERE chat_id == {chat_id}').fetchall()

async def read_admins():
    return cur_user.execute(f'SELECT * FROM users WHERE is_admin == 1').fetchall()

async def update_language(chat_id, new_language):
    cur_user.execute(f'UPDATE users SET language_code = "{new_language}" WHERE chat_id == {chat_id}')
    base_user.commit()

async def update_phone_number(chat_id, new_phone_number):
    cur_user.execute(f'UPDATE users SET phone_number = "{new_phone_number}" WHERE chat_id == {chat_id}')
    base_user.commit()

async def update_full_name(chat_id, new_full_name):
    cur_user.execute(f'UPDATE users SET full_name = "{new_full_name}" WHERE chat_id == {chat_id}')
    base_user.commit()

async def update_receive_notifications(chat_id, new_receive):
    cur_user.execute(f'UPDATE users SET receive_notifications = "{new_receive}" WHERE chat_id == {chat_id}')
    base_user.commit()


#reviews.db
async def add_a_review(state):
    async with state.proxy() as data:
        cur_review.execute('INSERT INTO reviews VALUES (?, ?, ?, ?)', tuple(data.values()))
        base_review.commit()

async def see_reviews():
    return cur_review.execute('SELECT * FROM reviews').fetchall()


#TODO look into databases, put something else instead of PRIMARY KEY