# Q1. Create a School Management System using Person, Student, Teacher and TeachingAssistant classes. Display complete details of a Teaching Assistant.
print("Q1. Create a School Management System using Person, Student, Teacher and TeachingAssistant classes. Display complete details of a Teaching Assistant.")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_p(self):
        print("Name :", self.name)
        print("Age  :", self.age)

class Student(Person):
    def __init__(self, name, age, roll_no, course):
        Person.__init__(self, name, age)
        self.roll_no = roll_no
        self.course = course

    def display_s(self):
        self.display_p()
        print("Roll No :", self.roll_no)
        print("Course  :", self.course)

class Teacher(Person):
    def __init__(self, name, age, subject):
        Person.__init__(self, name, age)
        self.subject = subject

    def display_t(self):
        self.display_p()
        print("Subject     :", self.subject)

class TeachingAssistant(Student, Teacher):
    def __init__(self, name, age, roll_no, course, subject):
        Student.__init__(self, name, age, roll_no, course)
        Teacher.__init__(self, name, age, subject)

    def display_details(self):
        print("\n--- Teaching Assistant Details ---")
        print("Name        :", self.name)
        print("Age         :", self.age)
        print("Roll No     :", self.roll_no)
        print("Course      :", self.course)
        print("Subject     :", self.subject)

t1 = TeachingAssistant("Saquib", 17, 54, "AIML", "Python")
t1.display_details()