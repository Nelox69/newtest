from aiogram import Router, F, Bot, types
from aiogram.filters import Command

from database import crud
from keyboards.user_menu import TOP_TEXT
from keyboards.mandatory_subscription import unsubbed
from utils import texts
from utils.admin import show_ad_pm, check_follow
from keyboards.tests.for_test_pass import group_result_menu
from utils.telegram import get_text_for_test

from keyboards.tests import for_top_tests

router = Router()


@router.message(F.text == TOP_TEXT)
async def handle_command(message: types.Message, bot: Bot):
    user = await crud.get_user(message.from_user.id)
    follows = await check_follow(user, bot)
    if follows and "subs" in follows:
        return await message.answer(
            texts.SUB_TEXT,
            reply_markup=unsubbed(follows)
        )

    tests = await crud.get_top_tests()
    await message.answer(
        text='<b>Топ тестов</b>',
        reply_markup=for_top_tests.list_of_top(
            list_of_tests=tests,
            page=0
        )
    )

    await show_ad_pm(message.from_user.id, bot)

@router.callback_query(F.data.startswith('test_'))
async def handler(call: types.CallbackQuery, bot: Bot):
    test_id=int(call.data.split('_')[1])
    test = await crud.get_test_by_id(
        test_id=test_id,
        prefetch_answers=True
    )
    if test is None:
        return await call.message.answer('Тестов пока нет.')

    message_text = get_text_for_test(test, True)
    await call.message.answer(message_text, reply_markup=group_result_menu(test.id, (await bot.me()).username))
    await crud.increment_pass_counter(int(test.id))

@router.callback_query(F.data.startswith('backlist'))
async def backlist(call: types.CallbackQuery):
    page = int(call.data.split('_')[1])
    tests = await crud.get_top_tests()
    await call.message.edit_text(
        text='Топ тестов',
        reply_markup=for_top_tests.list_of_top(
            list_of_tests=tests,
            page=page-1
        )
    )

@router.callback_query(F.data.startswith('nextlist'))
async def backlist(call: types.CallbackQuery):
    page = int(call.data.split('_')[1])
    tests = await crud.get_top_tests()
    
    await call.message.edit_text(
        text='Топ тестов',
        reply_markup=for_top_tests.list_of_top(
            list_of_tests=tests,
            page=page+1
        )
    )