from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import *

from database.connections import *
from keyboards.inline_btns import *
from keyboards.reply_btns import *
from loader import dp, bot
from config import CHANNEL_ID, CHANNEL_USERNAME
from states.AllStates import UserStates


async def bot_start_handler(message: Message):
    user_id = message.from_user.id
    username = message.from_user.username
    check_user_full_name = await add_user_db(user_id, username)
    if check_user_full_name:
        await message.answer(f"👋🏻Assalomu aleykum qadirli\n"
                             f"📋Ro'yxatdan utish uchun Familiya va Ismingizni kiriting!")
        await UserStates.full_name.set()
    else:
        check_channel = (await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)).status
        if check_channel != "left":
            btn = await start_menu_btn()
            await message.answer("ℹ️ Bo`limni tanlang:", reply_markup=btn)
        else:
            btn = await subscribe_btn()
            await message.answer(
                f"Botdan to'liq foydalanishingiz uchun {CHANNEL_USERNAME} kanaliga a'zo bo'lishingiz shart!\n\n"
                f"Kanalga a'zo bo'lganingizdan so'ng \n"
                f"✅ A'zo bo'ldim tugmasini bosing.", reply_markup=btn)


async def user_full_name_state(message: Message, state: FSMContext):
    user_id = message.from_user.id
    full_name = message.text
    if len(full_name) >= 15:
        await update_user_db(user_id, full_name)
        await state.finish()
        check_channel = (await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)).status
        if check_channel != "left":
            btn = await start_menu_btn()
            await message.answer("ℹ️ Bo`limni tanlang:", reply_markup=btn)
        else:
            btn = await subscribe_btn()
            await message.answer(
                f"Botdan to'liq foydalanishingiz uchun {CHANNEL_USERNAME} kanaliga a'zo bo'lishingiz shart!\n\n"
                f"Kanalga a'zo bo'lganingizdan so'ng \n"
                f"✅ A'zo bo'ldim tugmasini bosing.", reply_markup=btn)
    else:
        await message.answer("⚠️ F.I.O to`liq emas!")


async def check_subscribe_user(c: CallbackQuery):
    user_id = c.from_user.id
    check_channel = (await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)).status
    if check_channel != 'left':
        await c.message.delete()
        btn = await start_menu_btn()
        await c.message.answer("ℹ️ Bo`limni tanlang:", reply_markup=btn)

    else:
        await c.answer(f"❗️ Siz xali kanalga a'zo bo'lmadingiz!", show_alert=True)


async def create_test_handler(message: Message):
    await message.answer(f"<b>📑Test yaratish bo'yicha qo'llanma:</b>\n\n"
                         f"<code>test+Fan nomi+1a2b3c4d5e.....</code>\n\n"
                         f"☝️<em>Namuna-1: test+Ona tili+1a2c3e4a5b....</em>\n"
                         f"☝️<em>Namuna-2: test+Ona tili+aceab....</em>")
    await UserStates.tests.set()


async def start_test_handler(message: Message):
    await message.answer(f"<b>📝Test yuborish bo'yicha qo'llanma:</b>\n\n"
                         f"<code>testkodi+1a2b3c4d5e.....</code>\n\n"
                         f"☝️<em>Namuna-1: 3541+1a2c3e4a5b....</em>\n"
                         f"☝️<em>Namuna-2: 3541+aceab....</em>")
    await UserStates.start_test.set()


def register_users_py(dp: Dispatcher):
    dp.register_message_handler(bot_start_handler, commands=['start'])

    dp.register_message_handler(create_test_handler, text='📑 Test yaratish')
    dp.register_message_handler(start_test_handler, text='📝 Test topshirish')
    dp.register_message_handler(user_full_name_state, state=UserStates.full_name)

    dp.register_callback_query_handler(check_subscribe_user, text='subscribe')
