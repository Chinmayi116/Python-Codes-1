class Library:
    def __init__(self):
        self.books = []

    def add(self, book):
        self.books.append(book)

    def show(self):
        print("Books:", self.books)

lib = Library()
lib.add("Python")
lib.add("DBMS")
lib.show()

