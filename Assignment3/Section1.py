# Section 1: Modules
print("Section 1: Modules")
print()

# Q1: Create a module named calculator.py containing functions add(), subtract(), multiply(), divide(). Import the module in another file and perform all operations.
print("Q1: Create a module named calculator.py containing functions add(), subtract(), multiply(), divide(). Import the module in another file and perform all operations.")
import mod_calculator

print("Addition:", mod_calculator.add(10, 5))
print("Subtraction:", mod_calculator.subtract(10, 5))
print("Multiplication:", mod_calculator.multiply(10, 5))
print("Division:", mod_calculator.divide(10, 5))
print()

# Q2: Create a module named employee.py. Store employee name and salary. Create a function to display employee details. Import and use the function in another file.
print("Q2: Create a module named employee.py. Store employee name and salary. Create a function to display employee details. Import and use the function in another file.")
import mod_employee

mod_employee.display_emp()
print()

# Q3: Import the math module and write a program to find square root of 144, value of pi and factorial of 6.
print("Q3: Import the math module and write a program to find square root of 144, value of pi and factorial of 6.")
import math

print("Square Root of 144:", math.sqrt(144))
print("Value of Pi:", math.pi)
print("Factorial of 6:", math.factorial(6))
print()

# Q4: Import the random module and generate a random number between 1 and 100 and a random choice from ['Python', 'Java', 'React', 'Django'].
print("Q4: Import the random module and generate a random number between 1 and 100 and a random choice from ['Python', 'Java', 'React', 'Django'].")
import random

print("Random Number:", random.randint(1, 100))
print("Random Choice:",
      random.choice(["Python", "Java", "React", "Django"]))
print()

# Q5: Create a custom module area.py with functions area_circle() and area_rectangle(). Import the module and calculate areas.
print("# Q5: Create a custom module area.py with functions area_circle() and area_rectangle(). Import the module and calculate areas.")
import mod_area

radius = 7
length = 10
breadth = 5
print(f"Radius = {radius}\nLength = {length}\nBreadth = {breadth}")
print("Area of Circle:",
      mod_area.area_circle(radius))

print("Area of Rectangle:",
      mod_area.area_rectangle(length, breadth))