# Q5. Create an Animal class and derive Dog, Cat and Cow classes. Implement sound() method in each class.
print("Q5. Create an Animal class and derive Dog, Cat and Cow classes. Implement sound() method in each class.")
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog Barks")

class Cat(Animal):
    def sound(self):
        print("Cat Meows")

class Cow(Animal):
    def sound(self):
        print("Cow Mooos")

dog = Dog()
cat = Cat()
cow = Cow()

dog.sound()
cat.sound()
cow.sound()