from aiogram import Router, Bot, types, html, F
from aiogram.filters import CommandObject, CommandStart, Command
from aiogram.fsm.context import FSMContext

from database import crud
from utils import texts
from utils.admin import send_greeting
from keyboards.user_menu import user_menu
from keyboards.default_test import confirm_passing

router = Router()

@router.message(F.text.startswith('/start dt_'))
async def start_passing_default_test(message: types.Message, state: FSMContext):
    await state.clear()
    
    await crud.create_user(
        message.from_user.id,
        html.quote(message.from_user.first_name),
        message.from_user.username,
        None
    )
    test_type = message.text.split('_')[1]
    user_id = int(message.text.split('_')[2])
    if user_id == message.from_user.id:
        return await message.answer('Нельзя пройти свой опрос')
    await message.answer(
        text=f'❔ Хочешь пройти тест "{texts.DEFAULT_TESTS_NAMES[test_type]}"',
        reply_markup=confirm_passing(
            user_id=user_id,
            test_type=test_type
            )
        )
    
@router.message(CommandStart())
async def start_cmd(message: types.Message, command: CommandObject, state: FSMContext, bot: Bot):
    await state.clear()

    await crud.create_user(
        message.from_user.id,
        html.quote(message.from_user.first_name),
        message.from_user.username,
        command.args
    )
    await send_greeting(bot, message.chat.id)

    await message.answer('💼 <b>Меню бота:</b>', reply_markup=user_menu())


@router.message(Command('menu'))
@router.message(Command('cancel'))
@router.message(F.text == '🔙Назад')
async def cancel_cmd(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer('💼 <b>Меню бота:</b>', reply_markup=user_menu())


@router.message(Command('help'))
async def cancel_cmd(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(texts.HELP_DESC, reply_markup=user_menu())
