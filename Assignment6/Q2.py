# Q2. Create a Vehicle Management System using Vehicle, Car, Bike, ElectricCar and SportsElectricCar classes.
print("Q2. Create a Vehicle Management System using Vehicle, Car, Bike, ElectricCar and SportsElectricCar classes.")
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display_vehicle(self):
        print("Brand:", self.brand)

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def display_car(self):
        self.display_vehicle()
        print("Model:", self.model)

class Bike(Vehicle):
    def __init__(self, brand, bike_type):
        super().__init__(brand)
        self.bike_type = bike_type

    def display_bike(self):
        self.display_vehicle()
        print("Type:", self.bike_type)

class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def display_electric_car(self):
        self.display_car()
        print("Battery Capacity:", self.battery_capacity, "kWh")

class SportsElectricCar(ElectricCar):
    def __init__(self, brand, model, battery_capacity, top_speed):
        super().__init__(brand, model, battery_capacity)
        self.top_speed = top_speed

    def display_details(self):
        print("\n--- Sports Electric Car Details ---")
        self.display_electric_car()
        print("Top Speed:", self.top_speed, "km/h")

car = SportsElectricCar("Tesla", "Roadster", 200, 400)
car.display_details()