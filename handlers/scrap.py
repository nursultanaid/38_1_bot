import sqlite3
from aiogram import types, Dispatcher
from scraping.film_scraper import FilmScraper
from config import bot
from database import bot_db


async def start_button(message: types.Message):
    db = bot_db.Database()
    scraper = FilmScraper()
    films = scraper.scrape_data()
    for i in films[:5]:
        await message.answer(i['link'])

def register_scraper_handlers(dp: Dispatcher):
    dp.register_message_handler(
        start_button,
        commands=['scraper']
    )

