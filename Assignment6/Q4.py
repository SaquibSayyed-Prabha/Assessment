# Q4. Create a Hospital System using Person, Doctor, Nurse and HeadNurse classes.
print("Q4. Create a Hospital System using Person, Doctor, Nurse and HeadNurse classes.")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name :", self.name)
        print("Age  :", self.age)

class Doctor(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def display_doctor(self):
        self.display_person()

class Nurse(Person):
    def __init__(self, name, age, ward):
        super().__init__(name, age)
        self.ward = ward

    def display_nurse(self):
        self.display_person()
        print("Ward :", self.ward)

class HeadNurse(Nurse):
    def __init__(self, name, age, ward, experience):
        super().__init__(name, age, ward)
        self.experience = experience

    def display_head_nurse(self):
        print("\n--- Head Nurse Details ---")
        self.display_nurse()
        print("Experience :", self.experience, "years")

N = HeadNurse("Shree", 40, "Neurology", 5)
N.display_head_nurse()