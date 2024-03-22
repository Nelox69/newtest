from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardBuilder
from utils.texts import DEFAULT_TESTS_NAMES, QUIZ_TEST_NAMES

def default_test_menu(user_id: int, tests) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for i in tests:
        builder.button(text=DEFAULT_TESTS_NAMES[i.test_type], callback_data=f'show_{i.test_type}_{user_id}')
    builder.button(text='Шаблоны тестов', callback_data=f'patterns')
    for test in QUIZ_TEST_NAMES.keys():
        builder.button(
        text=QUIZ_TEST_NAMES[test],
        callback_data=f'deftest_{test}'
    )
    builder.button(
        text='Квиз: Гарри Потер',
        callback_data='harrypotter_test'
    )
    builder.adjust(1)

    return builder.as_markup(resize_keyboard=True)

def tests_petterns():
    builder = InlineKeyboardBuilder()
    for test in DEFAULT_TESTS_NAMES.keys():
        builder.button(
        text=DEFAULT_TESTS_NAMES[test],
        callback_data=f'deftest_{test}'
    )
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)

def pattern(test_type: str):
    builder = InlineKeyboardBuilder()
    builder.button(
        text='👍 Продолжить',
        callback_data=f'startdeftest_{test_type}'
    )
    builder.button(
        text='⬅️ Вернуться к списку',
        callback_data='back_to_patterns'
    )

    builder.adjust(1)

    return builder.as_markup(resize_keyboard=True)

def answers(test_type: str, options, q_index: int, action):
    builder = InlineKeyboardBuilder()
    for i, j in enumerate(options, 0):
        builder.button(
            text=j,
            callback_data=f'{action}_{test_type}_{q_index}_{i}'
        )

    builder.adjust(1)

    return builder.as_markup(resize_keyboard=True)

def confirm_passing(
        user_id,
        test_type
    ):
    builder = InlineKeyboardBuilder()
    builder.button(
        text='📋 Пройти тест',
        callback_data=f'startpassdeftest_{test_type}_{user_id}'
    )

    return builder.as_markup(resize_keyboard=True)

def confirm_harry_test():
    builder = InlineKeyboardBuilder()
    builder.button(
        text='Начать',
        callback_data=f'startharrytest'
    )

    return builder.as_markup(resize_keyboard=True)
    
def showing_test(
        user_id,
        test_type
    ):
    builder = InlineKeyboardBuilder()
    builder.button(
        text='🔗 Получить ссылку',
        callback_data=f'getlink_{test_type}_{user_id}'
    )
    builder.button(
        text='✍️ Изменить мои ответы',
        callback_data=f'changeans_{test_type}_{user_id}'
    )

    builder.adjust(1)

    return builder.as_markup(resize_keyboard=True)

