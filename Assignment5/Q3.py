# Q3: Create a Car class with instance variables brand and model. Write an instance method to display car details.
print("Q3: Create a Car class with instance variables brand and model. Write an instance method to display car details.")
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Car Brand: ", self.brand)
        print("Model: ", self.model)

c1 = Car("Mercedes", "Benz C")
c2 = Car("BMW", "X5")

c1.display()
c2.display()