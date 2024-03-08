# import sqlite3
# from aiogram import types, Dispatcher
# import database.bot_db
# from config import bot, GROUP_ID
# from profanity_check import predict, predict_prob
#
#
# async def availability_check(message: types.Message):
#     db = database.bot_db.Database()
#     if message.from_user.id:
#         if message.from_user:
#             banned = db.sql_availability_ban_user(
#                 tg_id=message.from_user.id
#             )
#
# if is_banned(message.from_user.id):
#                 # Получение количества нарушений
#                 cursor.execute('''SELECT COUNT FROM banned_users WHERE TELEGRAM_ID = ?''', (message.from_user.id,))
#                 count = cursor.fetchone()[0]
#                 # Отправка сообщения с количеством нарушений
#                 bot.send_message(message.chat.id, f"Вы уже нарушили правила {count} раз(а).")
#
#
# async def chat_messages(message: types.Message):
#     db = database.bot_db.Database()
#     if message.chat.id == int(GROUP_ID):
#         ban_words_prob = predict_prob([message.text])
#         if ban_words_prob > 0.8:
#             potential = db.sql_select_ban_user(
#                 tg_id=message.from_user.id
#             )
#
#
#
#             if not potential:
#                 db.sql_insert_ban_user(
#                     tg_id=message.from_user.id
#                 )
#             elif potential['count'] >= 3:
#                 await bot.ban_chat_member(
#                     chat_id=message.chat.id,
#                     user_id=message.from_user.id,
#                     until_date=datetime.datetime.now() + datetime.timedelta(hours=1)
#                 )
#                 await bot.send_message(
#                     chat_id=message.chat.id,
#                     text=f"User: @{message.from_user.first_name} banned\n"
#                          f"Ban Count: {potential['count']}"
#                 )
#             else:
#                 db.sql_update_ban_count(
#                     tg_id=message.from_user.id
#                 )
#             await message.delete()
#             await bot.send_message(
#                 chat_id=message.chat.id,
#                 text=f'Hey!!! @{message.from_user.first_name}\n'
#                      f'You have cursed {potential["count"]} times!\n'
#                      f'If num of cursing reaches 3 times, you will get ban!\n'
#                      f'Stop curse in our chat 👊🏻!!!'
#             )
#             print(potential)