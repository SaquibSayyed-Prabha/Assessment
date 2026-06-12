# Q21: Create a Library Management System using classes, objects, constructors, and methods.
print("Q21: Create a Library Management System using classes, objects, constructors, and methods.")
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"{book} added.")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"{book} removed.")
        else:
            print("Book not available.")

    def display_books(self):
        if self.books:
            print("Available Books:")
            for book in self.books:
                print("-", book)
        else:
            print("No books available.")


library = Library()

while True:
    print("\n1.Add Book \n2.Remove Book \n3.Show Books \n4.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        library.add_book(input("Book Name: "))
    elif choice == "2":
        library.remove_book(input("Book Name: "))
    elif choice == "3":
        library.display_books()
    elif choice == "4":
        break