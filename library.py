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