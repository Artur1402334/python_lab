import csv

FILE_NAME = 'books.csv'
MAX_TITLE_LENGTH = 30
TITLE_COLUMN = 1  # номер колонки с названием


def count_long_titles():
    count = 0
    with open(FILE_NAME, encoding='cp1251', newline='') as csv_file:
        table = csv.reader(csv_file, delimiter=';')
        next(table)  # скип первой строки
        for row in table:
            if len(row[TITLE_COLUMN]) > MAX_TITLE_LENGTH:
                count += 1
    print(f'Записей с названием длиннее {MAX_TITLE_LENGTH} символов: {count}')


count_long_titles()