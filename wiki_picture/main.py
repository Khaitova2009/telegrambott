import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import Message

from botton import menu


import wikipedia

wikipedia.set_lang("uz")

bot = Bot(token="7805288230:AAHqKki2jRCGpL7YmI39iTJenkLwAqrDUlU")
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message:types.Message):
    await message.answer("Botga xush kelibsiz!", reply_markup=menu)

@dp.message(F.text=="Xiva")
async def wiki(message:Message):
    wiki_answer= wikipedia.summary(message.text)
    await  message.answer(str(wiki_answer),reply_markup=menu)


@dp.message(F.text=="Toshkent")
async def wiki(message:Message):
    wiki_answer= wikipedia.summary(message.text)
    await  message.answer(str(wiki_answer),reply_markup=menu)


@dp.message(F.text=="Namangan")
async def wiki(message:Message):
    wiki_answer= wikipedia.summary(message.text)
    await  message.answer(str(wiki_answer),reply_markup=menu)


async def main():
    await dp.start_polling(bot)

if __name__ =="__main__":
    asyncio.run(main())