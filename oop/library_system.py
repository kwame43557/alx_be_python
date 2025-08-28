class Book:
    def __init__(self, title, author):
        """Base class for all books."""
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """Derived class for eBooks, with additional file size attribute."""
        super().__init__(title, author)  # Call base class __init__
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Derived class for printed books, with additional page count attribute."""
        super().__init__(title, author)  # Call base class __init__
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """Library holds a collection of books (composition)."""
        self.books = []

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook to the collection."""
        self.books.append(book)

    def list_books(self):
        """Print details of each book in the library."""
        for book in self.books:
            print(book)