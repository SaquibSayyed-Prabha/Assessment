# Assignment 3 - Python OOP Challenges
print("Assignment 3 - Python OOP Challenges")
print()


# Challenge 1: Student Management System

# Create a Student class.
# Requirements:
# - Create instance variables: name, age, course.
# - Create a class variable school_name = "ABC College".
# - Create an instance method display_student() to display student details.
# - Create a class method change_school_name() to change the school name.
# - Create 2 student objects and demonstrate the class method

print("Challenge 1: Student Management System")
print()

class Student:
    school_name = "ABC College"      # Class Variable

    def __init__(self, name, age, course):
        self.name = name                    # Instance variables
        self.age = age
        self.course = course

    def display_student(self):              # Instance method
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        print("School:", Student.school_name)
        print()

    @classmethod                            # Class Method
    def change_school_name(cls, new_name):
        cls.school_name = new_name

# Creating Objects
s1 = Student("Saquib", 17, "AIML")
s2 = Student("Nikhil", 18, "AR")

print("Before Change:")
s1.display_student()
s1.display_student()

Student.change_school_name("XYZ College")

print("\nAfter Change:")
s1.display_student()
s2.display_student()
print("\n\n")



# Challenge 2: Employee Counter

# Create an Employee class.
# Requirements:
# - Create instance variables: emp_id, emp_name, salary.
# - Create a class variable employee_count to count total employees.
# - Increment the count whenever a new employee object is created.
# - Create an instance method display_employee().
# - Create a class method show_total_employees() to display the total employee count.

print("Challenge 2: Employee Counter")
print()

class Employee:
    employee_count = 0      # Class Variable

    def __init__(self, emp_id, emp_name, salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.salary = salary

        Employee.employee_count += 1

    def display_employee(self):
        print("ID:", self.emp_id)
        print("Name:", self.emp_name)
        print("Salary:", self.salary)
        print()

    @classmethod
    def show_total_employees(cls):                        # We use 'cls' to access class variables.
        print("Total Employees:", cls.employee_count)

# Creating Objects
e1 = Employee(101, "Saquib", 90000)
e2 = Employee(102, "Atharva", 80000)
e3 = Employee(103, "Suraj", 75000)

e1.display_employee()
Employee.show_total_employees()
print("\n\n")



# Challenge 3: Bank Account System

# Create a BankAccount class.
# Requirements:
# - Create instance variables: account_number, holder_name, balance.
# - Create a class variable bank_name = "State Bank of India".
# - Create instance methods deposit(amount), withdraw(amount), check_balance().
# - Create a class method change_bank_name() to update the bank name.
# - Create multiple account objects and test all methods.

print("Challenge 3: Bank Account System")
print()

class BankAccount:
    bank_name = "SBI"

    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(amount, "deposited successfully")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(amount, "withdrawn successfully")
        else:
            print("Insufficient Balance")

    def check_balance(self):
        print("Current Balance:", self.balance)

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

# Objects
a1 = BankAccount(1001, "Saquib", 10000)
a2 = BankAccount(1002, "Atharva", 10000)

a1.deposit(2000)
a1.withdraw(1000)
a1.check_balance()

BankAccount.change_bank_name("HDFC")
print("New Bank Name:", BankAccount.bank_name)
print("\n\n")



# Challenge 4: Mobile Store Inventory

# Create a Mobile class.
# Requirements:
# - Create instance variables: brand, model, price.
# - Create a class variable discount_percentage = 10.
# - Create an instance method display_mobile().
# - Create an instance method calculate_discount_price().
# - Create a class method change_discount(new_discount) to update the discount percentage for all mobiles.

print("Challenge 4: Mobile Store Inventory")
print()

class Mobile:
    discount_percentage = 10

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_mobile(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)

    def calculate_discount_price(self):
        discount = (self.price * Mobile.discount_percentage) / 100
        final_price = self.price - discount
        print("Discounted Price:", final_price)

    @classmethod
    def change_discount(cls, new_discount):
        cls.discount_percentage = new_discount

# Objects
m1 = Mobile("Samsung", "M14", 15000)
m2 = Mobile("Realme", "Narzo", 12000)

m1.display_mobile()
m1.calculate_discount_price()

Mobile.change_discount(20)
print("\nAfter Discount Change:")
m2.calculate_discount_price()
print("\n\n")



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