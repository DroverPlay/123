class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn

    def get_info(self):
        return f"{self.title} by {self.author}, {self.year} (ISBN: {self.isbn})"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if not self.validate_book(book):
            print("Ошибка: Неправильные данные книги.")
        else:
            self.books.append(book)
            print(f"Книга '{book.title}' добавлена в библиотеку.")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Книга с ISBN {isbn} удалена.")
                return
        print("Ошибка: Книга с таким ISBN не найдена.")

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def display_books(self):
        if not self.books:
            print("В библиотеке нет книг.")
        else:
            for book in self.books:
                print(book.get_info())

    def validate_book(self, book):
        if not book.title or not book.author or book.year <= 0 or not book.isbn:
            return False
        return True

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