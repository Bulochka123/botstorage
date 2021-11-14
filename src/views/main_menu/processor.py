from aiogram import types

from config import EXTENSIONS_PATH
from src.base.constants import me
from src.base.helpers import read_extensions_db
from src.base.objects import dispatcher
from src.views.main_menu.menu import MainMenu

import os


@dispatcher.message_handler(commands=["start"])
async def show_main_menu(message: types.Message):
    menu = MainMenu()
    await message.answer(
        text=menu.get_text(),
        reply_markup=menu.get_keyboard()
    )


@dispatcher.message_handler(lambda message: message.text == me)
async def managing_extensions(message: types.Message):
    if not os.path.exists(EXTENSIONS_PATH):
        text = "Нет доступных расширений"
    else:
        extensions = read_extensions_db()
        text = "В данный момент доступны расширения:\n"
        for extension, branches in extensions.items():
            item_text = f"{extension}: {branches}\n"
            text += item_text
    await message.answer(text)
