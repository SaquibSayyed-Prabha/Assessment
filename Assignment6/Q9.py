# Q9. Create Shape, Circle, Rectangle and Triangle classes. Override area() method and call it using a loop.
print("Q9. Create Shape, Circle, Rectangle and Triangle classes. Override area() method and call it using a loop.")
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        print("Circle Area = 78.5")

class Rectangle(Shape):
    def area(self):
        print("Rectangle Area = 24")

class Triangle(Shape):
    def area(self):
        print("Triangle Area = 20")

shapes = [Circle(), Rectangle(), Triangle()]

for shape in shapes:
    shape.area()