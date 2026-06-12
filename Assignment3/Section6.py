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