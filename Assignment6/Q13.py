# Q13. Create Employee, Developer, Tester and Manager classes. Override role() method.
print("Q13. Create Employee, Developer, Tester and Manager classes. Override role() method.")
class Employee:
    def role(self):
        print("Employee")

class Developer(Employee):
    def role(self):
        print("Developer")

class Tester(Employee):
    def role(self):
        print("Tester")

class Manager(Employee):
    def role(self):
        print("Manager")

employees = [Developer(), Tester(), Manager()]

for e in employees:
    e.role()