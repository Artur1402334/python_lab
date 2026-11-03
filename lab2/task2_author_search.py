import csv

FILE_NAME = 'books.csv'
MAX_PRICE = 200
ID_COLUMN = 0
TITLE_COLUMN = 1
AUTHOR_COLUMN = 3
PRICE_COLUMN = 7


def search_author():
    while True:
        search = input('Введите автора: ').strip().lower()
        if search == '0' or search == '':
            break
        found = 0
        with open(FILE_NAME, encoding='cp1251', newline='') as csv_file:
            table = csv.reader(csv_file, delimiter=';')
            next(table)  # скип строки с заголовками
            for row in table:
                price = float(row[PRICE_COLUMN].replace(',', '.'))
                author = row[AUTHOR_COLUMN].lower()
                if search in author and price <= MAX_PRICE:
                    found += 1
                    print(f'{row[ID_COLUMN]} | {row[TITLE_COLUMN]} | '
                        f'{row[AUTHOR_COLUMN]} | {price} руб.')

        if found == 0:
            print('Ничего не найдено.')
        else:
            print(f'Найдено записей: {found}')


search_author()