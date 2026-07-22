class Library:

    def __init__(self, book_name, author):
        self.book_name = book_name
        self.author = author
        self.is_issued = False

    def display_book(self):
        print("\nBook Name :", self.book_name)
        print("Author :", self.author)

        if self.is_issued:
            print("Status : Issued")
        else:
            print("Status : Available")

    def issue_book(self):

        if self.is_issued:
            print("Book is already issued")
        else:
            self.is_issued = True
            print("Book issued successfully")

    def return_book(self):

        if self.is_issued:
            self.is_issued = False
            print("Book returned successfully")
        else:
            print("Book is already available")


book1 = Library("Python Programming", "Guido Van Rossum")

book1.display_book()

book1.issue_book()

book1.display_book()

book1.return_book()

book1.display_book()