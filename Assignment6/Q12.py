# Q12. Create Animal, Dog, Cat and Lion classes. Override make_sound() method.
print("Q12. Create Animal, Dog, Cat and Lion classes. Override make_sound() method.")
class Animal:
    def make_sound(self):
        print("Animal makes a sound.")

class Dog(Animal):
    def make_sound(self):
        print("Dog barks.")

class Cat(Animal):
    def make_sound(self):
        print("Cat meows.")

class Lion(Animal):
    def make_sound(self):
        print("Lion roars.")

animals = [Dog(), Cat(), Lion()]

for a in animals:
    a.make_sound()