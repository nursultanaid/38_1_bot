import sqlite3
from aiogram import types, Dispatcher
from aiogram.utils.deep_linking import _create_link
from config import bot, MEDIA_DESTINATION
from database import bot_db
from keyboards import start_inline_button
import const


async def start_button(message: types.Message):
    db = bot_db.Database()
    db.sql_insert_user(
        tg_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
    )
    print(message.get_full_command())
    command = message.get_full_command()
    if command[1] != "":
        link = await _create_link("start", payload=command[1])
        owner = db.sql_select_user_by_link(
            link=link
        )
        if owner['telegram_id'] == message.from_user.id:
            await bot.send_message(
                chat_id=message.from_user.id,
                text='U can not use ur own link!!!'
            )
            return

        try:
            db.sql_insert_referral(
                owner=owner['telegram_id'],
                referral=message.from_user.id
            )
        except sqlite3.IntegrityError:
            pass

    with open(MEDIA_DESTINATION + "Bot.gif", 'rb') as ani:
        await bot.send_animation(
            chat_id=message.from_user.id,
            animation=ani,
            caption=const.START_MENU_TEXT.format(
                user=message.from_user.first_name
            ),
            reply_markup=await start_inline_button.start_keyboard()
        )


def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(
        start_button,
        commands=['start']
    )