import asyncio 
import logging 
import sys 
from aiogram import Bot, Dispatcher, F, html 
from aiogram.client.default import DefaultBotProperties 
from aiogram.enums import ParseMode 
from aiogram.filters import Command 
from aiogram.types import Message
from config import BOT_TOKEN 
from aiogram.fsm.context import FSMContext 
from state import UstozShogird as US 
from button import * 
 
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML)) 
dp = Dispatcher() 

 
@dp.message(Command('start')) 
async def CommandStart(message: Message):  
    await message.answer(f"Assalomu Aleykum, {html.bold(message.from_user.full_name)}!",reply_markup=menu) 

@dp.message(F.text == 'Ish Kerak') 
async def start_ism(message: Message, state: FSMContext): 
    await state.set_state(US.Familiyangizni_kiriting) 
    await message.answer(text='Familiyangizni Kiriting:')

@dp.message(US.Familiyangizni_kiriting) 
async def get_ism(message: Message, state: FSMContext): 
    fam = message.text 
    await state.update_data(fam=fam) 
    await message.answer(text='Ismingizni Kiriting:') 
    await state.set_state(US.Ismingizni_kiriting) 
 
@dp.message(US.Ismingizni_kiriting) 
async def get_ism(message: Message, state: FSMContext): 
    ism = message.text 
    await state.update_data(ism=ism) 
    await message.answer(text='Yoshingizni Kiriting:\nMasalan, 18') 
    await state.set_state(US.Yoshingizni_kiriting) 
 
@dp.message(US.Yoshingizni_kiriting) 
async def get_ism(message: Message, state: FSMContext): 
    yosh = message.text 
    await state.update_data(yosh=yosh) 
    await message.answer(text='Telefon raqamingizni kiriting:\nTel: +998') 
    await state.set_state(US.Telefon_raqamingizni_kiriting) 



@dp.message(US.Telefon_raqamingizni_kiriting) 
async def get_ism(message: Message, state: FSMContext): 
    tel = message.text 
    await state.update_data(tel=tel) 
    await message.answer(text="Viloyatingizni kiriting:\nO'zb. Res.") 
    await state.set_state(US.Viloyatni_kiriting)



@dp.message(US.Telefon_raqamingizni_kiriting) 
async def get_ism(message: Message, state: FSMContext): 
    vil = message.text 
    await state.update_data(vil=vil) 
    await message.answer(text="Ish vahtingizni kiriting:\nMasalan, 9:00 dan 22:00 gacha") 
    await state.set_state(US.Ish_vaqti)

@dp.message(US.Telefon_raqamingizni_kiriting) 
async def get_ism(message: Message, state: FSMContext): 
    ish = message.text 
    await state.update_data(ish=ish) 
    await message.answer(text="Maoshingizni kiriting:\nMasalan, 10000$") 
    await state.set_state(US.Maosh)

@dp.message(US.Telefon_raqamingizni_kiriting) 
async def get_ism(message: Message, state: FSMContext): 
    maosh = message.text 
    await state.update_data(maosh=maosh) 
    await message.answer(text="Qo'shimcha ma'lumot kiriting:") 
    await state.set_state(US.Qoshimcha_malumot)


@dp.message(US.Viloyatni_kiriting) 
async def get_viloyat(message: Message, state: FSMContext): 
    qosh = message.text 
    await state.update_data(qosh=qosh) 
    user_data = await state.get_data() 
    fam = user_data.get('fam')
    ism = user_data.get('ism') 
    yosh = user_data.get('yosh') 
    tel = user_data.get('tel') 
    vil = user_data.get('vil') 
    ish = user_data.get('ish')
    maosh = user_data.get('maosh')
    qosh = user_data.get('qosh')

     
     
    await message.answer(text=f"Familiyangiz: {fam}\nIsmingiz: {ism}\nYoshingiz: {yosh}\nTelefon: {tel}\nViloyat: {vil}\nIsh vaqti: {ish}\nMaosh: {maosh}\nQo'shimcha ma'lumot:{qosh}") 
    await state.clear() 


async def main(): 
    await dp.start_polling(bot) 
 
if __name__ == "__main__": 
    try: 
        logging.basicConfig(level=logging.INFO, stream=sys.stdout) 
        asyncio.run(main()) 
    except Exception as e: 
        print(f"Xatolik: {e}")
