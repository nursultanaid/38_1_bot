from aiogram import executor
from config import dp
from handlers import (
    start,
    questionnaire,
    group_actions
)
from database import bot_db
async def on_startup(_):
    db = bot_db.BotDB
    db.sql_create_table()

start.register_start_handlers(dp=dp)
questionnaire.register_questionnaire_handlers(dp=dp)
group_actions.register_group_action_handlers(dp=dp)

if __name__ == '__main__':
    executor.start_polling(
        dp
    )

