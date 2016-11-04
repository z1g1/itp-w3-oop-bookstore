_and = lambda x, y: x and y
_or = lambda x, y: x or y


class Bookstore(object):
    def __init__(self, name):
        self.name = name
        self.books = []

    def get_books(self):
        return self.books

    def add_book(self, book):
        self.books.append(book)

    def search_books(self, title=None, author=None):
        results = []
        for book in self.books:

            has_title = title and title.lower() in book.title.lower()
            has_author = author and book.author == author
            both_present = title and author
            operator = _and if both_present else _or
            condition = operator(has_title, has_author)

            if condition:
                results.append(book)

        return results


class Author(object):
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_books(self):
        return self.books


class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author

        self.author.add_book(self)
