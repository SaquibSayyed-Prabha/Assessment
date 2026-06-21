# Q14. Create Vehicle, Car, Bike and Bus classes. Override start() method.
print("Q14. Create Vehicle, Car, Bike and Bus classes. Override start() method.")
class Vehicle:
    def start(self):
        print("Vehicle started.")

class Car(Vehicle):
    def start(self):
        print("Car started.")

class Bike(Vehicle):
    def start(self):
        print("Bike started.")

class Bus(Vehicle):
    def start(self):
        print("Bus started.")

vehicles = [Car(), Bike(), Bus()]

for v in vehicles:
    v.start()