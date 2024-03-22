from aiogram import Router, types,  F, Bot
from aiogram.fsm.context import FSMContext

from database import crud

from keyboards import default_test

from keyboards.tests.for_test_pass import add_to_gr

from utils import texts

router = Router()

@router.callback_query(F.data == 'harrypotter_test')
async def confirm_passing(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer_photo(
        photo=types.FSInputFile(f'utils/images/harry/preview.jpg'),
        caption=texts.HARRY_POTER_DEMO,
        reply_markup=default_test.confirm_harry_test()
    )


@router.callback_query(F.data == 'startharrytest')
async def start_passing(call: types.CallbackQuery, state: FSMContext):

    await call.message.delete()

    await call.message.answer_photo(
        photo=types.FSInputFile(f'utils/images/harry/questions/0.jpg'),
        caption='Выберите, как зовут персонажа с фотографии:',
        reply_markup=default_test.answers(
            test_type='harry',
            options=texts.KNOWLEGE_TEST_OPTIONS[0],
            q_index=0,
            action='knowledge'
        )
    )

    await state.update_data(right_ans = 0)

@router.callback_query(F.data.startswith('knowledge'))
async def take_answer(call: types.CallbackQuery, state: FSMContext, bot: Bot):
    test_type = call.data.split('_')[1]
    question_index = call.data.split('_')[2]
    ans_index = call.data.split('_')[3]

    try:
        info = await state.get_data()
        right_ans = info['right_ans']
        await call.answer(show_alert=True,text=texts.KNOWLEGE_TEST_ANSWERS[int(question_index)][int(ans_index)])
        
        await call.message.delete()
        
        await call.message.answer_photo(
            photo=types.FSInputFile(f'utils/images/harry/questions/{int(question_index)+1}.jpg'),
            caption='Выберите, как зовут персонажа с фотографии:',
            reply_markup=default_test.answers(
                test_type=test_type,
                options=texts.KNOWLEGE_TEST_OPTIONS[int(question_index)+1],
                q_index=int(question_index) + 1,
                action='knowledge'
            )
        )
        right_ans += texts.KNOWLEGE_TEST_RIGHTS[int(question_index)][int(ans_index)]


        await state.update_data(right_ans=right_ans)
    except IndexError:
        info = await state.get_data()
        right_ans = info['right_ans']
        await call.answer(show_alert=True,text=texts.KNOWLEGE_TEST_ANSWERS[int(question_index)][int(ans_index)])
        right_ans += texts.KNOWLEGE_TEST_RIGHTS[int(question_index)][int(ans_index)]
        
        await call.message.answer_photo(
            photo=types.FSInputFile(f'utils/images/harry/results/{right_ans}.jpg'),
            caption=texts.KNOWLEGE_TEST_RESULTS[right_ans].format(name=call.from_user.first_name)
        )
        
        