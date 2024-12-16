from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Xiva"), KeyboardButton(text="Toshkent"), KeyboardButton(text="Namangan")],
    ],
     resize_keyboard = True
)