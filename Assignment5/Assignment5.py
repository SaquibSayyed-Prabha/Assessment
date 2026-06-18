
# Assignment 5 - Python OOP Practical Questions
print("Assignment 5 - Python OOP Practical Questions")
print()

# Q1: Create a Student class with instance variables name and age. Create 3 objects and display their details.
print("Q1: Create a Student class with instance variables name and age. Create 3 objects and display their details.")
class Student:
    def __init__(self, name, age):
        self.name = name                   
        self.age = age
    
    def display_student(self):              
        print("Name:", self.name)
        print("Age:", self.age)
        print()

s1 = Student("Saquib", 17)
s2 = Student("Atharva", 18)
s3 = Student("Suraj", 18)

s1.display_student()
s2.display_student()
s3.display_student()
print()

# Q2: Create an Employee class with a constructor to initialize employee id, name, and salary.
print("Q2: Create an Employee class with a constructor to initialize employee id, name, and salary.")
class Emp:
    def __init__(self, emp_id, emp_name, salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.salary = salary

    def display(self):
        print("ID:", self.emp_id)
        print("Name:", self.emp_name)
        print("Salary:", self.salary)
        print()

e1 = Emp(101, "Saquib", 90000)
e1.display()
print()

# Q3: Create a Car class with instance variables brand and model. Write an instance method to display car details.
print("Q3: Create a Car class with instance variables brand and model. Write an instance method to display car details.")
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Car Brand: ", self.brand)
        print("Model: ", self.model)

c1 = Car("Mercedes", "Benz C")
c2 = Car("BMW", "X5")

c1.display()
c2.display()
print()

# Q4: Create a BankAccount class with deposit() and withdraw() instance methods.
print("Q4: Create a BankAccount class with deposit() and withdraw() instance methods.")
class BankAccount:
    def __init__(self):
        self.balance = 0

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

# Objects
a1 = BankAccount(1001, "Saquib")
a1.deposit(2000)
a1.withdraw(1000)
a1.check_balance()
print()

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
print()

# Q6: Create a Mobile class with a constructor and display mobile details using an instance method.
print("Q6: Create a Mobile class with a constructor and display mobile details using an instance method.")
class Mobile:
    def __init__(self, brand, model, ram, storage, price):
        self.brand = brand
        self.model = model
        self.ram = ram
        self.storage = storage
        self.price = price

    def display_mob(self):
        print("Mobile Brand: ", self.brand)
        print("Model: ", self.model)
        print("RAM: ", self.ram)
        print("Storage", self.storage)
        print("Price", self.price)
        print()

m1 = Mobile("Samsung", "J7", 2, 16, 8000)
m1.display_mob()
print()

# Q7: Create a Company class with a class variable company_name shared by all employees.
print("Q7: Create a Company class with a class variable company_name shared by all employees.")
class Company:
    company_name = "Prabha Technology"

    def __init__(self, id, name):
        self.id = id
        self.name = name
        
    def display(self):
        print("Employee Name: ", self.name)
        print("Employee ID: ", self.id)
        print("Company name: ", Company.company_name)
print()

# Q8: Create a Product class with a class variable tax_rate and calculate the final product price.
print("Q8: Create a Product class with a class variable tax_rate and calculate the final product price.")
class Product:
    tax_rate = 0.15

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def final_price(self):
        return self.price + (self.price * Product.tax_rate)
    
    def display(self):
        print("Product Name: ", self.name)
        print("Price with tax: ", Product.final_price())
        print()

p1 = Product("Laptop", 50000)
p2 = Product("Mouse", 1000)

p1.display()
p2.display()
print()

# Q9: Create a Student class with a class method to update the school name for all students.
print("Q9: Create a Student class with a class method to update the school name for all students.")
class Student:
    school_name = "ABC School"
    def __init__(self, s_no, name):
        self.s_no = s_no
        self.name = name

    def display(self):
        print("Student Name: ", self.name)
        print("Roll no: ", self.s_no)
        print("School Name: ", Student.school_name)
        print()

    @classmethod
    def change_school_name(cls, new_name):
        cls.school_name = new_name

s1 = Student(1, "Saquib")
s1.display()
s1.change_school_name("XYZ School")
s1.display()
print()

# Q10: Create a Vehicle class with a class variable vehicle_count. Count the total number of vehicles created.
print("Q10: Create a Vehicle class with a class variable vehicle_count. Count the total number of vehicles created.")
class Vehicle:
    vehicle_count = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        vehicle_count +=1

    def show_vehicle(self):
        print("Vehicle Brand: ", self.brand)
        print("Model: ", self.model)
        print()
    
    @classmethod
    def display_count(cls):
        print("Total No. of vehicles: ", cls.vehicle_count)

v1 = Vehicle("Mercedes", "Benz")
v2 = Vehicle("BMW", "M3")
Vehicle.display_count()
print()

# Q11: Create a Calculator class with static methods add(), subtract(), multiply(), and divide().
print("Q11: Create a Calculator class with static methods add(), subtract(), multiply(), and divide().")
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        return a / b

print(Calculator.add(10, 5))
print(Calculator.subtract(10, 5))
print(Calculator.multiply(10, 5))
print(Calculator.divide(10, 5))
print()

# Q12: Create a TemperatureConverter class with a static method to convert Celsius to Fahrenheit.
print("Q12: Create a TemperatureConverter class with a static method to convert Celsius to Fahrenheit.")
class Temp_Conv:
    @staticmethod
    def c_to_f(c):
        return (c * 9/5) + 32

print(f"25 C = {Temp_Conv.c_to_f(25)}F")
print()

# Q13: Create a Utility class with a static method to check whether a number is even or odd.
print("Q13: Create a Utility class with a static method to check whether a number is even or odd.")
class Utility:
    @staticmethod
    def check_even_odd(num):
        if num % 2 == 0:
            return "Even"
        return "Odd"

print("The given no. is ", Utility.check_even_odd(7))
print()

# Q14: Create a Person class and a Student class that inherits from Person. Display inherited properties.
print("Q14: Create a Person class and a Student class that inherits from Person. Display inherited properties.")
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)     # super() is used to access elements from the parent class
        self.roll = roll

s = Student("Sayyed", 101)
print("Student Name: ", s.name)
print("Roll no: ", s.roll)
print()

# Q15: Create a Vehicle class and a Bike class that inherits from Vehicle. Add extra properties in Bike.
print("Q15: Create a Vehicle class and a Bike class that inherits from Vehicle. Add extra properties in Bike.")
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Bike(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

b = Bike("Honda", "Shine")
print("Bike Brand: ", b.brand)
print("Model: ", b.model)
print()

# Q16: Create a Shape class and inherit Circle and Rectangle classes from it.
print("Q16: Create a Shape class and inherit Circle and Rectangle classes from it.")
class Shape:
    def area(self):
        print("Area calculation not defined")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

c = Circle(5)
r = Rectangle(4, 6)

print("Circle Area:", c.area())
print("Rectangle Area:", r.area())
print()

# Q17: Create an Animal class and inherit Dog and Cat classes. Display different sounds using methods.
print("Q17: Create an Animal class and inherit Dog and Cat classes. Display different sounds using methods.")
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog says: Bark")

class Cat(Animal):
    def sound(self):
        print("Cat says: Meow")

d = Dog()
c = Cat()

d.sound()
c.sound()
print()

# Q18: Create a Person class with private variable __salary and access it using getter and setter methods.
print("Q18: Create a Person class with private variable __salary and access it using getter and setter methods.")
class Person:
    def __init__(self):
        self.__salary = 0

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

p = Person()
p.set_salary(50000)
print(p.get_salary())
print()

# Q19: Create a BankAccount class and implement encapsulation using private balance variable.
print("Q19: Create a BankAccount class and implement encapsulation using private balance variable.")
class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount()
acc.deposit(1000)
print(acc.get_balance())
print()

# Q20: Create an Employee class with private data and update it using setter methods.
print("Q20: Create an Employee class with private data and update it using setter methods.")
class Employee:
    def __init__(self):
        self.__name = ""

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

e = Employee()
e.set_name("Saquib")
print(e.get_name())
print()

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
print()

# Q22: Create a Hospital Management System using inheritance and encapsulation concepts.
print("Q22: Create a Hospital Management System using inheritance and encapsulation concepts.")
class Hospital:
    def __init__(self, hospital_name):
        self.hospital_name = hospital_name


class Patient(Hospital):
    def __init__(self, hospital_name, patient_name, disease):
        super().__init__(hospital_name)
        self.__disease = disease
        self.patient_name = patient_name

    def get_disease(self):
        return self.__disease


p = Patient("City Hospital", "Ahmed", "Fever")

print("Hospital:", p.hospital_name)
print("Patient:", p.patient_name)
print("Disease:", p.get_disease())
print()

# Q23: Create a School Management System using class variables, class methods, and instance methods.
print("Q23: Create a School Management System using class variables, class methods, and instance methods.")
class School:
    total_students = 0

    def __init__(self, name):
        self.name = name
        School.total_students += 1

    def display(self):
        print("Student:", self.name)

    @classmethod
    def student_count(cls):
        print("Total Students:", cls.total_students)

s1 = School("Suraj")
s2 = School("Rohit")
s3 = School("Atharva")

s1.display()
s2.display()
s3.display()

School.student_count()
print()

# Q24: Create an Online Shopping System using OOP concepts including inheritance.
print("Q24: Create an Online Shopping System using OOP concepts including inheritance.")
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f"Product: {self.name}")
        print(f"Price: ${self.price}")

class Electronics(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty

    def display(self):
        super().display()
        print(f"Warranty: {self.warranty} Years")

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)
        print(f"{product.name} added to cart.")

    def show_bill(self):
        total = 0

        print("\n===== CART ITEMS =====")
        for item in self.items:
            item.display()
            print("----------------")
            total += item.price

        print(f"Total Bill = ${total}")

# Objects
laptop = Electronics("Laptop", 2500, 2)
headphone = Electronics("Headphone", 10, 1)

# Cart
cart = ShoppingCart()
cart.add_product(laptop)
cart.add_product(headphone)

cart.show_bill()
print()

# Q25: Create a Mini ATM System using encapsulation, constructors, and instance methods.
print("Q25: Create a Mini ATM System using encapsulation, constructors, and instance methods.")
class Account:

    def __init__(self, username, password):
        self.username = username
        self.__password = password
        self.__balance = 0

    def verify_password(self, password):
        return self.__password == password

    def deposit(self, amount):

        if amount <= 0:
            print("Invalid amount.")
            return

        self.__balance += amount
        print(f"₹{amount} deposited successfully.")

    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid amount.")
            return

        if amount > self.__balance:
            print("Insufficient balance.")
            return

        self.__balance -= amount
        print(f"₹{amount} withdrawn successfully.")

    def check_balance(self):
        print(f"Current Balance: ₹{self.__balance}")


class ATM:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        username = input("Enter Username: ")

        if username in self.accounts:
            print("Username already exists.")
            return

        password = input("Create Password: ")

        self.accounts[username] = Account(username, password)

        print("Account created successfully!")
        print("Starting Balance: ₹0")

    def login(self):
        username = input("Enter Username: ")
        password = input("Enter Password: ")

        if username not in self.accounts:
            print("Account not found.")
            return None

        account = self.accounts[username]

        if account.verify_password(password):
            print(f"Welcome, {username}!")
            return account

        print("Incorrect Password.")
        return None

atm = ATM()
while True:
    print("\n===== ATM SYSTEM =====")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter Choice: ")
    if choice == "1":
        atm.create_account()

    elif choice == "2":
        account = atm.login()

        if account:
            while True:
                print("\n===== ACCOUNT MENU =====")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Logout")
                option = input("Enter Choice: ")

                if option == "1":
                    amount = float(input("Enter Amount: "))
                    account.deposit(amount)

                elif option == "2":
                    amount = float(input("Enter Amount: "))
                    account.withdraw(amount)

                elif option == "3":
                    account.check_balance()

                elif option == "4":
                    print("Logged Out Successfully.")
                    break

                else:
                    print("Invalid Choice.")

    elif choice == "3":
        print("Thank You For Using ATM.")
        break

    else:
        print("Invalid Choice.")