import csv

FILE_NAME = 'books.csv'
TOP_COUNT = 20
ID_COLUMN = 0
TITLE_COLUMN = 1
ISSUES_COLUMN = 8


def show_top():
    totals = {}  # ID книги - сумма выдач
    titles = {}  # ID книги - название
    with open(FILE_NAME, encoding='cp1251', newline='') as csv_file:
        table = csv.reader(csv_file, delimiter=';')
        next(table)
        for row in table:
            book_id = row[ID_COLUMN]
            if book_id not in totals:
                totals[book_id] = 0
                titles[book_id] = row[TITLE_COLUMN]
            totals[book_id] += int(row[ISSUES_COLUMN])

    ranking = []
    for book_id in totals:
        ranking.append((totals[book_id], titles[book_id]))
    ranking.sort(reverse=True)

    for place, book in enumerate(ranking[:TOP_COUNT], start=1):
        print(f'{place}. {book[1]} - выдач: {book[0]}')


show_top()