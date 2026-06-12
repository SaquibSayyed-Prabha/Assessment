# Q9: Create a Student class with a class method to update the school name for all students.
print("Q9: Create a Student class with a class method to update the school name for all students.")
class Student:
    school_name = "ABC School"
    def __init__(self, s_no, name):
        self.s_no = s_no
        self.name = name

    def display(self):
        print("Student Name: ", self.name)
        print("Roll no: ", self.s_no)
        print("School Name: ", Student.school_name)
        print()

    @classmethod
    def change_school_name(cls, new_name):
        cls.school_name = new_name

s1 = Student(1, "Saquib")
s1.display()
s1.change_school_name("XYZ School")
s1.display()