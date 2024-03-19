from aiogram import Router, types,  F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command

from database import crud

from keyboards import default_test
from keyboards.user_menu import MY_TESTS_TEXT

from utils import texts

router = Router()

@router.message(Command('mytests'))
@router.message(F.text == MY_TESTS_TEXT)
async def anonim_test(message: types.Message):
    user_id=message.from_user.id
    await message.answer(
        texts.DEFAULT_TEST_MENU
    )
    count = await crud.get_default_test_quantity(
        user_id=user_id
    )
    await message.answer(
        text=f'Список твоих тестов ({len(count)})',
        reply_markup=default_test.default_test_menu(user_id=user_id,tests=count)
    )

@router.callback_query(F.data == 'patterns')
@router.callback_query(F.data == 'back_to_patterns')
async def patterns_menu(call: types.CallbackQuery):
    await call.message.edit_text(
        text='Список шаблонов для тестов:',
        reply_markup=default_test.tests_petterns()
    )

@router.callback_query(F.data.startswith('deftest'))
async def patterns(call: types.CallbackQuery):
    test_type = call.data.split('_')[1]

    await call.message.edit_text(
        text=texts.PATTERNS_TEXT[test_type],
        reply_markup=default_test.pattern(test_type=test_type)
    )

@router.callback_query(F.data.startswith('show'))
async def show_test(call: types.CallbackQuery):
    test_type=call.data.split('_')[1]
    await call.message.answer(
        text=f'💬 Тест "{texts.DEFAULT_TESTS_NAMES[test_type]}"\n\n'
        '😋 Хочешь изменить его?',
        reply_markup=default_test.showing_test(
            user_id=call.from_user.id,
            test_type=test_type
        )
    )

@router.callback_query(F.data.startswith('getlink'))
async def get_link(call: types.CallbackQuery, bot: Bot):
    test_type=call.data.split('_')[1]
    me = await bot.me()
    await call.message.edit_text(
        text=f'💬 Тест "{texts.DEFAULT_TESTS_NAMES[test_type]}"\n\n'
        '👇 Ссылка на тест:\n\n'
        f't.me/{me.username}?start=dt_{test_type}_{call.from_user.id}'
    )


@router.message(F.text == '👥 Тест на дружбу')
async def friend_test(message: types.Message, state: FSMContext):
    exist = await crud.get_def_test(
        user_id=message.from_user.id,
        test_type='howfriend'
    )

    if exist:

        await message.answer(
            text=f'💬 Тест "Тест на дружбу"\n\n'
            '😋 Хочешь изменить его?',
            reply_markup=default_test.showing_test(
                user_id=message.from_user.id,
                test_type='howfriend'
            )
        )

    else:
        await message.answer(
        text=texts.DEFAULT_TESTS['howfriend'][0],
        reply_markup=default_test.answers(
            test_type='howfriend',
            options=texts.DEFAULT_ANS['howfriend'][0],
            q_index=0,
            action='create'
        )
    )
    await state.update_data(answers=[])

@router.message(F.text == '💘 Тест на совместимость')
async def friend_test(message: types.Message, state: FSMContext):
    exist = await crud.get_def_test(
        user_id=message.from_user.id,
        test_type='howlove'
    )

    if exist:

        await message.answer(
            text=f'💬 Тест "Тест на совместимость"\n\n'
            '😋 Хочешь изменить его?',
            reply_markup=default_test.showing_test(
                user_id=message.from_user.id,
                test_type='howlove'
            )
        )

    else:
        await message.answer(
        text=texts.DEFAULT_TESTS['howlove'][0],
        reply_markup=default_test.answers(
            test_type='howlove',
            options=texts.DEFAULT_ANS['howlove'][0],
            q_index=0,
            action='create'
        )
    )
    await state.update_data(answers=[])