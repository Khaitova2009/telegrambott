import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message,CallbackQuery
from config import BOT_TOKEN as token
from button import *
bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

@dp.message(Command('start'))
async def StartCommand(message: Message):
   await message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=de526850208a84902373b37f897f8412d44e6ae8-12523274-images-thumbs&n=13", caption="Dasturlash tillari")
    
@dp.message(F.data == "1 -dars")
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/17',reply_markup=csss)

@dp.message(F.data == "2 -dars")
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/18',reply_markup=csss)


@dp.message(F.data == "3 -dars")
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/19',reply_markup=csss)


@dp.message(F.data == "4 -dars")
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/20',reply_markup=csss)


@dp.message(F.data == "5 -dars")
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/21',reply_markup=csss)


@dp.message(F.data == "6 -dars")
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/22',reply_markup=csss)


@dp.message(F.data == "7 -dars")
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/23',reply_markup=csss)


@dp.message(F.data == "8 -dars")
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/24',reply_markup=csss)


@dp.message(F.data == "9 -dars")
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/25',reply_markup=csss)

@dp.message(F.data == "10 -dars")
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/26',reply_markup=csss)

@dp.message(F.data == "1--dars")
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/46',reply_markup=java)

@dp.message(F.data == "2--dars")
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/47',reply_markup=java)

@dp.message(F.data == "3--dars")
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/48',reply_markup=java)

@dp.message(F.data == "4--dars")
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/49',reply_markup=java)

@dp.message(F.data == "5--dars")
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/50',reply_markup=java)

@dp.message(F.data == "6--dars")
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/51',reply_markup=java)

@dp.message(F.data == "7--dars")
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/52',reply_markup=java)

@dp.message(F.data == "8--dars")
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/53',reply_markup=java)

@dp.message(F.data == "9--dars")
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/54',reply_markup=java)

@dp.message(F.data == "10--dars")
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/55',reply_markup=java)

@dp.message(F.data == "1--Dars")
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/32',reply_markup=ccc)

@dp.message(F.data == "2--Dars")
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/33',reply_markup=ccc)

@dp.message(F.data == "3--Dars")
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/34',reply_markup=ccc)

@dp.message(F.data == "4--Dars")
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/35',reply_markup=ccc)

@dp.message(F.data == "5--Dars")
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/36',reply_markup=ccc)

@dp.message(F.data == "6--Dars")
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/37',reply_markup=ccc)

@dp.message(F.data == "7--Dars")
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/38',reply_markup=ccc)

@dp.message(F.data == "8--Dars")
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/39',reply_markup=ccc)

@dp.message(F.data == "9--Dars")
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/40',reply_markup=ccc)












async def main():
  await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
