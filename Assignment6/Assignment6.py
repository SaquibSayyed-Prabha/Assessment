# Assignment 6 - Hybrid Inheritance, Hierarchical Inheritance, Polymorphism
print("Assignment 6 – Hybrid Inheritance, Hierarchical Inheritance, Polymorphism")
print()

# Q1. Create a School Management System using Person, Student, Teacher and TeachingAssistant classes. Display complete details of a Teaching Assistant.
print("Q1. Create a School Management System using Person, Student, Teacher and TeachingAssistant classes. Display complete details of a Teaching Assistant.")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_p(self):
        print("Name :", self.name)
        print("Age  :", self.age)

class Student(Person):
    def __init__(self, name, age, roll_no, course):
        Person.__init__(self, name, age)
        self.roll_no = roll_no
        self.course = course

    def display_s(self):
        self.display_p()
        print("Roll No :", self.roll_no)
        print("Course  :", self.course)

class Teacher(Person):
    def __init__(self, name, age, subject):
        Person.__init__(self, name, age)
        self.subject = subject

    def display_t(self):
        self.display_p()
        print("Subject     :", self.subject)

class TeachingAssistant(Student, Teacher):
    def __init__(self, name, age, roll_no, course, subject):
        Student.__init__(self, name, age, roll_no, course)
        Teacher.__init__(self, name, age, subject)

    def display_details(self):
        print("\n--- Teaching Assistant Details ---")
        print("Name        :", self.name)
        print("Age         :", self.age)
        print("Roll No     :", self.roll_no)
        print("Course      :", self.course)
        print("Subject     :", self.subject)

t1 = TeachingAssistant("Saquib", 17, 54, "AIML", "Python")
t1.display_details()
print()

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
print()

# Q3. Create an Employee System using Employee, Developer, Manager and TechLead classes. Show coding and team-management functionalities.
print("Q3. Create an Employee System using Employee, Developer, Manager and TechLead classes. Show coding and team-management functionalities.")
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display(self):
        print("Name :", self.name)
        print("Employee ID :", self.emp_id)

class Developer(Employee):
    def code(self):
        print(self.name, "is writing Python code.")

class Manager(Employee):
    def manage_team(self):
        print(self.name, "is managing the development team.")

class TechLead(Developer):
    def manage_team(self):
        print(self.name, "is leading and managing the team.")

    def show_details(self):
        print("\n--- Tech Lead Details ---")
        self.display()
        self.code()
        self.manage_team()

tl = TechLead("Saquib", "54")
tl.show_details()
print()

# Q4. Create a Hospital System using Person, Doctor, Nurse and HeadNurse classes.
print("Q4. Create a Hospital System using Person, Doctor, Nurse and HeadNurse classes.")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name :", self.name)
        print("Age  :", self.age)

class Doctor(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def display_doctor(self):
        self.display_person()

class Nurse(Person):
    def __init__(self, name, age, ward):
        super().__init__(name, age)
        self.ward = ward

    def display_nurse(self):
        self.display_person()
        print("Ward :", self.ward)

class HeadNurse(Nurse):
    def __init__(self, name, age, ward, experience):
        super().__init__(name, age, ward)
        self.experience = experience

    def display_head_nurse(self):
        print("\n--- Head Nurse Details ---")
        self.display_nurse()
        print("Experience :", self.experience, "years")

N = HeadNurse("Shree", 40, "Neurology", 5)
N.display_head_nurse()
print()

# Q5. Create an Animal class and derive Dog, Cat and Cow classes. Implement sound() method in each class.
print("Q5. Create an Animal class and derive Dog, Cat and Cow classes. Implement sound() method in each class.")
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog Barks")

class Cat(Animal):
    def sound(self):
        print("Cat Meows")

class Cow(Animal):
    def sound(self):
        print("Cow Mooos")

dog = Dog()
cat = Cat()
cow = Cow()

dog.sound()
cat.sound()
cow.sound()
print()

# Q6. Create a BankAccount class and derive SavingsAccount, CurrentAccount and FixedDepositAccount classes.
print("Q6. Create a BankAccount class and derive SavingsAccount, CurrentAccount and FixedDepositAccount classes.")
class BankAccount:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def display(self):
        print("Account No :", self.acc_no)
        print("Holder Name:", self.name)
        print("Balance    :", self.balance)

class SavingsAccount(BankAccount):
    def __init__(self, acc_no, name, balance, interest_rate):
        super().__init__(acc_no, name, balance)
        self.interest_rate = interest_rate

    def display_savings(self):
        self.display()
        print("Interest Rate:", self.interest_rate, "%")

class CurrentAccount(BankAccount):
    def __init__(self, acc_no, name, balance, overdraft_limit):
        super().__init__(acc_no, name, balance)
        self.overdraft_limit = overdraft_limit

    def display_current(self):
        self.display()
        print("Overdraft Limit:", self.overdraft_limit)

class FixedDepositAccount(BankAccount):
    def __init__(self, acc_no, name, balance, tenure):
        super().__init__(acc_no, name, balance)
        self.tenure = tenure

    def display_fd(self):
        self.display()
        print("Tenure:", self.tenure, "years")

sa = SavingsAccount("112233", "Saquib", 50000, 4.5)
sa.display_savings()
print()

# Q7.Create an Employee class and derive Developer, Tester and Designer classes. Override work() method.
print("Q7.Create an Employee class and derive Developer, Tester and Designer classes. Override work() method.")
class Employee:
    def work(self):
        print("Employee is working.")

class Developer(Employee):
    def work(self):
        print("Developer writes code.")

class Tester(Employee):
    def work(self):
        print("Tester tests software.")

class Designer(Employee):
    def work(self):
        print("Designer creates UI designs.")

d = Developer()
t = Tester()
ds = Designer()

d.work()
t.work()
ds.work()
print()

# Q8. Create a Shape class and derive Circle, Rectangle and Square classes. Display area calculations.
print("Q8. Create a Shape class and derive Circle, Rectangle and Square classes. Display area calculations.")
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        print("Area of Circle =", 3.14 * self.r * self.r)

class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        print("Area of Rectangle =", self.l * self.b)

class Square(Shape):
    def __init__(self, s):
        self.s = s

    def area(self):
        print("Area of Square =", self.s * self.s)

c = Circle(5)
r = Rectangle(4, 6)
s = Square(4)

c.area()
r.area()
s.area()
print()

# Q9. Create Shape, Circle, Rectangle and Triangle classes. Override area() method and call it using a loop.
print("Q9. Create Shape, Circle, Rectangle and Triangle classes. Override area() method and call it using a loop.")
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        print("Circle Area = 78.5")

class Rectangle(Shape):
    def area(self):
        print("Rectangle Area = 24")

class Triangle(Shape):
    def area(self):
        print("Triangle Area = 20")

shapes = [Circle(), Rectangle(), Triangle()]

for shape in shapes:
    shape.area()
print()

# Q10. Create Payment, CreditCardPayment, UPIPayment and NetBankingPayment classes. Override pay() method.
print("Q10. Create Payment, CreditCardPayment, UPIPayment and NetBankingPayment classes. Override pay() method.")
class Payment:
    def pay(self):
        print("Processing payment...")

class CreditCardPayment(Payment):
    def pay(self):
        print("Paid using Credit Card.")

class UPIPayment(Payment):
    def pay(self):
        print("Paid using UPI.")

class NetBankingPayment(Payment):
    def pay(self):
        print("Paid using Net Banking.")

p = UPIPayment()
p.pay()
print()

# Q11. Create Notification, EmailNotification, SMSNotification and PushNotification classes. Override send() method.
print("Q11. Create Notification, EmailNotification, SMSNotification and PushNotification classes. Override send() method.")
class Notification:
    def send(self):
        print("Sending notification.")

class EmailNotification(Notification):
    def send(self):
        print("Email sent.")

class SMSNotification(Notification):
    def send(self):
        print("SMS sent.")

class PushNotification(Notification):
    def send(self):
        print("Push notification sent.")

notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification()
]

for n in notifications:
    n.send()
print()

# Q12. Create Animal, Dog, Cat and Lion classes. Override make_sound() method.
print("Q12. Create Animal, Dog, Cat and Lion classes. Override make_sound() method.")
class Animal:
    def make_sound(self):
        print("Animal makes a sound.")

class Dog(Animal):
    def make_sound(self):
        print("Dog barks.")

class Cat(Animal):
    def make_sound(self):
        print("Cat meows.")

class Lion(Animal):
    def make_sound(self):
        print("Lion roars.")

animals = [Dog(), Cat(), Lion()]

for a in animals:
    a.make_sound()
print()

# Q13. Create Employee, Developer, Tester and Manager classes. Override role() method.
print("Q13. Create Employee, Developer, Tester and Manager classes. Override role() method.")
class Employee:
    def role(self):
        print("Employee")

class Developer(Employee):
    def role(self):
        print("Developer")

class Tester(Employee):
    def role(self):
        print("Tester")

class Manager(Employee):
    def role(self):
        print("Manager")

employees = [Developer(), Tester(), Manager()]

for e in employees:
    e.role()
print()

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
print()

# Q15. Create Device, Camera, Phone and SmartPhone classes. Demonstrate runtime polymorphism.
print("Q15. Create Device, Camera, Phone and SmartPhone classes. Demonstrate runtime polymorphism.")
class Device:
    def operate(self):
        print("Device operating.")

class Camera(Device):
    def operate(self):
        print("Camera taking photos.")

class Phone(Device):
    def operate(self):
        print("Phone making calls.")

class SmartPhone(Device):
    def operate(self):
        print("SmartPhone calling and taking photos.")

devices = [Camera(), Phone(), SmartPhone()]

for d in devices:
    d.operate()
print()
