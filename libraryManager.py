class LibraryManager:
    def __init__(self):
        self.library = Library()

    def add_sample_books(self):
        book1 = Book("1984", "George Orwell", 1949, "978-0451524935")
        book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960, "978-0061120084")
        book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "978-0743273565")

        self.library.add_book(book1)
        self.library.add_book(book2)
        self.library.add_book(book3)

    def run(self):
        self.add_sample_books()
        self.library.display_books()

        # Удаление книги
        self.library.remove_book("978-0451524935")
        self.library.display_books()