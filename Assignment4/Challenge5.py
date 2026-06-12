# Challenge 5: Library Book Management

# Create a Book class.
# Requirements:
# - Create instance variables: book_id, title, author.
# - Create a class variable library_name = "City Library".
# - Create an instance method display_book_info().
# - Create a class method change_library_name() to change the library name.
# - Create at least 3 book objects and display their information before and after changing the library name.

print("Challenge 5: Library Book Management")
print()

class Book:
    library_name = "City Library"

    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

    def display_book_info(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Library:", Book.library_name)
        print()

    @classmethod
    def change_library_name(cls, new_name):
        cls.library_name = new_name


# Objects
b1 = Book(1, "Python Basics", "S. Sayyed")
b2 = Book(2, "Data Science", "A. Wagh")
b3 = Book(3, "AI Fundamentals", "S. Patil")

print("Before Change:")
b1.display_book_info()
b2.display_book_info()
b3.display_book_info()
print()

Book.change_library_name("Pune Library")
print("After Change:")
b1.display_book_info()
b2.display_book_info()
b3.display_book_info()