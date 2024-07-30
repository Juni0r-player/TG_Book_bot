# Настраиваем после datavase.py

"""Модуль для подготовки книги, чтобы боту было удобно с ней работать"""

"""Для того, чтобы было удобно работать с книгой - нам нужно преобразовать текстовый файл книги в словарь,
где ключами будут номера страниц, а значениями - тексты этих страниц. """

import os # Нужна для работы с файловой системой ПК. Когда указываются пути к файлам
import sys # Опять же нужна для работы с файлами

BOOK_PATH = "book/book.txt" # Указали путь к модулю в папке book, который лежит в этом же проекте (репозитории)
PAGE_SIZE = 1050 # Максимальное кол-во букв для одной страницы.

book: dict[int, str] = {}

# Создали функцию, начинается с нижнего подчеркивания, что говорит о том-что она используется только в этом модуле.
# Функция возвращает строку с текстом страницы и ее размер.
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    end_signs = ',.!:;?'
    counter = 0
    if len(text) < start + size:
        size = len(text) - start
        text = text[start:start + size]
    else:
        if text[start + size] == '.' and text[start + size - 1] in end_signs:
            text = text[start:start + size - 2]
            size -= 2
        else:
            text = text[start:start + size]
        for i in range(size - 1, 0, -1):
            if text[i] in end_signs:
                break
            counter = size - i
    page_text = text[:size - counter]
    page_size = size - counter
    return page_text, page_size

# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(file=path, mode='r', encoding='utf-8') as file:
        text = file.read()
    start, page_number = 0, 1
    while start < len(text):
        page_text, page_size = _get_part_text(text, start, PAGE_SIZE)
        start += page_size
        book[page_number] = page_text.strip()
        page_number += 1
"""После того, как отработает функция prepare_book, получится словарь вида:
book = {1: 'Здесь текст первой страницы книги',
        2: 'Здесь текст второй страницы книги',
        3: 'Здесь текст третьей страницы книги',
        4: 'Здесь текст четвертой страницы книги',
        5: 'Здесь текст пятой страницы книги',
        6: 'Здесь текст шестой страницы книги'}"""

prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))
"""Строка prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH))) может показаться несколько сложной,
но суть ее работы сводится к тому, чтобы универсализировать запуск бота в разных операционных системах из разных редакторов кода.
Дело в том, что путь в константе BOOK_PATH записан понятным для операционных систем на базе UNIX, к которым относятся и Linux и MacOS,
но будет непонятен операционной системе Windows, потому что разделителем между директориями и
файлами в Windows служит обратный слеш - \., а не прямой /, как в BOOK_PATH. Чтобы путь был понятен всем операционным
системам его нужно нормализовать и за это отвечает метод normpath из встроенной библиотеки os. Отсюда конструкция os.path.normpath(BOOK_PATH)."""