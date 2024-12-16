import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import Message

from botton2 import meny, vil, shah1, shah2, shah3, shah4, shah5
import wikipedia

wikipedia.set_lang("uz")

bot = Bot(token="7821528426:AAEgV1XNCxJqaZAqu_zHYrpNGWi2JXPEpyc")
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message:types.Message):
    await message.answer(text= "Salom wikipedia botga xush kelibsiz!", reply_markup=meny)

@dp.message(F.text == 'Viloyatlar')
async def shop1(message: Message):
    wiki=wikipedia.summary(message.text)
    await message.answer_photo(photo='https://static.tildacdn.com/tild6632-3836-4633-a663-636265303165/photo.jpg', caption=f'{wiki}', reply_markup=vil)


@dp.message(F.text == "Xorazm")
async def wiki(message:Message):
    wiki = wikipedia.summary(message.text)
    await message.answer_photo(photo='https://s0.rbk.ru/v6_top_pics/media/img/7/82/756558266557827.jpg',caption=f'{wiki}',reply_markup=shah1)

@dp.message(F.text == "Buxoro")
async def wiki(message:Message):
    wiki = wikipedia.summary(message.text)
    await message.answer_photo(photo='https://avatars.mds.yandex.net/i?id=3d3a60c7df47c1c88e4c8b48d681b8370ddebd33-9834801-images-thumbs&n=13',caption=f'{wiki}',reply_markup=shah2)

@dp.message(F.text == "Farg'ona")
async def wiki(message:Message):
    wiki = wikipedia.summary(message.text)
    await message.answer_photo(photo='https://uza.uz/upload/medialibrary/737/15.jpg',caption=f'{wiki}',reply_markup=shah3)

@dp.message(F.text == "Jizzax")
async def wiki(message:Message):
    wiki = wikipedia.summary(message.text)
    await message.answer_photo(photo='https://avatars.mds.yandex.net/i?id=8492288d761dc6eda5f5b3056402478f5aac1bae-4381247-images-thumbs&n=13',caption=f'{wiki}',reply_markup=shah4)

@dp.message(F.text == "Navoiy")
async def wiki(message:Message):
    wiki = wikipedia.summary(message.text)
    await message.answer_photo(photo='https://i.pinimg.com/originals/66/d0/c5/66d0c581902eb7748832ae9a42f2c0ef.png',caption=f'{wiki}',reply_markup=shah5)

@dp.message(F.text == "Xiva")
async def wiki(message:Message):
    wiki = wikipedia.summary(message.text)
    await message.answer_photo(photo='https://cdn.tripster.ru/thumbs2/f0e9bb86-597b-11ee-9b38-e28d8140917d.1200x1000.jpeg',caption=f'{wiki}',reply_markup=shah1)

@dp.message(F.text == "Qo'shko'pir")
async def wiki(message:Message):
    wiki = wikipedia.summary(message.text)
    await message.answer_photo(photo='https://static10.tgstat.ru/channels/_0/08/0836bec0cad0b90fea885a3c7c0c8534.jpg',caption=f'{wiki}',reply_markup=shah1)

@dp.message(F.text == "Urganch")
async def wiki(message:Message):
    wiki = wikipedia.summary(message.text)
    await message.answer_photo(photo='https://img-fotki.yandex.ru/get/4404/235890831.2/0_114dfb_5d3755fe_XXL',caption=f'{wiki}',reply_markup=shah1)

@dp.message(F.text == "Xonqa")
async def wiki(message:Message):
    wiki = wikipedia.summary(message.text)
    await message.answer_photo(photo='https://www.tefl.com/recruiterImages/e6f58a74-dda9-4e82-ab03-7aea8c34d403.jpg',caption=f'{wiki}',reply_markup=shah1)

@dp.message(F.text == "Orqaga")
async def wiki(message:Message):
    await message.answer(text="Asosiy menu",reply_markup=vil)

@dp.message(F.text == "Kogon")
async def wiki(message:Message):
    wiki = wikipedia.summary(message.text)
    await message.answer_photo(photo='https://proza.ru/pics/2021/12/06/1622.jpg',caption=f'{wiki}',reply_markup=shah2)

@dp.message(F.text == "G'ijduvon")
async def wiki(message:Message):
    wiki = wikipedia.summary(message.text)
    await message.answer_photo(photo='https://avatars.dzeninfra.ru/get-zen_doc/1886085/pub_606d478d756f335670e41ce4_606d66a1a133670139f2407b/scale_1200',caption=f'{wiki}',reply_markup=shah2)

@dp.message(F.text == "Vobkent")
async def wiki(message:Message):
    wiki = wikipedia.summary(message.text)
    await message.answer_photo(photo='http://ic.pics.livejournal.com/orchid_eya/19793158/365085/365085_original.jpg',caption=f'{wiki}',reply_markup=shah2)

@dp.message(F.text == " Buxoro shahar markazi ")
async def wiki(message:Message):
    wiki = wikipedia.summary(message.text)
    await message.answer_photo(photo='https://www.gazeta.uz/media/img/2023/12/vNHlTE17019517377063_l.jpg',caption=f'{wiki}',reply_markup=shah2)

@dp.message(F.text == "OrqagA")
async def wiki(message:Message):
    await message.answer(text="Asosiy menu",reply_markup=vil)




@dp.message(F.text == "Marg'ilon")
async def wiki(message:Message):
    wiki = wikipedia.summary(message.text)
    await message.answer_photo(photo='https://upload.wikimedia.org/wikipedia/commons/2/2b/%D0%A4%D0%B5%D1%80%D0%B3%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B5_%D0%92%D0%BE%D1%80%D0%BE%D1%82%D0%B0.jpg',caption=f'{wiki}',reply_markup=shah3)

@dp.message(F.text == "Qo‘qon")
async def wiki(message:Message):
    wiki = wikipedia.summary(message.text)
    await message.answer_photo(photo='https://stihi.ru/pics/2024/06/15/5306.jpg',caption=f'{wiki}',reply_markup=shah3)

@dp.message(F.text == "Oltiariq")
async def wiki(message:Message):
    wiki = wikipedia.summary(message.text)
    await message.answer_photo(photo='https://rct.kz/assets/images/countries/uzbekistan/andijan/andizhan.jpg',caption=f'{wiki}',reply_markup=shah3)

@dp.message(F.text == "Bo'ston")
async def wiki(message:Message):
    wiki = wikipedia.summary(message.text)
    await message.answer_photo(photo='https://cdn.uza.uz/2022/03/08/16/54/T6O9zKd6bEcBL6mePCw8qkd47If5yRp7_normal.jpg',caption=f'{wiki}',reply_markup=shah3)

@dp.message(F.text == "ORqaga")
async def wiki(message:Message):
    await message.answer(text="Asosiy menu",reply_markup=vil)




@dp.message(F.text == "Arnasoy")
async def wiki(message:Message):
    wiki = wikipedia.summary(message.text)
    await message.answer_photo(photo='https://anhor.uz/wp-content/uploads/2020/11/502.jpg',caption=f'{wiki}',reply_markup=shah4)

@dp.message(F.text == "G‘allaorol")
async def wiki(message:Message):
    wiki = wikipedia.summary(message.text)
    await message.answer_photo(photo='https://daryo.uz/cache/2019/02/photo_2019-02-27_22-35-03-1280x852.jpg',caption=f'{wiki}',reply_markup=shah4)

@dp.message(F.text == "Baxmal")
async def wiki(message:Message):
    wiki = wikipedia.summary(message.text)
    await message.answer_photo(photo='https://en.sezamtravel.uz/d/gory_chimgan_11.jpg',caption=f'{wiki}',reply_markup=shah4)

@dp.message(F.text == "Forish")
async def wiki(message:Message):
    wiki = wikipedia.summary(message.text)
    await message.answer_photo(photo='https://uzb-urban.uz/storage/project_images/1654598103_photo_2022-04-27_11-08-20.jpg',caption=f'{wiki}',reply_markup=shah4)

@dp.message(F.text == "ORQaga")
async def wiki(message:Message):
    await message.answer(text="Asosiy menu",reply_markup=vil)




@dp.message(F.text == "Uchquduq")
async def wiki(message:Message):
    wiki = wikipedia.summary(message.text)
    await message.answer_photo(photo='https://avatars.dzeninfra.ru/get-zen_doc/8098241/pub_64117d244d97ea3d686eafea_64117d7daad9141a24985199/scale_1200',caption=f'{wiki}',reply_markup=shah5)

@dp.message(F.text == "Karmana ")
async def wiki(message:Message):
    wiki = wikipedia.summary(message.text)
    await message.answer_photo(photo='https://avatars.mds.yandex.net/i?id=cb3dc91641d5beb5924f4793321c0d716d87741d-12569941-images-thumbs&n=13',caption=f'{wiki}',reply_markup=shah5)

@dp.message(F.text == "Nurota")
async def wiki(message:Message):
    wiki = wikipedia.summary(message.text)
    await message.answer_photo(photo='https://agroturizm.uz/images/Nurotatur1.jpg',caption=f'{wiki}',reply_markup=shah5)

@dp.message(F.text == "Zarafshon ")
async def wiki(message:Message):
    wiki = wikipedia.summary(message.text)
    await message.answer_photo(photo='https://avatars.mds.yandex.net/get-altay/5235198/2a0000017b1b06ad9e6d9c3761deb8a8eab7/XXL_height',caption=f'{wiki}',reply_markup=shah5)

@dp.message(F.text == "ORQAGA")
async def wiki(message:Message):
    await message.answer(text="Asosiy menu",reply_markup=vil)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())