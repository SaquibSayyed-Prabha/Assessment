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