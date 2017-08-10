import unittest
from bookstore import Book, Author


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
