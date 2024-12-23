class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
book = Book("The Book Thief", "Markus Zusak")
print(book.title, book.author)
del book.author
book2 = Book("Nineteen Eighty-Four", "George Orwell")
print(book2.title, book2.author)
print(book.author) 