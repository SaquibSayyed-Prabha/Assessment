# Q5: Create a Book class and create multiple objects to store book information.
print("Q5: Create a Book class and create multiple objects to store book information.")
class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    def display_book(self):
        print("Book Title: ", self.title)
        print("Author Name: ", self.author)
        print(f"Price: {self.price}$")
        print()

b1 = Book("Let's explore Python", "S.Sayyed", 20 )
b2 = Book("Introduction to ML", "S.Patil", 25)
b3 = Book("AI Fundamentals", "A.Wagh", 29)

b1.display()
b2.display()
b3.display()