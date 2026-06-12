# Q1: Create a Student class with instance variables name and age. Create 3 objects and display their details.
print("Q1: Create a Student class with instance variables name and age. Create 3 objects and display their details.")
class Student:
    def __init__(self, name, age):
        self.name = name                   
        self.age = age
    
    def display_student(self):              
        print("Name:", self.name)
        print("Age:", self.age)
        print()

s1 = Student("Saquib", 17)
s2 = Student("Atharva", 18)
s3 = Student("Suraj", 18)

s1.display_student()
s2.display_student()
s3.display_student()