from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def kb_client():

    button_1 = KeyboardButton('/register')

    keyboard_client = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard_client.add(button_1)

    return keyboard_client
