# Q7.Create an Employee class and derive Developer, Tester and Designer classes. Override work() method.
print("Q7.Create an Employee class and derive Developer, Tester and Designer classes. Override work() method.")
class Employee:
    def work(self):
        print("Employee is working.")

class Developer(Employee):
    def work(self):
        print("Developer writes code.")

class Tester(Employee):
    def work(self):
        print("Tester tests software.")

class Designer(Employee):
    def work(self):
        print("Designer creates UI designs.")

d = Developer()
t = Tester()
ds = Designer()

d.work()
t.work()
ds.work()