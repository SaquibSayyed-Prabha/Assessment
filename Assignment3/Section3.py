# Section 3: Constructor (__init__)
print("Section 3: Constructor")
print()

# Q11: Create a class Employee. Use constructor to initialize emp_id, emp_name, and salary. Display employee information.
print("Q11: Create a class Employee. Use constructor to initialize emp_id, emp_name, and salary. Display employee information.")
class Employee:
    def __init__(self, emp_id, emp_name, salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.salary = salary
    
    def display(self):
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.emp_name)
        print("Salary:", self.salary)

emp1 = Employee(101, "Saquib", 50000)
emp1.display()
print()

# Q12: Create a class BankAccount. Initialize account_number, holder_name, and balance. Create two accounts and display details.
print("Q12: Create a class BankAccount. Initialize account_number, holder_name, and balance. Create two accounts and display details.")
class BankAccount:
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
    
    def display(self):
        print("Account Number:", self.account_number)
        print("Holder Name:", self.holder_name)
        print("Balance:", self.balance)
        print()

acc1 = BankAccount(1001, "Saquib", 10000)
acc2 = BankAccount(1002, "Atharva", 15000)
print("Account 1")
acc1.display()
print("Account 2")
acc2.display()
print()

# Q13: Create a class Movie. Initialize movie_name, hero, and rating. Display movie details.
print("Q13: Create a class Movie. Initialize movie_name, hero, and rating. Display movie details.")
class Movie:
    def __init__(self, movie_name, hero, rating):
        self.movie_name = movie_name
        self.hero = hero
        self.rating = rating

movie1 = Movie("Kung Fu Panda", "Po", 9.5)

print("Movie Name:", movie1.movie_name)
print("Hero:", movie1.hero)
print("Rating:", movie1.rating)
print()

# Q14: Create a class Product. Initialize product_id, product_name, and price. Create multiple products and print details.
print("Q14: Create a class Product. Initialize product_id, product_name, and price. Create multiple products and print details.")
class Product:
    def __init__(self, product_id, product_name, price):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price

    def display(self):
        print(f"ID: {self.product_id}\nProduct: {self.product_name}\nPrice: {self.price}\n")

product1 = Product(1, "Laptop", 50000)
product2 = Product(2, "Mobile", 25000)
product3 = Product(3, "Keyboard", 1200)

print("Product 1:")
product1.display()
print("Product 2:")
product2.display()
print("Product 3:")
product3.display()
print()

# Q15: Create a class College. Initialize college_name, city, and students_count. Display details using objects.
print("Q15: Create a class College. Initialize college_name, city, and students_count. Display details using objects.")
class College:
    def __init__(self, college_name, city, students_count):
        self.college_name = college_name
        self.city = city
        self.students_count = students_count

    def display(self):
        print("College Name:", college1.college_name)
        print("City:", college1.city)
        print("Students Count:", college1.students_count)

college1 = College("Government Polytechnic", "Pune", 1200)

print("College Name:", college1.college_name)
print("City:", college1.city)
print("Students Count:", college1.students_count)