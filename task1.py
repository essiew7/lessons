class Book:
    def __init__(self, name, author, pages, date):
        self.name = name
        self.author = author
        self.pages = pages
        self.date = date


book1 = Book(name="Anna Karenina", author="Lev Tolstoi", pages=896, date=2017)
print(book1.name, book1.author)
