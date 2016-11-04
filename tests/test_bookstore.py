import unittest

from bookstore import Bookstore, Book, Author


class BookstoreTestCase(unittest.TestCase):
    def setUp(self):
        self.borges = Author("Jorge Luis Borges", "AR")
        self.poe = Author('Edgar Allan Poe', 'US')

        self.ficciones = Book("Ficciones", author=self.borges)
        self.aleph = Book("The Aleph", author=self.borges)
        self.raven = Book("The Raven", author=self.poe)

    def test_instantiate_bookstore(self):
        store = Bookstore("Rmotr's bookstore")
        self.assertEqual(store.name, "Rmotr's bookstore")
        self.assertEqual(store.get_books(), [])

    def test_add_book_to_bookstore(self):
        store = Bookstore("Rmotr's bookstore")
        self.assertEqual(store.get_books(), [])

        store.add_book(self.ficciones)
        self.assertEqual(store.get_books(), [self.ficciones])

        store.add_book(self.raven)
        self.assertEqual(store.get_books(), [self.ficciones, self.raven])

        # Test second store
        second_store = Bookstore("Second bookstore")
        self.assertEqual(second_store.get_books(), [])

        second_store.add_book(self.raven)
        self.assertEqual(second_store.get_books(), [self.raven])

    def test_search_bookstore_by_book_title(self):
        store = Bookstore("Rmotr's bookstore")

        store.add_book(self.ficciones)
        store.add_book(self.aleph)

        results = store.search_books(title='XYZ')
        self.assertEqual(results, [])

        results = store.search_books(title='ficc')
        self.assertEqual(results, [self.ficciones])

        results = store.search_books(title='The')
        self.assertEqual(results, [self.aleph])

        store.add_book(self.raven)
        results = store.search_books(title='The')
        self.assertEqual(results, [self.aleph, self.raven])

    def test_search_bookstore_by_book_author(self):
        store = Bookstore("Rmotr's bookstore")
        store.add_book(self.ficciones)
        store.add_book(self.aleph)

        austen = Author('Jane Austen', 'UK')

        results = store.search_books(author=austen)
        self.assertEqual(results, [])

        results = store.search_books(author=self.borges)
        self.assertEqual(results, [self.ficciones, self.aleph])

        results = store.search_books(author=self.poe)
        self.assertEqual(results, [])

        store.add_book(self.raven)
        results = store.search_books(author=self.poe)
        self.assertEqual(results, [self.raven])

    def test_search_bookstore_by_both_author_and_title(self):
        store = Bookstore("Rmotr's bookstore")
        store.add_book(self.ficciones)
        store.add_book(self.aleph)
        store.add_book(self.raven)

        results = store.search_books(title='ficc', author=self.borges)
        self.assertEqual(results, [self.ficciones])


class AuthorTestCase(unittest.TestCase):
    def test_author_creation(self):
        borges = Author("Jorge Luis Borges", "AR")
        poe = Author('Edgar Allan Poe', 'US')

        self.assertEqual(borges.name, "Jorge Luis Borges")
        self.assertEqual(borges.nationality, "AR")

        self.assertEqual(poe.name, "Edgar Allan Poe")
        self.assertEqual(poe.nationality, "US")

    def test_get_books_from_author(self):
        borges = Author("Jorge Luis Borges", "AR")
        ficciones = Book("Ficciones", author=borges)
        aleph = Book("The Aleph", author=borges)

        self.assertEqual(borges.get_books(), [ficciones, aleph])


class BookTestCase(unittest.TestCase):
    def test_book_creation(self):
        borges = Author("Jorge Luis Borges", "AR")
        poe = Author('Edgar Allan Poe', 'US')

        ficciones = Book("Ficciones", author=borges)
        aleph = Book("The Aleph", author=borges)
        raven = Book("The Raven", author=poe)

        self.assertEqual(ficciones.title, "Ficciones")
        self.assertEqual(ficciones.author, borges)

        self.assertEqual(aleph.title, "The Aleph")
        self.assertEqual(aleph.author, borges)

        self.assertEqual(raven.title, "The Raven")
        self.assertEqual(raven.author, poe)
