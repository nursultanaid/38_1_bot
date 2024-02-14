import sqlite3
from aiogram import types, Dispatcher
from config import bot
from database import bot_db
from keyboards import start_inline_button
import const

async def start_button(message: types.Message):
    print(message)
    db = bot_db.BotDB()
    db.sql_insert_user(
        tg_id=message.from_user.id,
        username=message.from_user.username,
        lastname=message.from_user.last_name,
        firstname=message.from_user.first_name
    )

    await bot.send_message(
        chat_id=message.from_user.id,
        text=const.START_MENU_TEXT.format(
            user=message.from_user.first_name
        ),
        reply_markup=await start_inline_button.start_keyboard()
    )
    return


def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(
        start_button,
        commands=['start']
    )