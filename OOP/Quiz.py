class Book:
    total_books = 0

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        Book.total_books += 1

    @classmethod
    def get_total_books(cls):
        return cls.total_books
    
    @staticmethod
    def is_valid_title(title):
        return isinstance (title, str) and len (title) > 0
            
    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"
  
    def __repr__(self):
        return f"Book(title={self.title!r}, author={self.author!r}, year={self.year!r})"

b1  = Book("1984", "George Orwell", 1949)
b2  = Book("To Kill a Mockingbird", "Harper Lee", 1960)

print(b1)
print(repr(b2))

print(Book.get_total_books())
print(Book.is_valid_title("The Great Gatsby"))
print(Book.is_valid_title(""))