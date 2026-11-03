import csv

FILE_NAME = 'books.csv'
GENRE_COLUMN = 12


def print_tags():
    tags = set()
    with open(FILE_NAME, encoding='cp1251', newline='') as csv_file:
        table = csv.reader(csv_file, delimiter=';')
        next(table)
        for row in table:
            for tag in row[GENRE_COLUMN].split('#'):
                tag = tag.strip()
                if tag != '':  #убираем пустой тег
                    tags.add(tag)

    print(f'Уникальных тегов: {len(tags)}')
    for tag in sorted(tags):
        print(tag)


print_tags()