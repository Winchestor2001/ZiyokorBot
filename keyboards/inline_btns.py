from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import CHANNEL_LINK


async def subscribe_btn():
    btn = InlineKeyboardMarkup(row_width=1)
    btn.add(
        InlineKeyboardButton("➕ Kanalga o'tish", url=CHANNEL_LINK),
        InlineKeyboardButton("✅ A'zo bo'ldim", callback_data="subscribe")
    )
    return btn

