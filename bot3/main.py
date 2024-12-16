import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, types, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from config import BOT_TOKEN as Token
from button import *
bot = Bot(token='7296502632:AAG4cUjo7XVf7G7_5A0JV8-znjQF9Q9nMUY', default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

@dp.message(Command('start'))
async def StartCommand(message: Message):
    await message.answer_photo(photo="https://static10.tgstat.ru/channels/_0/46/4665b5bf496dcc6f303f42296f9cf64f.jpg",caption='' , reply_markup=menu)


@dp.callback_query(F.data=="alifbo")
async def shop2(call:CallbackQuery):
    await call.message.answer_photo(photo='https://i.pinimg.com/originals/0c/fe/0b/0cfe0bab64ca0dbd577f2b4e85e446a2.png',caption='Буквы алфавита/Alifbo harflari',reply_markup=harflar)


@dp.callback_query(F.data=="sanoq")
async def shop2(call:CallbackQuery):
    await call.message.answer_photo(photo='https://i.ytimg.com/vi/_lHboSycg_k/maxresdefault.jpg',caption='Цифры на русском языке/Rus tilida sonlar')


@dp.callback_query(F.data=="gramatika")
async def shop2(call:CallbackQuery):
    await call.message.answer_photo(photo='https://i.ytimg.com/vi/GOU1ErXutVY/hqdefault.jpg',caption='Времена в русском языке/Rus tilida zamonlar')


@dp.callback_query(F.data=="alifbe")
async def shop2(call:CallbackQuery):
    await call.message.answer_photo(photo='https://ytimg.googleusercontent.com/vi/sp1dOqy2ja8/maxresdefault.jpg',caption='Письмо/Yozilishi')


@dp.callback_query(F.data=="alifbe")
async def shop2(call:CallbackQuery):
    await call.message.answer_photo(photo='https://1.bp.blogspot.com/-ys5qI1Nub0I/XDn2luBlxRI/AAAAAAAAAEM/P5Eca-pSfHYOV_JjSLJbHk5V08Q8A25iwCEwYBhgL/s1600/%25D0%25B1.jpg',caption='Письмо/Yozilishi',reply_markup=harflar)


@dp.callback_query(F.data=="alifbe")
async def shop2(call:CallbackQuery):
    await call.message.answer_photo(photo='https://sovyatka.ru/800/600/https/ds04.infourok.ru/uploads/ex/0ebf/000b806e-61ea6b4d/img8.jpg',caption='Письмо/Yozilishi',reply_markup=harflar)


@dp.callback_query(F.data=="alifbe")
async def shop2(call:CallbackQuery):
    await call.message.answer_photo(photo='https://avatars.mds.yandex.net/i?id=d740d363056f240278918f9342219425_l-5287637-images-thumbs&ref=rim&n=13&w=1024&h=767',caption='Письмо/Yozilishi',reply_markup=harflar)


@dp.callback_query(F.data=="alifbe")
async def shop2(call:CallbackQuery):
    await call.message.answer_photo(photo='https://i.ytimg.com/vi/GUCOb6nbpJQ/maxresdefault.jpg',caption='Письмо/Yozilishi',reply_markup=harflar)


@dp.callback_query(F.data=="alifbe")
async def shop2(call:CallbackQuery):
    await call.message.answer_photo(photo='https://cdn1.coreapp.ai/uploads/image/1649076247181-16490762481802148496624ae818a5cf6.jpeg',caption='Письмо/Yozilishi',reply_markup=harflar)


@dp.callback_query(F.data=="alifbe")
async def shop2(call:CallbackQuery):
    await call.message.answer_photo(photo='https://3.bp.blogspot.com/-Zw6ecnv9coY/XDn5CbtSHOI/AAAAAAAAAEs/S9_fld-EyskC9ssJAc2yhrepeWppekPDACLcBGAs/s1600/%25D0%2581.jpg',caption='Письмо/Yozilishi',reply_markup=harflar)


@dp.callback_query(F.data=="alifbe")
async def shop2(call:CallbackQuery):
    await call.message.answer_photo(photo='https://www.uchmag.ru/upload/catalog/posob/_/n/_n-123_/images/03.jpg',caption='Письмо/Yozilishi',reply_markup=harflar)


@dp.callback_query(F.data=="alifbe")
async def shop2(call:CallbackQuery):
    await call.message.answer_photo(photo='https://cdn1.coreapp.ai/uploads/image/1649402158898-16494021681128644065624fe1389f75e.jpeg',caption='Письмо/Yozilishi',reply_markup=harflar)


@dp.callback_query(F.data=="alifbe")
async def shop2(call:CallbackQuery):
    await call.message.answer_photo(photo='https://avatars.mds.yandex.net/i?id=12074e9a45655e6220b3daa81fbcd816efdf1199-9100075-images-thumbs&ref=rim&n=33&w=367&h=275',caption='Письмо/Yozilishi',reply_markup=harflar)


@dp.callback_query(F.data=="alifbe")
async def shop2(call:CallbackQuery):
    await call.message.answer_photo(photo='https://avatars.mds.yandex.net/i?id=233b569fde6ea9ab678102943efe38b33d5ce319-10812288-images-thumbs&ref=rim&n=33&w=378&h=275',caption='Письмо/Yozilishi',reply_markup=harflar)


@dp.callback_query(F.data=="alifbe")
async def shop2(call:CallbackQuery):
    await call.message.answer_photo(photo='https://avatars.mds.yandex.net/i?id=4e6426d92bbb523a6a368c4ee6391e842f7d0914-9268591-images-thumbs&ref=rim&n=33&w=366&h=275',caption='Письмо/Yozilishi',reply_markup=harflar)


@dp.callback_query(F.data=="alifbe")
async def shop2(call:CallbackQuery):
    await call.message.answer_photo(photo='https://for-teacher.ru/edu/data/img/pic-023omxb989-011.png',caption='Письмо/Yozilishi',reply_markup=harflar)


@dp.callback_query(F.data=="alifbe")
async def shop2(call:CallbackQuery):
    await call.message.answer_photo(photo='https://shareslide.ru/img/thumbs/d81da8a633d60c24a98fd34d5459d7f1-800x.jpg',caption='Письмо/Yozilishi',reply_markup=harflar)


@dp.callback_query(F.data=="alifbe")
async def shop2(call:CallbackQuery):
    await call.message.answer_photo(photo='https://fsd.multiurok.ru/html/2018/06/23/s_5b2d7c550ad89/921782_15.jpeg',caption='Письмо/Yozilishi',reply_markup=harflar)


@dp.callback_query(F.data=="alifbe")
async def shop2(call:CallbackQuery):
    await call.message.answer_photo(photo='https://3.bp.blogspot.com/-JptzTL-j6xM/XDn6lxA-7rI/AAAAAAAAAFw/XokyMN-VzZUtLWXgZY20F5i3n933qHv7wCLcBGAs/s1600/%25D0%25BE.jpg',caption='Письмо/Yozilishi',reply_markup=harflar)


@dp.callback_query(F.data=="alifbe")
async def shop2(call:CallbackQuery):
    await call.message.answer_photo(photo='https://3.bp.blogspot.com/-7uO_MQYFjkY/X02HoOWohQI/AAAAAAAA59s/LiQTq6yQJ6oWy7CVo1P95WkvQ5MfxxXmACLcBGAsYHQ/s1600/0015.jpg',caption='Письмо/Yozilishi',reply_markup=harflar)


@dp.callback_query(F.data=="alifbe")
async def shop2(call:CallbackQuery):
    await call.message.answer_photo(photo='https://deti-karusel.ru/wp-content/uploads/1/3/6/13692f391b8720a812867e4847864d37.png',caption='Письмо/Yozilishi',reply_markup=harflar)


@dp.callback_query(F.data=="alifbe")
async def shop2(call:CallbackQuery):
    await call.message.answer_photo(photo='https://3.bp.blogspot.com/-7t5wD_8Tewk/X02Hop7EpjI/AAAAAAAA590/DOGRlwPvQHwo8MLs7fhsBSDISK7RWjyjACLcBGAsYHQ/s1600/0017.jpg',caption='Письмо/Yozilishi',reply_markup=harflar)


@dp.callback_query(F.data=="alifbe")
async def shop2(call:CallbackQuery):
    await call.message.answer_photo(photo='https://fs.znanio.ru/d5af0e/bc/c2/11d901665c4c22650dae590c7eb3c9b3fa.jpg',caption='Письмо/Yozilishi',reply_markup=harflar)


@dp.callback_query(F.data=="alifbe")
async def shop2(call:CallbackQuery):
    await call.message.answer_photo(photo='https://fs.znanio.ru/d5af0e/c5/e3/50210bb42031acfb5c77559c0efc155690.jpg',caption='Письмо/Yozilishi',reply_markup=harflar)


@dp.callback_query(F.data=="alifbe")
async def shop2(call:CallbackQuery):
    await call.message.answer_photo(photo='https://2.bp.blogspot.com/-lRA8Y9_FEcg/X02Hpb38PoI/AAAAAAAA5-A/Twb94ZAgnZAnkJ295Wxkajt84KlHU1t8ACLcBGAsYHQ/s1600/0020.jpg',caption='Письмо/Yozilishi',reply_markup=harflar)


@dp.callback_query(F.data=="alifbe")
async def shop2(call:CallbackQuery):
    await call.message.answer_photo(photo='https://2.bp.blogspot.com/-x7nQfWwnaN0/X02HppshzwI/AAAAAAAA5-E/aGlYBnH4MAA-AAxTSA7vwH58wl0O_y4AwCLcBGAsYHQ/s1600/0021.jpg',caption='Письмо/Yozilishi',reply_markup=harflar)


@dp.callback_query(F.data=="alifbe")
async def shop2(call:CallbackQuery):
    await call.message.answer_photo(photo='https://fsd.multiurok.ru/html/2018/06/23/s_5b2d7c550ad89/921782_23.jpeg',caption='Письмо/Yozilishi',reply_markup=harflar)


@dp.callback_query(F.data=="alifbe")
async def shop2(call:CallbackQuery):
    await call.message.answer_photo(photo='https://fsd.multiurok.ru/html/2018/06/23/s_5b2d7c550ad89/921782_24.jpeg',caption='Письмо/Yozilishi',reply_markup=harflar)


@dp.callback_query(F.data=="alifbe")
async def shop2(call:CallbackQuery):
    await call.message.answer_photo(photo='https://avatars.mds.yandex.net/i?id=c3f69fc5cf4c4eb6322aa2fc4490d9f5bb497134-9042494-images-thumbs&ref=rim&n=33&w=378&h=275',caption='Письмо/Yozilishi',reply_markup=harflar)


@dp.callback_query(F.data=="alifbe")
async def shop2(call:CallbackQuery):
    await call.message.answer_photo(photo='https://avatars.mds.yandex.net/i?id=4f0bf3889d61737e680aa16577b371dedff86a63-8271677-images-thumbs&ref=rim&n=33&w=338&h=275',caption='Письмо/Yozilishi',reply_markup=harflar)


@dp.callback_query(F.data=="alifbe")
async def shop2(call:CallbackQuery):
    await call.message.answer_photo(photo='https://avatars.mds.yandex.net/i?id=667bddeeb6a7340f842e325aa82c529977d4d63c-9097381-images-thumbs&ref=rim&n=33&w=390&h=275',caption='Письмо/Yozilishi',reply_markup=harflar)


@dp.callback_query(F.data=="alifbe")
async def shop2(call:CallbackQuery):
    await call.message.answer_photo(photo='https://avatars.mds.yandex.net/i?id=dd76b6ce66dc1ae3862636f618423f11f994fc4c-9908477-images-thumbs&ref=rim&n=33&w=480&h=240',caption='Письмо/Yozilishi',reply_markup=harflar)


@dp.callback_query(F.data=="alifbe")
async def shop2(call:CallbackQuery):
    await call.message.answer_photo(photo='https://avatars.mds.yandex.net/i?id=667bddeeb6a7340f842e325aa82c529977d4d63c-9097381-images-thumbs&ref=rim&n=33&w=390&h=275',caption='Письмо/Yozilishi',reply_markup=harflar)


@dp.callback_query(F.data=="alifbe")
async def shop2(call:CallbackQuery):
    await call.message.answer_photo(photo='https://avatars.mds.yandex.net/i?id=0d7e714353033e3c0d8235bfbcceda3ac3d32dd2-9057188-images-thumbs&ref=rim&n=33&w=389&h=275',caption='Письмо/Yozilishi',reply_markup=harflar)

@dp.callback_query(F.data=="alifbe")
async def shop2(call:CallbackQuery):
    await call.message.answer_photo(photo='https://avatars.mds.yandex.net/i?id=3434960587ab6ac106866a6896c43a8f7c4451c5-9148257-images-thumbs&ref=rim&n=33&w=389&h=275',caption='Письмо/Yozilishi',reply_markup=harflar)


@dp.callback_query(F.data=="alifbe")
async def shop2(call:CallbackQuery):
    await call.message.answer_photo(photo='https://avatars.mds.yandex.net/i?id=4add7bd78c7e2049622e33f726b3271cd74a713c-10672158-images-thumbs&ref=rim&n=33&w=367&h=275',caption='Письмо/Yozilishi',reply_markup=harflar)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
