# Challenge 1: Student Management System

# Create a Student class.
# Requirements:
# - Create instance variables: name, age, course.
# - Create a class variable school_name = "ABC College".
# - Create an instance method display_student() to display student details.
# - Create a class method change_school_name() to change the school name.
# - Create 2 student objects and demonstrate the class method

print("Challenge 1: Student Management System")
print()

class Student:
    school_name = "ABC College"      # Class Variable

    def __init__(self, name, age, course):
        self.name = name                    # Instance variables
        self.age = age
        self.course = course

    def display_student(self):              # Instance method
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        print("School:", Student.school_name)
        print()

    @classmethod                            # Class Method
    def change_school_name(cls, new_name):
        cls.school_name = new_name

# Creating Objects
s1 = Student("Saquib", 17, "AIML")
s2 = Student("Nikhil", 18, "AR")

print("Before Change:")
s1.display_student()
s2.display_student()

Student.change_school_name("XYZ College")

print("\nAfter Change:")
s1.display_student()
s2.display_student()