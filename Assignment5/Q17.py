# Q17: Create an Animal class and inherit Dog and Cat classes. Display different sounds using methods.
print("Q17: Create an Animal class and inherit Dog and Cat classes. Display different sounds using methods.")
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog says: Bark")

class Cat(Animal):
    def sound(self):
        print("Cat says: Meow")

d = Dog()
c = Cat()

d.sound()
c.sound()