from aiogram import Router, types,  F, Bot
from aiogram.fsm.context import FSMContext

from database import crud

from keyboards import default_test
from keyboards.tests.for_test_pass import add_to_gr

from utils import texts

router = Router()

@router.callback_query(F.data.startswith('startdeftest'))
@router.callback_query(F.data.startswith('changeans'))
async def start_creating(call: types.CallbackQuery, state: FSMContext):
    test_type = call.data.split('_')[1]

    test_name = ''
    if test_type in texts.QUIZ_TEST_NAMES.keys():
        test_name = texts.QUIZ_TEST_NAMES[test_type]
    else:
        test_name=texts.DEFAULT_TESTS_NAMES[test_type]

    await call.message.delete()

    await call.message.answer_photo(
        photo=types.FSInputFile(f'utils/images/{test_type}/{0}.jpg'),
        caption=texts.DEFTEST_MESSAGE.format(
            test_name=test_name,
            current_q=1,
            all_q=len(texts.DEFAULT_TESTS[test_type]),
            question=texts.DEFAULT_TESTS[test_type][0]
        ),
        reply_markup=default_test.answers(
            test_type=test_type,
            options=texts.DEFAULT_ANS[test_type][0],
            q_index=0,
            action='create'
        )
    )
    await state.update_data(answers=[])

@router.callback_query(F.data.startswith('create'))
async def take_answer(call: types.CallbackQuery, state: FSMContext, bot: Bot):
    test_type = call.data.split('_')[1]
    question_index = call.data.split('_')[2]
    ans_index = call.data.split('_')[3]

    test_name = ''
    if test_type in texts.QUIZ_TEST_NAMES.keys():
        test_name = texts.QUIZ_TEST_NAMES[test_type]
    else:
        test_name=texts.DEFAULT_TESTS_NAMES[test_type]

    try:
        info = await state.get_data()
        
        await call.message.delete()

        await call.message.answer_photo(
            photo=types.FSInputFile(f'utils/images/{test_type}/{int(question_index)+1}.jpg'),
            caption=texts.DEFTEST_MESSAGE.format(
                test_name=test_name,
                current_q=int(question_index)+2,
                all_q=len(texts.DEFAULT_TESTS[test_type]),
                question=texts.DEFAULT_TESTS[test_type][int(question_index)+1]
            ),
            reply_markup=default_test.answers(
                test_type=test_type,
                options=texts.DEFAULT_ANS[test_type][int(question_index)+1],
                q_index=int(question_index) + 1,
                action='create'
            )
        )
        upd_answers = info['answers']
        upd_answers.append(ans_index)

        await state.update_data(answers=upd_answers)
    except IndexError: 
        info = await state.get_data()
        answers = info['answers']

        if test_type in texts.QUIZ_TEST_NAMES.keys():
            score = 0
            res_idx = 0
            for idx,ans in enumerate(answers, 0):
                score += texts.QUIZ_TEST_SCORES[test_type][idx][int(ans)]
            for idx,sc in enumerate(texts.QUIZ_REZULTS_BY_SCORES[test_type],0):
                if score in sc:
                    res_idx=idx
                    break

            res = list(texts.QUIZ_TEST_RESULTS[test_type].keys())[res_idx]

            await call.message.answer(
                text=texts.QUIZ_TEST_RESULTS[test_type][res]
            )
            
        else:
            
            is_created = await crud.get_or_create_test(
                user_id=call.from_user.id,
                answers=answers,
                test_type=test_type
            )
            me = await bot.me()

            if is_created:
                await call.message.answer(
                    text=texts.TEST_CREATED.format(
                        q_count=int(question_index) + 1,
                        bot_username=me.username,
                        test_type=test_type,
                        user_id=call.from_user.id
                    ),
                    reply_markup=add_to_gr(bot_username=me.username)
                )
            else:
                await call.message.answer(
                    text=texts.TEST_EDITED.format(
                        q_count=int(question_index) + 1,
                        bot_username=me.username,
                        test_type=test_type,
                        user_id=call.from_user.id
                    ),
                    reply_markup=add_to_gr(bot_username=me.username)
                )

        

