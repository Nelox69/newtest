from aiogram import Router, F

from . import new_group
from . import start_cmd
from . import randomtest

group_router = Router()
group_router.message.filter(F.chat.type != 'private')
group_router.include_routers(
    new_group.router,
    start_cmd.router,
    randomtest.router
)
