from csv import DictReader
import json
import logging

from helpers.paths import BOOKS, USERS


def file_reader():
    with open(USERS, 'r') as f:
        users = json.load(f)
    with open(BOOKS, 'r') as f:
        books = DictReader(f)

        with open('result.json', 'w') as res_f:
            result = []
            user_books = []
            for user in users:
                result_user = {k: v for k, v in user.items() if k in ['name', 'gender', 'address', 'age']}
                result_user['books'] = []
                result.append(result_user)

            for book in books:
                user_book = {k: v for k, v in book.items() if k.lower() in ['title', 'author', 'pages', 'genre']}
                user_books.append(user_book)

            user_books = iter(user_books)

            try:
                while user_books:
                    for user in result:
                        user['books'].append(next(user_books))
            except StopIteration as e:
                logging.info('All books are distributed by users ')

            result_data = json.dumps(result, indent=4)
            res_f.write(result_data)


if __name__ == '__main__':
    file_reader()








