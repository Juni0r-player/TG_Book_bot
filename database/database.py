# Настраиваем после main.py

"""Данная база данных нужна, чтобы хранить текущий номер страницы, которую читает пользователь
и список закладок, которые пользователь сделал во время прочтения книги."""

# Создается словарь с данными о странице и закладках (закладки использую тип данных множество)
# Создаем шаблон заполнения словаря с пользователями
user_dict_template = {
    'page': 1,
    'bookmarks': set()
}

# Инициализируем "базу данных"
users_db = {}

"""Множество - это неупорядоченное коллекция УНИКАЛЬНЫХ элементов, т.е. 2 одинаковые закладки быть не могут
и таким образом - это упрощает нам работу"""
