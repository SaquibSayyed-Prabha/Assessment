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