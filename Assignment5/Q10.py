# Q10: Create a Vehicle class with a class variable vehicle_count. Count the total number of vehicles created.
print("Q10: Create a Vehicle class with a class variable vehicle_count. Count the total number of vehicles created.")
class Vehicle:
    vehicle_count = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        vehicle_count +=1

    def show_vehicle(self):
        print("Vehicle Brand: ", self.brand)
        print("Model: ", self.model)
        print()
    
    @classmethod
    def display_count(cls):
        print("Total No. of vehicles: ", cls.vehicle_count)

v1 = Vehicle("Mercedes", "Benz")
v2 = Vehicle("BMW", "M3")
Vehicle.display_count()