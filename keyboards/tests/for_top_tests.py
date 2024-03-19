from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardBuilder
from aiogram.types import InlineKeyboardButton

def list_of_top(
        list_of_tests,
        page
    ):
    builder = InlineKeyboardBuilder()
    for i in range((page)*10,(page)*10+10):
            try:
                builder.button(
                    text=f'{i+1}. {list_of_tests[i].name}',
                    callback_data=f'test_{list_of_tests[i].id}'
                )
            except IndexError:
                break

    menu = []
    if page != 0:
        menu.append(
            InlineKeyboardButton(
            text='⬅️',
            callback_data=f'backlist_{page}'
            )
        )

    all_pages = len(list_of_tests)//10
    menu.append(
        InlineKeyboardButton(
            text=f'{page+1}/{all_pages+1}',
        callback_data='None'
        )
    )
    if page < all_pages:
        menu.append(
        InlineKeyboardButton(
            text='➡️',
            callback_data=f'nextlist_{page}'
        )
        )
    builder.adjust(1)
    builder.row(
        *menu,

    )
        

    return builder.as_markup()

        
    
