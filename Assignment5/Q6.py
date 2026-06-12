# Q6: Create a Mobile class with a constructor and display mobile details using an instance method.
print("Q6: Create a Mobile class with a constructor and display mobile details using an instance method.")
class Mobile:
    def __init__(self, brand, model, ram, storage, price):
        self.brand = brand
        self.model = model
        self.ram = ram
        self.storage = storage
        self.price = price

    def display_mob(self):
        print("Mobile Brand: ", self.brand)
        print("Model: ", self.model)
        print("RAM: ", self.ram)
        print("Storage", self.storage)
        print("Price", self.price)
        print()

m1 = Mobile("Samsung", "J7", 2, 16, 8000)
m1.display_mob()