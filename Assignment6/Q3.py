# Q3. Create an Employee System using Employee, Developer, Manager and TechLead classes. Show coding and team-management functionalities.
print("Q3. Create an Employee System using Employee, Developer, Manager and TechLead classes. Show coding and team-management functionalities.")
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display(self):
        print("Name :", self.name)
        print("Employee ID :", self.emp_id)

class Developer(Employee):
    def code(self):
        print(self.name, "is writing Python code.")

class Manager(Employee):
    def manage_team(self):
        print(self.name, "is managing the development team.")

class TechLead(Developer):
    def manage_team(self):
        print(self.name, "is leading and managing the team.")

    def show_details(self):
        print("\n--- Tech Lead Details ---")
        self.display()
        self.code()
        self.manage_team()

tl = TechLead("Saquib", "54")
tl.show_details()