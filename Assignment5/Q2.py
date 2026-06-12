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