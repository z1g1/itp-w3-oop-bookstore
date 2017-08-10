import unittest
from bookstore import Book, Author


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
