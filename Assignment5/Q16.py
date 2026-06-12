# Q16: Create a Shape class and inherit Circle and Rectangle classes from it.
print("Q16: Create a Shape class and inherit Circle and Rectangle classes from it.")
class Shape:
    def area(self):
        print("Area calculation not defined")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

c = Circle(5)
r = Rectangle(4, 6)

print("Circle Area:", c.area())
print("Rectangle Area:", r.area())