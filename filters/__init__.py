from aiogram import Dispatcher

from loader import dp
from .admins import AdminFilter
from .admins import RegexFilter
from .group_chat import IsGroup
from .user import IsUser
from .private_chat import IsPrivate


if __name__ == "filters":
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(RegexFilter)
    dp.filters_factory.bind(IsUser)
    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(IsPrivate)
