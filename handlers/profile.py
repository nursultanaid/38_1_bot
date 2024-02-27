import sqlite3
from aiogram import types, Dispatcher
import const
from config import bot
from database.bot_db import Database
from keyboards.profile_inline_button import (
    my_profile_keyboard,
    like_dislike_keyboard
)
import random
import re


async def my_profile_call(call: types.CallbackQuery):
    db = Database()
    profile = db.sql_select_profile(
        tg_id=call.from_user.id
    )

    if profile:
        with open(profile['photo'], 'rb') as photo:
            await bot.send_photo(
                chat_id=call.from_user.id,
                photo=photo,
                caption=const.PROFILE_TEXT.format(
                    nickname=profile['nickname'],
                    bio=profile['bio'],
                    age=profile['age'],
                    sign=profile['sign'],
                ),
                reply_markup=await my_profile_keyboard()
            )
    else:
        await bot.send_message(
            chat_id=call.from_user.id,
            text="U did not registered\n"
                 "Please register to view ur profile"
        )

async def random_fiter_profile_call(call: types.CallbackQuery):
    db = Database()
    profiles = db.sql_select_all_profiles(
        tg_id=call.from_user.id
    )
    random_profile = random.choice(profiles)
    with open(random_profile['photo'], 'rb') as photo:
        await bot.send_photo(
            chat_id=call.from_user.id,
            photo=photo,
            caption=const.PROFILE_TEXT.format(
                nickname=random_profile['nickname'],
                bio=random_profile['bio'],
                age=random_profile['age'],
                sign=random_profile['sign'],
            ),
            reply_markup = await like_dislike_keyboard(
                tg_id=random_profile['telegram_id']
            )
        )

async def detect_like_call(call: types.CallbackQuery):
    await call.message.delete()
    owner = re.sub("like_", "", call.data)
    print(owner)
    db = Database()
    db.sql_insert_like(
        owner=owner,
        liker=call.from_user.id
    )
    await random_fiter_profile_call(call=call)

def register_profile_handler(dp: Dispatcher):
    dp.register_callback_query_handler(
        my_profile_call,
        lambda call: call.data == "my_profile"
    )
    dp.register_callback_query_handler(
        random_fiter_profile_call,
        lambda call: call.data == "random_profiles"
    )
    dp.register_callback_query_handler(
        detect_like_call,
        lambda call: 'like_' in call.data
    )