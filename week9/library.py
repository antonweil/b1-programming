class book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN

    def info(self):
        return f"Title: {self.title}, Written by: {self.author}, ISBN: {self.ISBN}"
    
class library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        return f"Added: {book.info()}"
    
    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                return f"Removed: {book.info()}"
        return f"book with title {title} not found."
    
    def list_books(self):
        if not self.books:
            return f"{self.name} has no books."
        result = f"\n=== Books in {self.name} ===\n"
        for i, book in enumerate(self.books, 1):
            result += f"{i}. {book.info()}\n"
        return result
    
    def search(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return f"book found: book info: {book.info()}"

library = library("City Library")
# Create and add books
book1 = book("Python Crash Course", "Eric Matthes", "978-1593279288")
book2 = book("Clean Code", "Robert Martin", "978-0132350884")
book3 = book("The Pragmatic Programmer", "Hunt & Thomas", "978-0201616224")
print(library.add_book(book1))
print(library.add_book(book2))
print(library.add_book(book3))
# List all books
print(library.list_books())
# Search for a book
print(library.search("Python"))
# Remove a book
print(library.remove_book("Clean Code"))
print(library.list_books())