# Настраиваем после файла конфиг

import asyncio
import logging

from aiogram import Bot, Dispatcher # Импортируем бота и диспетчера для работы бота
from aiogram.client.default import DefaultBotProperties # модуль, позволяющий читать HTML теги <b> и др, чтобы делать шрифт жирным или курсивом.
from aiogram.enums import ParseMode # Так-же для редактирования выводимых ботом сообщений.
from config_data.config import Config, load_config # Мы в конфиге настроили Config, который запускает бота и функцию load_config, которая читает env файл
from handlers import other_handlers, user_handlers # Импортируем хэндлеры основные и левые.
from keyboards.main_menu import set_main_menu # Импортируем кнопку меню

# Инициализируем логгер
logger = logging.getLogger(__name__)


# Функция конфигурирования и запуска бота
async def main():
    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    # # Строчка, которая выводит старт бот во время начала запуска бота
    logger.info('Starting bot')

    # Загружаем конфиг в переменную config, чтобы можно было с ней работать.
    config: Config = load_config()

    # Инициализируем бот и диспетчер
    bot = Bot(
        token=config.tg_bot.token, # Инициализация бота, получаем путем к токену
        default=DefaultBotProperties(parse_mode=ParseMode.HTML) # Включение модулей, для вывода жирного текста.
    )
    dp = Dispatcher()

    # # включение кнопки главное меню в боте.
    await set_main_menu(bot)

        # Регистрация роутеров в диспетчере.
    """Зачем это нужно? -
    Диспетчер - это грубо говоря список хендлеров, который обрабатывает апдейты, пришедшие с серверов телеграмм и распределяет
    эти апдейты по хендлерам. Но диспетчер работает только там, где мы его проинициализировали, а инициализацию его мы провели в этом модуле
    main.py строкой dp = Dispatcher(), соответственно и работать он будет только здесь и видит все апдейты только здесь.
    Но т.к. у нас проект разделен на пакеты, диспетчер не видит в других   модулях апдейты, вот мы их сюда таким образом и добавляем, чтобы
    апдейты с пакета handlers были видны и в этом файле."""
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    # Пропускаем апдейты и запускаем полинг. Это нужно, если проект разбит на множество пакетов как в данном случае.
    # и есть накопившиеся пакеты, которые мы регистрировали чуть выше в роутере.
    await bot.delete_webhook(drop_pending_updates=True)# пропускает ожидающие обновления. Нужно, если бот выключен, но в него отправляются сообщения, чтобы потом эти сообщения
    #при включении бота разом не высыпались на экран.
    await dp.start_polling(bot) # Запуск полинга, т.е. постоянный опрос сервера.


asyncio.run(main()) # запускаем функцию main.
