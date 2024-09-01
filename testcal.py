import unittest
from library_Management import Book,Library

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()

    def test_add_book_success(self):
        self.library.add_book("1234567890", "Book 1", "Author 1", 2020)
        self.assertIn("1234567890", self.library.books)

    def test_add_book_duplicate_isbn(self):
        self.library.add_book("1234567890", "Book 1", "Author 1", 2020)
        with self.assertRaises(ValueError):
            self.library.add_book("1234567890", "Book 2", "Author 2", 2021)

    def test_borrow_book_success(self):
        self.library.add_book("1234567890", "Book 1", "Author 1", 2020)
        self.library.borrow_book("1234567890")
        book = self.library.books["1234567890"]
        self.assertFalse(book.is_available)

    def test_borrow_book_not_found(self):
        with self.assertRaises(ValueError):
            self.library.borrow_book("invalid isbn")

    def test_borrow_book_book_not_available(self):
        self.library.add_book("1234567890", "Book 1", "Author 1", 2020)
        self.library.borrow_book("1234567890")
        with self.assertRaises(ValueError):
            self.library.borrow_book("1234567890")

    def test_return_book_success(self):
        self.library.add_book("1234567890", "Book 1", "Author 1", 2020)
        self.library.borrow_book("1234567890")
        self.library.return_book("1234567890")
        book = self.library.books["1234567890"]
        self.assertTrue(book.is_available)

    def test_return_book_book_not_found(self):
        with self.assertRaises(ValueError):
            self.library.return_book("invalid isbn")

    def test_view_available_books(self):
        self.library.add_book("1234567890", "Book 1", "Author 1", 2020)
        self.library.add_book("2345678901", "Book 2", "Author 2", 2021)
        self.library.borrow_book("1234567890")
        available_books = self.library.view_available_books()
        self.assertEqual(len(available_books), 1)
        self.assertEqual(available_books[0].isbn, "2345678901")

if __name__ == "__main__":
    unittest.main()