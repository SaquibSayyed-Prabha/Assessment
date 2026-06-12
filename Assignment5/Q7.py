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