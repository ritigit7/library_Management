class Book:
    def __init__(self, isbn, title, author, publication_year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_available = True

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, isbn, title, author, publication_year):
        """Add a new book to the library."""
        if isbn in self.books:
            raise ValueError("Book with ISBN {} already exists.".format(isbn))
        book = Book(isbn, title, author, publication_year)
        self.books[isbn] = book
        

    def borrow_book(self, isbn):
        """Borrow a book from the library."""
        if isbn not in self.books:
            raise ValueError("Book with ISBN {} not found.".format(isbn))
        book = self.books[isbn]
        if not book.is_available:
            raise ValueError("Book with ISBN {} is not available.".format(isbn))
        book.is_available = False
        print("Borrow book with ISBN {} successfully.".format(isbn))
        return book

    def return_book(self, isbn):
        """Return a borrowed book."""
        if isbn not in self.books:
            raise ValueError("Book with ISBN {} not found.".format(isbn))
        book = self.books[isbn]
        
        book.is_available = True
        print("Return  book with ISBN {} successfully.".format(isbn))

    def view_available_books(self):
        """View a list of all available books."""
        available_books = [book for book in self.books.values() if book.is_available]
        return available_books

# Example usage
library = Library()

# Add books
library.add_book("1234567890", "Book 1", "Author 1", 2020)
library.add_book("2345678901", "Book 2", "Author 2", 2019)

# Borrow a book
temp=library.borrow_book("1234567890")




# Try to borrow an unavailable book
try:
    library.borrow_book("1234567890")
except ValueError as e:
    print(e)

# Return a book
library.return_book("1234567890")

# View available books
available_books = library.view_available_books()
for book in available_books:
    print(book.title)
    
    
    
    
    