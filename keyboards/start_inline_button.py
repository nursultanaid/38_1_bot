from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Questionnaire ❓",
        callback_data="start_questionnaire"
    )
    # swearer_button = InlineKeyboardButton(
    #     "Swearer 🤬",
    #     callback_data="swearer"
    # )
    registration_button = InlineKeyboardButton(
        "Registration 📝",
        callback_data="registration"
    )
    my_profile_button = InlineKeyboardButton(
        "My profile 📰",
        callback_data="my_profile"
    )
    profiles_button = InlineKeyboardButton(
        "Check profiles 🧐",
        callback_data="random_profiles"
    )
    reference_button = InlineKeyboardButton(
        "Reference Menu 💷",
        callback_data="reference_menu"
    )
    # news_button = InlineKeyboardButton(
    #     "Last five News 🗞",
    #     callback_data="last_news"
    # )
    markup.add(questionnaire_button)
    # markup.add(swearer_button)
    markup.add(registration_button)
    markup.add(my_profile_button)
    markup.add(profiles_button)
    markup.add(reference_button)
    # markup.add(news_button)
    return markup