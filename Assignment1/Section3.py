# Section 3: Operators 
print("Section 3: Operators")
print()

# Q9. Write a program to perform: 
# - Addition 
# - Subtraction 
# - Multiplication 
# - Division 
# - Modulus 
# on two user-input numbers. 
print("Q9. Write a program to perform: Addition, Subtraction, Multiplication, Division, Modulus on two user-input numbers.")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f" {num1} + {num2} = {num1 + num2}")       # operators are used to perform operations on variables and values.
print(f" {num1} - {num2} = {num1 - num2}")       # arithmetic operators are used to perform mathematical operations like addition, subtraction, etc.
print(f" {num1} * {num2} = {num1 * num2}")
print(f" {num1} / {num2} = {num1 / num2}")
print(f" {num1} % {num2} = {num1 % num2}")
print()

# Q10. Take two numbers and display comparison results using: 
# - Greater than 
# - Less than 
# - Equal to 
# - Not equal to 
print("Q10. Take two numbers and display comparison results using: Greater than, Less than, Equal to, Not equal to.")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f" {num1} > {num2} = {num1 > num2}")            # relational operators are used to compare values and return a boolean result (True or False).
print(f" {num1} < {num2} = {num1 < num2}")               
print(f" {num1} == {num2} = {num1 == num2}")
print(f" {num1} != {num2} = {num1 != num2}")
print()

# Q11. Create a login system using logical operators: 
# - Username must be "admin" 
# - Password must be "1234" 
# Display login success or failure.
print("Q11. Create a login system using logical operators: Username must be 'admin', Password must be '1234'. Display login success or failure.")
username = input("Enter username: ")
password = input("Enter password: ")
                                                      # Indentation defines the scope of loops, functions, and other code blocks.
if username == "admin" and password == "1234":        # 'and' is a logical operator that returns True if both conditions are true, otherwise it returns False.
    print("Login successful!")
else:
    print("Login failed!")
print()

# Q12. Write a program to check whether a number is: 
# - Positive 
# - Negative 
# - Zero 
print("Q12. Write a program to check whether a number is: Positive, Negative, Zero.")
num = float(input("Enter a number: "))
if num > 0:
    print("POSITIVE")
elif num < 0:
    print("NEGATIVE")
else:
    print("ZERO")