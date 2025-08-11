class Book:
    total_books = 0
    
    def __init__(self, title,isbn):
        self.title = title
        self.isbn = isbn
        Book.total_books += 1
    def read(self):
        return(f"Reading '{self.title}'")
    @classmethod
    def get_total_books(cls):
        return cls.total_books
    @staticmethod
    def is_isbn_valid(isbn):
        degits = isbn.replace("-", "")
        return len(degits) in [10, 13]

b1 = Book("The Great Gatsby", "978-5-4461-1173-7")

print (Book.get_total_books())
print (b1.read())
print (Book.is_isbn_valid(b1.isbn))