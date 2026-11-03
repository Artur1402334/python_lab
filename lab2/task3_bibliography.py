import csv
import random

FILE_NAME = 'books.csv'
OUTPUT_NAME = 'bibliography.txt'
LINKS_COUNT = 20
TITLE_COLUMN = 1
AUTHOR_COLUMN = 3
DATE_COLUMN = 6


def make_bibliography():
    books = []
    with open(FILE_NAME, encoding='cp1251', newline='') as csv_file:
        table = csv.reader(csv_file, delimiter=';')
        next(table)  # пропускаем строку с заголовками
        for row in table:
            author = row[AUTHOR_COLUMN].strip()
            if author == '':
                author = '------'  # если автор не указан, ставим прочерк
            title = row[TITLE_COLUMN].strip()
            # дата выглядит как «15.10.2021 9:22»: делим её по точкам,
            # берём третий элемент («2021 9:22») и оставляем 4 символа (год)
            year = row[DATE_COLUMN].split('.')[2][:4]
            books.append(f'{author}. {title} - {year}')

    chosen = random.sample(books, LINKS_COUNT)

    with open(OUTPUT_NAME, 'w', encoding='utf-8') as output:
        for number, link in enumerate(chosen, start=1):
            output.write(f'{number}. {link}\n')

    print(f'Готово! Ссылок сохранено: {LINKS_COUNT}. Файл: {OUTPUT_NAME}')


make_bibliography()