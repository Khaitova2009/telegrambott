from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
menu=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Русский алфавит/Rus tili alifbosi", callback_data='alifbo')],
        [InlineKeyboardButton(text="Система счисления русского языка/Rus tili sanoq sistemasi",callback_data='sanoq')],
        [InlineKeyboardButton(text="Грамматика русского языка/Rus tili gramatilasi",callback_data='gramatika')],
    ],
)

alifbe = ["А","Б","В","Г","Д","E","Ж","З","И","Й","К","Л","М","Н","О","П","Р","С","Т","У","Ф","Х","Ц","Ч","Ш","Щ","Ъ","Ы","Ь","Э","Ю","Я"]
harflar=InlineKeyboardBuilder()
for i in alifbe:
    harflar.button(text=f'{i}',callback_data=f'{i}')
harflar.adjust(4)








# maxx = ["Qish", "Bahor", "Yoz", "Kuz"]
# maxsulotlar=InlineKeyboardBuilder()
# for i in maxx:
#     maxsulotlar.button(text=f'{i}',callback_data=f'{i}')
# maxsulotlar.adjust(2)