# Q23: Create a School Management System using class variables, class methods, and instance methods.
print("Q23: Create a School Management System using class variables, class methods, and instance methods.")
class School:
    total_students = 0

    def __init__(self, name):
        self.name = name
        School.total_students += 1

    def display(self):
        print("Student:", self.name)

    @classmethod
    def student_count(cls):
        print("Total Students:", cls.total_students)

s1 = School("Suraj")
s2 = School("Rohit")
s3 = School("Atharva")

s1.display()
s2.display()
s3.display()

School.student_count()