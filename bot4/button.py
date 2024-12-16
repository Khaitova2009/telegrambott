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
  await message.answer_photo(photo='https://i.pinimg.com/originals/7c/d8/28/7cd828487e0e630e1cd0026253a29e93.jpg',caption='Dastrulash darsiga hush kelibsiz!',reply_markup=menu)
  
@dp.message(F.text=="Fronted")
async def it(message:Message):
   await message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=bf2aebc8c747886c14b52beb4db22f4c_l-9147490-images-thumbs&n=13",caption="Fronted !",reply_markup=html)

@dp.message(F.text=="Bakent")
async def it(message:Message):
   await message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=d9cc8885eaf826e514190cb7cffe8e1f5d36e3d3-10869405-images-thumbs&n=13",caption="Bakent",reply_markup=fron)

@dp.message(F.text=="Aloqa")
async def it(message:Message):
   await message.answer_photo(photo="https://static10.tgstat.ru/channels/_0/5d/5da5a97a698ecad4ce93d293ff8a207a.jpg",caption="Aloqa",reply_markup=menu)

@dp.message(F.text=="HTML")
async def it(message:Message):
   await message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=89f11c7e63cc82a8edce7209e20c7c7c8eb97f19-4438614-images-thumbs&n=13",caption="HTML!",reply_markup=Html)

@dp.message(F.text=="CSS")
async def it(message:Message):
   await message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=a30f5f99811273754c1bcecbc9a6c807_l-10385132-images-thumbs&n=13",caption="CSS",reply_markup=csss)

@dp.message(F.text=="PYTHON")
async def it(message:Message):
   await message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=da4f86f7be7f0f012099df703de8a29eba175c1d-12522847-images-thumbs&n=13",caption="Python!",reply_markup=fron)

@dp.message(F.text=="JAVASCRIPT")
async def it(message:Message):
   await message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=3389e73cf4b07d713a6b3adbdd109d2e1779c460-5545903-images-thumbs&n=13",caption="Java-Script",reply_markup=fron)

@dp.message(F.text=="C++")
async def it(message:Message):
   await message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=78fb54a6ff6d20d974607f19afd31d106cd57311-12463602-images-thumbs&n=13",caption="C++",reply_markup=fron)

@dp.message(F.text == "1-darst")
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/17',reply_markup=csss)

@dp.message(F.data == "2-darst")
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




@dp.callback_query(F.data == 'HTML')
async def StartCommand(message: Message):
   await message.answer(text="Html darslari", reply_markup=Html)


@dp.callback_query(F.data == '1-dars')
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/7', reply_markup=Html)

@dp.callback_query(F.data == '2-dars')
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/8', reply_markup=Html)

@dp.callback_query(F.data == '3-dars')
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/9', reply_markup=Html)


@dp.callback_query(F.data == '4-dars')
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/10', reply_markup=Html)


@dp.callback_query(F.data == '5-dars')
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/11', reply_markup=Html)


@dp.callback_query(F.data == '6-dars')
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/12', reply_markup=Html)



@dp.callback_query(F.data == '7-dars')
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/13', reply_markup=Html)


@dp.callback_query(F.data == '8-dars')
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/14', reply_markup=Html)


@dp.callback_query(F.data == '9-dars')
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/15', reply_markup=Html)


@dp.callback_query(F.data == '10-dars')
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/16', reply_markup=Html)

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



@dp.message(text= "5--Dars")
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/36',reply_markup=ccc)

@dp.message(text= "6--Dars")
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/37',reply_markup=ccc)

@dp.message(text= "7--Dars")
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/38',reply_markup=ccc)

@dp.message(text= "8--Dars")
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/39',reply_markup=ccc)

@dp.message(text= "9--Dars")
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/40',reply_markup=ccc)

@dp.message(text= "Python")
async def StartCommand(message: Message):
   await message.answer(text="python darslari", reply_markup=pyton)


@dp.message(text= "1 - dars")
async def StartCommand(message: Message):
   await message.answer(text="https://t.me/botvideo12/26", reply_markup=pyton)


@dp.message(text= "2 - dars")
async def StartCommand(message: Message):
   await message.answer(text="https://t.me/botvideo12/27", reply_markup=pyton)


@dp.message(text= "3 - dars")
async def StartCommand(message: Message):
   await message.answer(text="https://t.me/botvideo12/28", reply_markup=pyton)


@dp.message(text= "4 - dars")
async def StartCommand(message: Message):
   await message.answer(text="https://t.me/botvideo12/29", reply_markup=pyton)


@dp.message(text= "5 - dars")
async def StartCommand(message: Message):
   await message.answer(text="https://t.me/botvideo12/30", reply_markup=pyton)


@dp.message(text= "6 - dars")
async def StartCommand(message: Message):
   await message.answer(text="https://t.me/botvideo12/30", reply_markup=pyton)


@dp.message(text= "7 - dars")
async def StartCommand(message: Message):
   await message.answer(text="https://t.me/botvideo12/31", reply_markup=pyton)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


# @dp.message(F.text=="Fronted")
# async def it(message:Message):
#   await message.answer_photo(photo="",caption="",reply_markup=menu)
