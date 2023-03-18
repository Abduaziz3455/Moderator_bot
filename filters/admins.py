from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
import re


class AdminFilter(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        member = await message.chat.get_member(message.from_user.id)
        return member.is_chat_admin()


class RegexFilter(BoundFilter):
    async def check(self, message: types.Message):
        regex = r'@(?!_)(?!.*?\_{2})[a-zA-Z0-9_]{5,32}(?<!_)|https?://(?:t(?:elegram)?\.me|telegram\.org)/\S*'
        pattern = re.findall(regex, message.text)
        if pattern:
            return True
