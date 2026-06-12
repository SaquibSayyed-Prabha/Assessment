# Q8: Create a Product class with a class variable tax_rate and calculate the final product price.
print("Q8: Create a Product class with a class variable tax_rate and calculate the final product price.")
class Product:
    tax_rate = 0.15

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def final_price(self):
        return self.price + (self.price * Product.tax_rate)
    
    def display(self):
        print("Product Name: ", self.name)
        print("Price with tax: ", Product.final_price())
        print()

p1 = Product("Laptop", 50000)
p2 = Product("Mouse", 1000)

p1.display()
p2.display()