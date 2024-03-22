from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardBuilder
from aiogram.types import KeyboardButton

CREATE_TEST_TEXT = '🧩 Создать тест'
MY_TESTS_TEXT = '🌟 Мои тесты'
TOP_TEXT = '🔝 Топ тестов'
CATALOGUE_TEXT = 'Каталог'
RANDOM_TEST_TEXT = '🎲 Случайный тест'
FRIEND_TEST = "👥Тесты дружбы"
MINI_TESTS = '📋Мини тесты'

def user_menu() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    builder.button(
        text=CREATE_TEST_TEXT
    )
    builder.row(
        KeyboardButton(
            text=TOP_TEXT
        ),
        KeyboardButton(
            text=RANDOM_TEST_TEXT
        )
    )
    
    builder.row(
        KeyboardButton(
            text=FRIEND_TEST
        ),
        KeyboardButton(
            text=MINI_TESTS
        )
    )


    

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