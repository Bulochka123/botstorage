from src.views.main_menu.keyboards import get_main_keyboard


class MainMenu:
    @staticmethod
    def get_text():
        text = "Добро пожаловать в хранилище от Макса!"
        return text

    @staticmethod
    def get_keyboard():
        return get_main_keyboard()
