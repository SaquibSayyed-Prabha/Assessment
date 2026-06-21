# Q8. Create a Shape class and derive Circle, Rectangle and Square classes. Display area calculations.
print("Q8. Create a Shape class and derive Circle, Rectangle and Square classes. Display area calculations.")
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        print("Area of Circle =", 3.14 * self.r * self.r)

class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        print("Area of Rectangle =", self.l * self.b)

class Square(Shape):
    def __init__(self, s):
        self.s = s

    def area(self):
        print("Area of Square =", self.s * self.s)

c = Circle(5)
r = Rectangle(4, 6)
s = Square(4)

c.area()
r.area()
s.area()