# Q24: Create an Online Shopping System using OOP concepts including inheritance.
print("Q24: Create an Online Shopping System using OOP concepts including inheritance.")
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f"Product: {self.name}")
        print(f"Price: ${self.price}")

class Electronics(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty

    def display(self):
        super().display()
        print(f"Warranty: {self.warranty} Years")

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)
        print(f"{product.name} added to cart.")

    def show_bill(self):
        total = 0

        print("\n===== CART ITEMS =====")
        for item in self.items:
            item.display()
            print("----------------")
            total += item.price

        print(f"Total Bill = ${total}")

# Objects
laptop = Electronics("Laptop", 2500, 2)
headphone = Electronics("Headphone", 10, 1)

# Cart
cart = ShoppingCart()
cart.add_product(laptop)
cart.add_product(headphone)

cart.show_bill()