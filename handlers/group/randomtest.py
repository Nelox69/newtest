import random

from aiogram import Router, Bot, types, html
from aiogram.filters import Command

from database import crud
from utils import texts


router = Router()


@router.message(Command('random'))
async def randomtest(message: types.Message, bot: Bot):
    source = message.text.split(' ')[1] if ' ' in message.text else None
    group, is_created = await crud.create_group(
        message.chat.id,
        html.quote(message.chat.title),
        message.chat.username,
        source
    )

    tests = await crud.get_random_deftest(
        user_id=message.from_user.id
    )

    bot_user = await bot.me()
    test_type = random.choice(tests)['test_type']
    await message.answer(
        texts.RANDOM_TEST_GROUP.format(
            name=message.from_user.first_name,
            test_name=texts.DEFAULT_TESTS_NAMES[test_type],
            bot_username=bot_user.username,
            test_type=test_type,
            user_id=message.from_user.id
        )
    )

