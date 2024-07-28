# Данный файл 3й по счету настройки, после енв.

"""Чувствительные данные, такие как токен, айди админа, пароли, логины
лучше хранить в переменных окружения, а чтобы использовать эти данные, будем
загружать через config.py в нашего бота. Для этого мы имортируем дата классы,
в которых будем хранить наши данные"""

from dataclasses import dataclass
from environs import Env

# Создается датакласс для хранения токена и айди админа
@dataclass
class TgBot:
    token: str # В данной строке будет храниться токен бота
    admin_ids: str # В данной строке будет храниться айди админа

@dataclass
class Config:
    tg_bot: TgBot # Мы как бы создали базу бота, который будет тянуть данные из вышестоящего датакласса.

# Создается функция, которая умеет читать секретный env файл
# и возвращать экземпляр класса с подтянутыми данными оттуда
def load_config(path: str | None = None) -> Config:
    env = Env() # Создали переменную для чтения файлика
    env.read_env(path) # прочитай вставленный файлик
    return Config( # Верни загруженного бота с таким то токеном и такими то админами
        tg_bot=TgBot(
        env.read_env("BOT_TOKEN"), # Прочитай файл енв и вытащи токен бота и админов
        admin_ids=list(map(int, env.list("ADMIN_IDS")))
    )
)