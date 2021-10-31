from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


def get_main_keyboard():
    kb = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    kb.add(
        KeyboardButton("Загрузки", callback_data="show_uploads"),
        KeyboardButton("Управление расширениями", callback_data="managing_extensions"),
        KeyboardButton("Избранное", callback_data="favourites")
    )
    return kb