# Assignment 3 - Python Modules & OOP Practice Coding
print("Assignment 3 - Python Modules & OOP Practice Coding")

# Section 1: Modules
print("Section 1: Modules")
print()

# Q1: Create a module named calculator.py containing functions add(), subtract(), multiply(), divide(). Import the module in another file and perform all operations.
print("Q1: Create a module named calculator.py containing functions add(), subtract(), multiply(), divide(). Import the module in another file and perform all operations.")
import mod_calculator

print("Addition:", mod_calculator.add(10, 5))
print("Subtraction:", mod_calculator.subtract(10, 5))
print("Multiplication:", mod_calculator.multiply(10, 5))
print("Division:", mod_calculator.divide(10, 5))
print()

# Q2: Create a module named employee.py. Store employee name and salary. Create a function to display employee details. Import and use the function in another file.
print("Q2: Create a module named employee.py. Store employee name and salary. Create a function to display employee details. Import and use the function in another file.")
import mod_employee

mod_employee.display_emp()
print()

# Q3: Import the math module and write a program to find square root of 144, value of pi and factorial of 6.
print("Q3: Import the math module and write a program to find square root of 144, value of pi and factorial of 6.")
import math

print("Square Root of 144:", math.sqrt(144))
print("Value of Pi:", math.pi)
print("Factorial of 6:", math.factorial(6))
print()

# Q4: Import the random module and generate a random number between 1 and 100 and a random choice from ['Python', 'Java', 'React', 'Django'].
print("Q4: Import the random module and generate a random number between 1 and 100 and a random choice from ['Python', 'Java', 'React', 'Django'].")
import random

print("Random Number:", random.randint(1, 100))
print("Random Choice:",
      random.choice(["Python", "Java", "React", "Django"]))
print()

# Q5: Create a custom module area.py with functions area_circle() and area_rectangle(). Import the module and calculate areas.
print("# Q5: Create a custom module area.py with functions area_circle() and area_rectangle(). Import the module and calculate areas.")
import mod_area

radius = 7
length = 10
breadth = 5
print(f"Radius = {radius}\nLength = {length}\nBreadth = {breadth}")
print("Area of Circle:",
      mod_area.area_circle(radius))

print("Area of Rectangle:",
      mod_area.area_rectangle(length, breadth))
print("\n\n")


# Section 2: Classes & Objects
print("Section: Classes & Objects")
print()

# Q6: Create a class Student with attributes name and age. Create an object and display the values.
print("Q6: Create a class Student with attributes name and age. Create an object and display the values.")
class Student:
    name = "Saquib"
    age = 18

student1 = Student()

print("Name:", student1.name)
print("Age:", student1.age)
print()

# Q7: Create a class Car with attributes brand and model. Create two objects and display details.
print("Q7: Create a class Car with attributes brand and model. Create two objects and display details.")
class Car:
    brand = "Toyota"
    model = "Fortuner"

car1 = Car()
car2 = Car()

print("Car 1:")
print("Brand:", car1.brand)
print("Model:", car1.model)

print("Car 2:")
print("Brand:", car2.brand)
print("Model:", car2.model)
print()

# Q8: Create a class Book with attributes title, author, and price. Create three objects and display details.
print("Q8: Create a class Book with attributes title, author, and price. Create three objects and display details.")
class Book:
    title = "Python Programming"
    author = "John Smith"
    price = 499

book1 = Book()
book2 = Book()
book3 = Book()

print("Book 1:")
print("Title:", book1.title)
print("Author:", book1.author)
print("Price:", book1.price)
print()

print("Book 2:")
print("Title:", book2.title)
print("Author:", book2.author)
print("Price:", book2.price)
print()

print("Book 3:")
print("Title:", book3.title)
print("Author:", book3.author)
print("Price:", book3.price)
print()

# Q9: Create a class Laptop with attributes brand, RAM, and price. Create two objects and print information.
print("Q9: Create a class Laptop with attributes brand, RAM, and price. Create two objects and print information.")
class Laptop:
    brand = "Samsung"
    ram = "16 GB"
    price = 55000

laptop1 = Laptop()
laptop2 = Laptop()

print("Laptop 1:")
print("Brand:", laptop1.brand)
print("RAM:", laptop1.ram)
print("Price:", laptop1.price)
print()

print("Laptop 2:")
print("Brand:", laptop2.brand)
print("RAM:", laptop2.ram)
print("Price:", laptop2.price)
print()

# Q10: Create a class Mobile with attributes company, model, and storage. Create multiple objects and display details.
print("Q10: Create a class Mobile with attributes company, model, and storage. Create multiple objects and display details.")
class Mobile:
    company = "Redmi"
    model = "12 5G"
    storage = "128 GB"

mobile1 = Mobile()
mobile2 = Mobile()
mobile3 = Mobile()

print("Mobile 1:")
print("Company:", mobile1.company)
print("Model:", mobile1.model)
print("Storage:", mobile1.storage)

print("Mobile 2:")
print("Company:", mobile2.company)
print("Model:", mobile2.model)
print("Storage:", mobile2.storage)

print("Mobile 3:")
print("Company:", mobile3.company)
print("Model:", mobile3.model)
print("Storage:", mobile3.storage)
print("\n\n")


# Section 3: Constructor (__init__)
print("Section 3: Constructor")
print()

# Q11: Create a class Employee. Use constructor to initialize emp_id, emp_name, and salary. Display employee information.
print("Q11: Create a class Employee. Use constructor to initialize emp_id, emp_name, and salary. Display employee information.")
class Employee:
    def __init__(self, emp_id, emp_name, salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.salary = salary
    
    def display(self):
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.emp_name)
        print("Salary:", self.salary)

emp1 = Employee(101, "Saquib", 50000)
emp1.display()
print()

# Q12: Create a class BankAccount. Initialize account_number, holder_name, and balance. Create two accounts and display details.
print("Q12: Create a class BankAccount. Initialize account_number, holder_name, and balance. Create two accounts and display details.")
class BankAccount:
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
    
    def display(self):
        print("Account Number:", self.account_number)
        print("Holder Name:", self.holder_name)
        print("Balance:", self.balance)
        print()

acc1 = BankAccount(1001, "Saquib", 10000)
acc2 = BankAccount(1002, "Atharva", 15000)
print("Account 1")
acc1.display()
print("Account 2")
acc2.display()
print()

# Q13: Create a class Movie. Initialize movie_name, hero, and rating. Display movie details.
print("Q13: Create a class Movie. Initialize movie_name, hero, and rating. Display movie details.")
class Movie:
    def __init__(self, movie_name, hero, rating):
        self.movie_name = movie_name
        self.hero = hero
        self.rating = rating

movie1 = Movie("Kung Fu Panda", "Po", 9.5)

print("Movie Name:", movie1.movie_name)
print("Hero:", movie1.hero)
print("Rating:", movie1.rating)
print()

# Q14: Create a class Product. Initialize product_id, product_name, and price. Create multiple products and print details.
print("Q14: Create a class Product. Initialize product_id, product_name, and price. Create multiple products and print details.")
class Product:
    def __init__(self, product_id, product_name, price):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price

    def display(self):
        print(f"ID: {self.product_id}\nProduct: {self.product_name}\nPrice: {self.price}\n")

product1 = Product(1, "Laptop", 50000)
product2 = Product(2, "Mobile", 25000)
product3 = Product(3, "Keyboard", 1200)

print("Product 1:")
product1.display()
print("Product 2:")
product2.display()
print("Product 3:")
product3.display()
print()

# Q15: Create a class College. Initialize college_name, city, and students_count. Display details using objects.
print("Q15: Create a class College. Initialize college_name, city, and students_count. Display details using objects.")
class College:
    def __init__(self, college_name, city, students_count):
        self.college_name = college_name
        self.city = city
        self.students_count = students_count

    def display(self):
        print("College Name:", college1.college_name)
        print("City:", college1.city)
        print("Students Count:", college1.students_count)

college1 = College("Government Polytechnic", "Pune", 1200)

print("College Name:", college1.college_name)
print("City:", college1.city)
print("Students Count:", college1.students_count)
print("\n\n")


# Section 4: self Keyword
print("Section 4: self Keyword")
print()

# Q16: Create a class Person. Use self to store name and age. Display values using a method.
print("Q16: Create a class Person. Use self to store name and age. Display values using a method.")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

person1 = Person("Saquib", 18)
person1.display()
print()

# Q17: Create a class Animal. Store animal_name and color. Print values using self.
print("Q17: Create a class Animal. Store animal_name and color. Print values using self.")
class Animal:
    def __init__(self, animal_name, color):
        self.animal_name = animal_name
        self.color = color

    def display(self):
        print("Animal Name:", self.animal_name)
        print("Color:", self.color)

animal1 = Animal("Tiger", "Orange")
animal1.display()
print()

# Q18: Create a class Vehicle. Store company and model. Display details using a method and self.
print("Q18: Create a class Vehicle. Store company and model. Display details using a method and self.")
class Vehicle:
    def __init__(self, company, model):
        self.company = company
        self.model = model

    def display(self):
        print("Company:", self.company)
        print("Model:", self.model)

vehicle1 = Vehicle("Toyota", "Fortuner")
vehicle1.display()
print()

# Q19: Create a class Teacher. Store teacher_name and subject. Display teacher information using self.
print("Q19: Create a class Teacher. Store teacher_name and subject. Display teacher information using self.")
class Teacher:
    def __init__(self, teacher_name, subject):
        self.teacher_name = teacher_name
        self.subject = subject

    def display(self):
        print("Teacher Name:", self.teacher_name)
        print("Subject:", self.subject)

teacher1 = Teacher("Mr. Sharma", "Python")
teacher1.display()
print()

# Q20: Create a class Player. Store player_name and team. Print details using self.
print("Q20: Create a class Player. Store player_name and team. Print details using self.")
class Player:
    def __init__(self, player_name, team):
        self.player_name = player_name
        self.team = team

    def display(self):
        print("Player Name:", self.player_name)
        print("Team:", self.team)

player1 = Player("Virat Kohli", "India")
player1.display()
print("\n\n")


# Section 5: Instance Attributes
print("Section 5: Instance Attributes")
print()

# Q21: Create a class Student with instance attributes name, roll_no, and marks. Create three students and display details.
print("Q21: Create a class Student with instance attributes name, roll_no, and marks. Create three students and display details.")
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

student1 = Student("Saquib", 101, 85)
student2 = Student("Atharva", 102, 84)
student3 = Student("Suraj", 103, 86)

print("Student 1:", student1.name, student1.roll_no, student1.marks)
print("Student 2:", student2.name, student2.roll_no, student2.marks)
print("Student 3:", student3.name, student3.roll_no, student3.marks)
print()

# Q22: Create a class Employee with instance attributes emp_id, emp_name, and department. Display all employee details.
print("Q22: Create a class Employee with instance attributes emp_id, emp_name, and department. Display all employee details.")
class Employee:
    def __init__(self, emp_id, emp_name, department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.department = department

emp1 = Employee(1, "Saquib", "IT")
emp2 = Employee(2, "Atharva", "HR")

print("Employee 1:", emp1.emp_id, emp1.emp_name, emp1.department)
print("Employee 2:", emp2.emp_id, emp2.emp_name, emp2.department)
print()

# Q23: Create a class Hospital with instance attributes doctor_name and specialization. Create multiple objects and display details.
print("Q23: Create a class Hospital with instance attributes doctor_name and specialization. Create multiple objects and display details.")
class Hospital:
    def __init__(self, doctor_name, specialization):
        self.doctor_name = doctor_name
        self.specialization = specialization

doctor1 = Hospital("Dr. A", "Dentist")
doctor2 = Hospital("Dr. B", "Vet")

print("Doctor 1:", doctor1.doctor_name, doctor1.specialization)
print("Doctor 2:", doctor2.doctor_name, doctor2.specialization)
print()

# Q24: Create a class Course with instance attributes course_name, duration, and fees. Display course details.
print("Q24: Create a class Course with instance attributes course_name, duration, and fees. Display course details.")
class Course:
    def __init__(self, course_name, duration, fees):
        self.course_name = course_name
        self.duration = duration
        self.fees = fees

course1 = Course("Python", "3 Months", 5000)

print("Course Name:", course1.course_name)
print("Duration:", course1.duration)
print("Fees:", course1.fees)
print()

# Q25: Create a class CricketPlayer with instance attributes player_name, runs, and matches. Display player details.
print("Q25: Create a class CricketPlayer with instance attributes player_name, runs, and matches. Display player details.")
class CricketPlayer:
    def __init__(self, player_name, runs, matches):
        self.player_name = player_name
        self.runs = runs
        self.matches = matches

player1 = CricketPlayer("Virat Kohli", 14000, 300)

print("Player Name:", player1.player_name)
print("Runs:", player1.runs)
print("Matches:", player1.matches)
print("\n\n")


# Section 6: Instance Methods
print("Section 6: Instance Methods")
print()

# Q26: Create a class Rectangle with an instance method calculate_area(). Take length and width from constructor.
print("Q26: Create a class Rectangle with an instance method calculate_area(). Take length and width from constructor.")
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

rectangle1 = Rectangle(10, 5)

print("Length:", rectangle1.length)
print("Width:", rectangle1.width)
print("Area:", rectangle1.calculate_area())
print()

# Q27: Create a class Circle with an instance method calculate_area(). Take radius from constructor.
print("Q27: Create a class Circle with an instance method calculate_area(). Take radius from constructor.")
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

circle1 = Circle(7)

print("Radius:", circle1.radius)
print("Area:", circle1.calculate_area())
print()

# Q28: Create a class Employee with an instance method annual_salary(). Calculate yearly salary.
print("Q28: Create a class Employee with an instance method annual_salary(). Calculate yearly salary.")
class Employee:
    def __init__(self, emp_name, monthly_salary):
        self.emp_name = emp_name
        self.monthly_salary = monthly_salary

    def annual_salary(self):
        return self.monthly_salary * 12

emp1 = Employee("Saquib", 50000)

print("Employee Name:", emp1.emp_name)
print("Monthly Salary:", emp1.monthly_salary)
print("Annual Salary:", emp1.annual_salary())
print()

# Q29: Create a class Student with an instance method calculate_percentage(). Calculate percentage from marks.
print("Q29: Create a class Student with an instance method calculate_percentage(). Calculate percentage from marks.")
class Student:
    def __init__(self, name, marks_obtained, total_marks):
        self.name = name
        self.marks_obtained = marks_obtained
        self.total_marks = total_marks

    def calculate_percentage(self):
        return (self.marks_obtained / self.total_marks) * 100

student1 = Student("Saquib", 425, 500)

print("Student Name:", student1.name)
print("Marks Obtained:", student1.marks_obtained)
print("Total Marks:", student1.total_marks)
print("Percentage:", student1.calculate_percentage(), "%")
print()

# Q30: Create a class BankAccount with methods deposit() and withdraw(). Update account balance.
print("Q30: Create a class BankAccount with methods deposit() and withdraw(). Update account balance.")
class BankAccount:
    def __init__(self, holder_name, balance):
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def display_balance(self):
        print("Current Balance:", self.balance)

account1 = BankAccount("Saquib", 10000)

account1.display_balance()
account1.deposit(5000)
account1.display_balance()
account1.withdraw(3000)
account1.display_balance()