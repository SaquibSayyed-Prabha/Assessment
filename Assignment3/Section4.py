# Section 4: self Keyword
print("Section 4: self Keyword")
print()

# Q16: Create a class Person. Use self to store name and age. Display values using a method.
print("Q16: Create a class Person. Use self to store name and age. Display values using a method.")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

person1 = Person("Saquib", 18)
person1.display()
print()

# Q17: Create a class Animal. Store animal_name and color. Print values using self.
print("Q17: Create a class Animal. Store animal_name and color. Print values using self.")
class Animal:
    def __init__(self, animal_name, color):
        self.animal_name = animal_name
        self.color = color

    def display(self):
        print("Animal Name:", self.animal_name)
        print("Color:", self.color)

animal1 = Animal("Tiger", "Orange")
animal1.display()
print()

# Q18: Create a class Vehicle. Store company and model. Display details using a method and self.
print("Q18: Create a class Vehicle. Store company and model. Display details using a method and self.")
class Vehicle:
    def __init__(self, company, model):
        self.company = company
        self.model = model

    def display(self):
        print("Company:", self.company)
        print("Model:", self.model)

vehicle1 = Vehicle("Toyota", "Fortuner")
vehicle1.display()
print()

# Q19: Create a class Teacher. Store teacher_name and subject. Display teacher information using self.
print("Q19: Create a class Teacher. Store teacher_name and subject. Display teacher information using self.")
class Teacher:
    def __init__(self, teacher_name, subject):
        self.teacher_name = teacher_name
        self.subject = subject

    def display(self):
        print("Teacher Name:", self.teacher_name)
        print("Subject:", self.subject)

teacher1 = Teacher("Mr. Sharma", "Python")
teacher1.display()
print()

# Q20: Create a class Player. Store player_name and team. Print details using self.
print("Q20: Create a class Player. Store player_name and team. Print details using self.")
class Player:
    def __init__(self, player_name, team):
        self.player_name = player_name
        self.team = team

    def display(self):
        print("Player Name:", self.player_name)
        print("Team:", self.team)

player1 = Player("Virat Kohli", "India")
player1.display()