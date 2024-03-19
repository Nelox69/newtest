from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardBuilder


CREATE_TEST_TEXT = '🧩 Создать тест'
MY_TESTS_TEXT = '🌟 Мои тесты'
TOP_TEXT = '🔝 Топ тестов'
CATALOGUE_TEXT = 'Каталог'
RANDOM_TEST_TEXT = '🎲 Случайный тест'

def user_menu() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    builder.button(
        text=CREATE_TEST_TEXT
    )
    builder.button(
        text=MY_TESTS_TEXT
    )
    
    builder.button(
        text=TOP_TEXT
    )
    builder.button(
        text=RANDOM_TEST_TEXT
    )
    builder.adjust(2)

    return builder.as_markup(resize_keyboard=True)

def anon_menu() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    builder.button(text='🔎 Найти собеседника')
    builder.button(text='👤 Мой профиль')
    builder.button(text='🔙Назад')
    builder.adjust(1)

    return builder.as_markup(resize_keyboard=True)

def anon_test(user_id: int) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(text='Пройти опрос', callback_data=f'anontest_{user_id}')

    return builder.as_markup(resize_keyboard=True)

def cancel_anon_test() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(text='❌ Отменить прохождение опроса', callback_data='anonstop')

    return builder.as_markup(resize_keyboard=True)