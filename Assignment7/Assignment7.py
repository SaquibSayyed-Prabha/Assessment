# Assignment 7 -  Abstract Class, Abstract Method, Polymorphism
print("Assignment 7 –  Abstract Class, Abstract Method, Polymorphism")
print()

# Q1. Abstract Class & Abstract Method
# Create an abstract class Vehicle.
# - Create an abstract method start().
# - Create a child class Car.
# - Implement the start() method in Car.
# - Create an object of Car and call start().
print("Q1. Abstract Class & Abstract Method")
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car is starting...")

obj = Car()
obj.start()
print()


# Q2. Abstract Class with Multiple Child Classes
# Create an abstract class Animal.
# - Create an abstract method sound().
# - Create two child classes: Dog and Cat.
# - Implement the sound() method in both classes.
# - Create objects and call sound().
print("Q2. Abstract Class with Multiple Child Classes")
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Cat(Animal):
    def sound(self):
        print("Meow")

class Dog(Animal):
    def sound(self):
        print("Barks")

obj = Cat()
obj2 = Dog()

obj.sound()
obj2.sound()
print()


# Q3. Polymorphism Using Method Overriding
# Create a class Shape.
# - Create a method draw().
# - Create child classes: Circle and Rectangle.
# - Override the draw() method in both child classes.
# - Call the draw() method using objects.
print("Q3. Polymorphism Using Method Overriding")
class Shape:
    def draw(self):
        print("Drawing a shape")

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle")

obj = [Circle(), Rectangle()]
for i in obj:
    i.draw()
print()


# Q4. Polymorphism with Loop
# Create a class Bird.
# - Create a method fly().
# - Create child classes: Sparrow and Eagle.
# - Override the fly() method.
# - Store objects in a list and call fly() using a loop.
print("Q4. Polymorphism with Loop")
class Bird:
    def fly(self):
        print("Flies")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow Flies low")

class Eagle(Bird):
    def fly(self):
        print("Eagle flies high")

obj = [Eagle(), Sparrow()]

for i in obj:
    i.fly()
print()


# Q5. Abstract Class + Polymorphism
# Create an abstract class Employee.
# - Create an abstract method work().
# - Create two child classes: Developer and Designer.
# - Implement the work() method in both classes.
# - Store objects in a list and call work() using a loop.
print("Q5. Abstract Class + Polymorphism")
from abc import ABC, abstractmethod

class Employee(ABC):
    def work(self):
        pass

class Developer(Employee):
    def work(self):
        print("Developer writes code")

class Designer(Employee):
    def work(self):
        print("Designer creates UI designs")

obj = [Developer(), Designer()]

for i in obj:
    i.work()