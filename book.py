class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn

    def get_info(self):
        return f"{self.title} by {self.author}, {self.year} (ISBN: {self.isbn})"