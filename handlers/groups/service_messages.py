import asyncio

from aiogram import types

from filters import IsGroup, IsUser, RegexFilter
from loader import dp, bot


@dp.message_handler(IsGroup(), content_types=['new_chat_members', 'left_chat_member'])
async def on_user_joined(message: types.Message):
    await message.delete()
    await asyncio.sleep(0.05)


@dp.message_handler(IsGroup(), IsUser(), RegexFilter())
async def on_user_joined(message: types.Message):
    await message.delete()
    await asyncio.sleep(0.05)
