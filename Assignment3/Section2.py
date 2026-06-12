# Section 2: Classes & Objects
print("Section: Classes & Objects")
print()

# Q6: Create a class Student with attributes name and age. Create an object and display the values.
print("Q6: Create a class Student with attributes name and age. Create an object and display the values.")
class Student:
    name = "Saquib"
    age = 18

student1 = Student()

print("Name:", student1.name)
print("Age:", student1.age)
print()

# Q7: Create a class Car with attributes brand and model. Create two objects and display details.
print("Q7: Create a class Car with attributes brand and model. Create two objects and display details.")
class Car:
    brand = "Toyota"
    model = "Fortuner"

car1 = Car()
car2 = Car()

print("Car 1:")
print("Brand:", car1.brand)
print("Model:", car1.model)

print("Car 2:")
print("Brand:", car2.brand)
print("Model:", car2.model)
print()

# Q8: Create a class Book with attributes title, author, and price. Create three objects and display details.
print("Q8: Create a class Book with attributes title, author, and price. Create three objects and display details.")
class Book:
    title = "Python Programming"
    author = "John Smith"
    price = 499

book1 = Book()
book2 = Book()
book3 = Book()

print("Book 1:")
print("Title:", book1.title)
print("Author:", book1.author)
print("Price:", book1.price)
print()

print("Book 2:")
print("Title:", book2.title)
print("Author:", book2.author)
print("Price:", book2.price)
print()

print("Book 3:")
print("Title:", book3.title)
print("Author:", book3.author)
print("Price:", book3.price)
print()

# Q9: Create a class Laptop with attributes brand, RAM, and price. Create two objects and print information.
print("Q9: Create a class Laptop with attributes brand, RAM, and price. Create two objects and print information.")
class Laptop:
    brand = "Samsung"
    ram = "16 GB"
    price = 55000

laptop1 = Laptop()
laptop2 = Laptop()

print("Laptop 1:")
print("Brand:", laptop1.brand)
print("RAM:", laptop1.ram)
print("Price:", laptop1.price)
print()

print("Laptop 2:")
print("Brand:", laptop2.brand)
print("RAM:", laptop2.ram)
print("Price:", laptop2.price)
print()

# Q10: Create a class Mobile with attributes company, model, and storage. Create multiple objects and display details.
print("Q10: Create a class Mobile with attributes company, model, and storage. Create multiple objects and display details.")
class Mobile:
    company = "Redmi"
    model = "12 5G"
    storage = "128 GB"

mobile1 = Mobile()
mobile2 = Mobile()
mobile3 = Mobile()

print("Mobile 1:")
print("Company:", mobile1.company)
print("Model:", mobile1.model)
print("Storage:", mobile1.storage)

print("Mobile 2:")
print("Company:", mobile2.company)
print("Model:", mobile2.model)
print("Storage:", mobile2.storage)

print("Mobile 3:")
print("Company:", mobile3.company)
print("Model:", mobile3.model)
print("Storage:", mobile3.storage)