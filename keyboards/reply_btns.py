from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton


remove_btn = ReplyKeyboardRemove()


async def start_menu_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    btn.add(
        KeyboardButton("📑 Test yaratish"),
        KeyboardButton("📝 Test topshirish"),
    )
    return btn
