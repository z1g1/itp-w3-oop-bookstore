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
