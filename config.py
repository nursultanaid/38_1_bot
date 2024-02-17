from aiogram import Dispatcher, Bot
from decouple import config

MEDIA_DESTINATION = config("MEDIA_DESTINATION")
TOKEN = config("TOKEN")
GROUP_ID = config("GROUP_ID")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

