class Student:



    college_name = "ABC College"



    def __init__(self, name):

        self.name = name



    @classmethod

    def change_college(cls, new_college):

        cls.college_name = new_college



    def display(self):

        print("Name:", self.name)

        print("College:", Student.college_name)



s1 = Student("Sham") 

s2 = Student("Amit")



Student.change_college("XYZ College")



s1.display()

s2.display()