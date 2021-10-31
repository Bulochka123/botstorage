from aiogram import types

from src.base.constants import me
from src.base.objects import dispatcher
from src.views.main_menu.menu import MainMenu


@dispatcher.message_handler(commands=["start"])
async def show_main_menu(message: types.Message):
    menu = MainMenu()
    await message.answer(
        text=menu.get_text(),
        reply_markup=menu.get_keyboard()
    )


@dispatcher.message_handler(lambda message: message.text == me)
async def managing_extensions(message: types.Message):
    await message.answer("Полетели")
