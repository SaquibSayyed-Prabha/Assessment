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