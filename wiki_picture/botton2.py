from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

meny = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Viloyatlar")]
    ],
    resize_keyboard=True
)

vil = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Xorazm"), KeyboardButton(text="Buxoro"), KeyboardButton(text="Farg'ona")],
        [KeyboardButton(text="Jizzax"), KeyboardButton(text="Navoiy")],
    ],
    resize_keyboard = True
)

shah1 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Xiva"), KeyboardButton(text="Qo'shko'pir")],
        [KeyboardButton(text="Urganch"), KeyboardButton(text="Xonqa")],
        [KeyboardButton(text="Orqaga")]
    ],
    resize_keyboard = True
)

shah2 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Kogon"), KeyboardButton(text="G'ijduvon")],
        [KeyboardButton(text="Vobkent"), KeyboardButton(text="Buxoro shahar markazi ")],
        [KeyboardButton(text="OrqagA")]
    ],
    resize_keyboard = True
)
shah3 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Marg'ilon"), KeyboardButton(text="Qo‘qon")],
        [KeyboardButton(text="Oltiariq"), KeyboardButton(text="Bo‘ston")],
        [KeyboardButton(text="ORqaga")]
    ],
    resize_keyboard = True
)

shah4 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Arnasoy"), KeyboardButton(text="G‘allaorol")],
        [KeyboardButton(text="Baxmal"), KeyboardButton(text="Forish")],
        [KeyboardButton(text="ORQaga")]
    ],
    resize_keyboard = True
)

shah5 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Uchquduq"), KeyboardButton(text="Karmana")],
        [KeyboardButton(text="Nurota"), KeyboardButton(text="Zarafshon ")],
        [KeyboardButton(text="ORQAGA")]
    ],
    resize_keyboard = True
)