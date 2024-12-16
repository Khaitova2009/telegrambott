from aiogram.fsm.state import State,StatesGroup
 
class UstozShogird(StatesGroup):
    Familiyangizni_kiriting = State ()
    Ismingizni_kiriting = State ()
    Yoshingizni_kiriting = State ()
    Telefon_raqamingizni_kiriting = State ()
    Viloyatni_kiriting = State ()
    Ish_vaqti = State ()
    Maosh = State ()
    Qoshimcha_malumot = State ()