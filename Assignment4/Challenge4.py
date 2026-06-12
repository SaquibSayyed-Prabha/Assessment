# Challenge 4: Mobile Store Inventory

# Create a Mobile class.
# Requirements:
# - Create instance variables: brand, model, price.
# - Create a class variable discount_percentage = 10.
# - Create an instance method display_mobile().
# - Create an instance method calculate_discount_price().
# - Create a class method change_discount(new_discount) to update the discount percentage for all mobiles.

print("Challenge 4: Mobile Store Inventory")
print()

class Mobile:
    discount_percentage = 10

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_mobile(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)

    def calculate_discount_price(self):
        discount = (self.price * Mobile.discount_percentage) / 100
        final_price = self.price - discount
        print("Discounted Price:", final_price)

    @classmethod
    def change_discount(cls, new_discount):
        cls.discount_percentage = new_discount

# Objects
m1 = Mobile("Samsung", "M14", 15000)
m2 = Mobile("Realme", "Narzo", 12000)

m1.display_mobile()
m1.calculate_discount_price()

Mobile.change_discount(20)
print("\nAfter Discount Change:")
m2.calculate_discount_price()