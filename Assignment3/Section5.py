# Section 5: Instance Attributes
print("Section 5: Instance Attributes")
print()

# Q21: Create a class Student with instance attributes name, roll_no, and marks. Create three students and display details.
print("Q21: Create a class Student with instance attributes name, roll_no, and marks. Create three students and display details.")
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

student1 = Student("Saquib", 101, 85)
student2 = Student("Atharva", 102, 84)
student3 = Student("Suraj", 103, 86)

print("Student 1:", student1.name, student1.roll_no, student1.marks)
print("Student 2:", student2.name, student2.roll_no, student2.marks)
print("Student 3:", student3.name, student3.roll_no, student3.marks)
print()

# Q22: Create a class Employee with instance attributes emp_id, emp_name, and department. Display all employee details.
print("Q22: Create a class Employee with instance attributes emp_id, emp_name, and department. Display all employee details.")
class Employee:
    def __init__(self, emp_id, emp_name, department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.department = department

emp1 = Employee(1, "Saquib", "IT")
emp2 = Employee(2, "Atharva", "HR")

print("Employee 1:", emp1.emp_id, emp1.emp_name, emp1.department)
print("Employee 2:", emp2.emp_id, emp2.emp_name, emp2.department)
print()

# Q23: Create a class Hospital with instance attributes doctor_name and specialization. Create multiple objects and display details.
print("Q23: Create a class Hospital with instance attributes doctor_name and specialization. Create multiple objects and display details.")
class Hospital:
    def __init__(self, doctor_name, specialization):
        self.doctor_name = doctor_name
        self.specialization = specialization

doctor1 = Hospital("Dr. A", "Dentist")
doctor2 = Hospital("Dr. B", "Vet")

print("Doctor 1:", doctor1.doctor_name, doctor1.specialization)
print("Doctor 2:", doctor2.doctor_name, doctor2.specialization)
print()

# Q24: Create a class Course with instance attributes course_name, duration, and fees. Display course details.
print("Q24: Create a class Course with instance attributes course_name, duration, and fees. Display course details.")
class Course:
    def __init__(self, course_name, duration, fees):
        self.course_name = course_name
        self.duration = duration
        self.fees = fees

course1 = Course("Python", "3 Months", 5000)

print("Course Name:", course1.course_name)
print("Duration:", course1.duration)
print("Fees:", course1.fees)
print()

# Q25: Create a class CricketPlayer with instance attributes player_name, runs, and matches. Display player details.
print("Q25: Create a class CricketPlayer with instance attributes player_name, runs, and matches. Display player details.")
class CricketPlayer:
    def __init__(self, player_name, runs, matches):
        self.player_name = player_name
        self.runs = runs
        self.matches = matches

player1 = CricketPlayer("Virat Kohli", 14000, 300)

print("Player Name:", player1.player_name)
print("Runs:", player1.runs)
print("Matches:", player1.matches)