from aiogram import types

from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

async def availability_ban_user(message: types.Message):
    markup = InlineKeyboardMarkup()
    availability_button = InlineKeyboardButton(
        "Availability to ban check😶",
        callback_data="availability_check"
    )
    markup.add(availability_button)
    return markup