from aiogram import types, Dispatcher
from config import bot
from keyboards import questionnaire_inline_button


async def questionnaire_start(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Movie 🎥 or Music 🎵?",
        reply_markup=await questionnaire_inline_button.questionnaire_keyboard()
    )


async def movie_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="What kind of movie do you like?",
        reply_markup = await questionnaire_inline_button.movie_questionnaire_keyboard()
    )
async def music_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Yes, music is good!",
    )

async def horror_movie_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="OHH!! Are not u afraid?",
        reply_markup = await questionnaire_inline_button.horror_questionnaire_keyboard()
    )

async def action_movie_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Yeah! thats crazy!",
        reply_markup = await questionnaire_inline_button.action_questionnaire_keyboard()

    )

def register_questionnaire_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        questionnaire_start,
        lambda call: call.data == "start_questionnaire"
    )
    dp.register_callback_query_handler(
        music_answer,
        lambda call: call.data == "music"
    )
    dp.register_callback_query_handler(
        movie_answer,
        lambda call: call.data == "movie"
    )
    dp.register_callback_query_handler(
        horror_movie_answer,
        lambda call: call.data == "horror_movie"
    )
    dp.register_callback_query_handler(
        action_movie_answer,
        lambda call: call.data == "action_movie"
    )