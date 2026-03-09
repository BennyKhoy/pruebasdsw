import unittest
from unittest.mock import patch

from white_box.book_store import Book, BookStore


class TestBook(unittest.TestCase):
    """
    Book class unit tests.
    """

    def setUp(self):
        self.book = Book("Python", "Guido", 50.0, 10)

    def test_initialize_book(self):
        """
        Checks the Book initializes correctly.
        """
        self.assertEqual(self.book.title, "Python")
        self.assertEqual(self.book.author, "Guido")
        self.assertEqual(self.book.price, 50.0)
        self.assertEqual(self.book.quantity, 10)

    @patch("builtins.print")
    def test_display_book(self, mock_print):
        """
        Checks the display method prints book information.
        """
        self.book.display()

        mock_print.assert_any_call("Title: Python")
        mock_print.assert_any_call("Author: Guido")
        mock_print.assert_any_call("Price: $50.0")
        mock_print.assert_any_call("Quantity: 10")


class TestBookStore(unittest.TestCase):
    """
    BookStore class unit tests.
    """

    def setUp(self):
        self.store = BookStore()
        self.book = Book("Python", "Guido", 50.0, 10)

    def test_initialize_store(self):
        """
        Checks bookstore initializes empty.
        """
        self.assertEqual(self.store.books, [])

    @patch("builtins.print")
    def test_add_book(self, mock_print):
        """
        Checks a book can be added.
        """
        self.store.add_book(self.book)

        self.assertEqual(len(self.store.books), 1)
        mock_print.assert_called_with("Book 'Python' added to the store.")

    @patch("builtins.print")
    def test_display_books_empty(self, mock_print):
        """
        Checks message when no books exist.
        """
        self.store.display_books()
        mock_print.assert_called_with("No books in the store.")

    @patch("builtins.print")
    def test_display_books_with_items(self, mock_print):
        """
        Checks books are displayed when store has books.
        """
        self.store.add_book(self.book)
        self.store.display_books()

        mock_print.assert_any_call("Books available in the store:")

    @patch("builtins.print")
    def test_search_book_found(self, mock_print):
        """
        Checks search finds books by title.
        """
        self.store.add_book(self.book)

        self.store.search_book("Python")

        mock_print.assert_any_call("Found 1 book(s) with title 'Python':")

    @patch("builtins.print")
    def test_search_book_not_found(self, mock_print):
        """
        Checks search handles missing books.
        """
        self.store.search_book("Java")

        mock_print.assert_called_with("No book found with title 'Java'.")
