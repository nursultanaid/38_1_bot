from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

async def questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    music_button = InlineKeyboardButton(
        "Music 🎵",
        callback_data="music"
    )
    movie_button = InlineKeyboardButton(
        "Movie 🎥",
        callback_data="movie"
    )
    markup.add(music_button)
    markup.add(movie_button)
    return markup

async def movie_questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    doc_button = InlineKeyboardButton(
        "Documentary 🤵🏻‍",
        callback_data="documentary"
    )
    hor_button = InlineKeyboardButton(
        "Horror 🧟‍️",
        callback_data="horror"
    )
    markup.add(doc_button)
    markup.add(hor_button)
    return markup