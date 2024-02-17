import datetime
from aiogram import types, Dispatcher
import database.bot_db
from config import bot, GROUP_ID
from keyboards import questionnaire_inline_button
from profanity_check import predict, predict_prob

async def chat_messages(message: types.Message):
    db = database.bot_db.Database
    if message.chat.id == int(GROUP_ID):
        # ban_words = predict([message.text])
        ban_words_prob = predict_prob([message.text])

        if ban_words_prob > 0.8:
            potential = db.sql_select_ban_user(
                tg_id=message.from_user.id
            )
            if not potential:
                db.sql_update_ban_count(
                    tg_id=message.from_user.id
                )
            elif potential['count'] >= 3:
                await bot.ban_chat_member(
                    chat_id=message.chat.id,
                    user_id=message.from_user.id,
                    until_date=datetime.datetime.now() + datetime.timedelta(seconds=1)
                )
                await bot.send_message(
                    chat_id=message.chat.id,
                    text=f'User: {message.from_user.first_name} banned\n'
                         f'Ban count: {potential["count"]}'
                )
            else:
                db.sql_insert_ban_user(
                    tg_id=message.from_user.id
                )
            await  message.delete()
            await bot.send_message(
                chat_id=message.chat.id,
                text=f'Hey{message.from_user.first_name}\n'
                     f'Do not curse in our chat!!!👊🏻'
                )

def register_group_action_handlers(dp: Dispatcher):
    dp.register_message_handler(
        chat_messages
    )