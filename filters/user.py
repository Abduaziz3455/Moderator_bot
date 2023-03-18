from aiogram.types import Message
from aiogram.dispatcher.filters import BoundFilter

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class IsUser(BoundFilter):
    async def check(self, message: Message):
        chat_admins = []
        chat_id = message.chat.id
        admins = await bot.get_chat_administrators(chat_id)
        for i in range(len(admins)):
            chat_admins.append(admins[i]['user']['id'])
        return message.from_user.id not in chat_admins
