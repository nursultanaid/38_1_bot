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
    horror_button = InlineKeyboardButton(
        "Horror 🧟‍",
        callback_data="horror"
    )
    action_button = InlineKeyboardButton(
        "Action 🥷🏻",
        callback_data="action"
    )
    markup.add(horror_button)
    markup.add(action_button)
    return markup