# # Настраивается после lexicon.
# """Отвечает за кнопку меню в боте"""
from aiogram import Bot
from aiogram.types import BotCommand # Импортируем класс ради функции set_my_commands

from lexicon.lexicon import LEXICON_COMMANDS


# Функция для настройки кнопки Menu бота
async def set_main_menu(bot: Bot):
    main_menu_commands = [BotCommand(
        command=command,
        description=description
    ) for command,
        description in LEXICON_COMMANDS.items()]
    await bot.set_my_commands(main_menu_commands) # За счет функции set_my_command появляется кнопка меню.