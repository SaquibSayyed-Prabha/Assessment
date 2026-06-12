# Q15: Create a Vehicle class and a Bike class that inherits from Vehicle. Add extra properties in Bike.
print("Q15: Create a Vehicle class and a Bike class that inherits from Vehicle. Add extra properties in Bike.")
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Bike(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

b = Bike("Honda", "Shine")
print("Bike Brand: ", b.brand)
print("Model: ", b.model)