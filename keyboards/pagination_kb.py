# Настраиваем после main_menu.py (после кнопки меню)

"""Модуль pagination_kb.py отвечает за кнопки под сообщением со страницей книги."""

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup # Button для создание кнопки и Murkup для создания клавиатуры
from aiogram.utils.keyboard import InlineKeyboardBuilder # Для автоматического построения клавиатуры.
from lexicon.lexicon import LEXICON


# Функция, генерирующая клавиатуру для страницы книги
def create_pagination_keyboard(*buttons: str) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()
    # Добавляем в билдер ряд с кнопками
    kb_builder.row(*[InlineKeyboardButton(
        text=LEXICON[button] if button in LEXICON else button,
        callback_data=button) for button in buttons]
    )
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()
