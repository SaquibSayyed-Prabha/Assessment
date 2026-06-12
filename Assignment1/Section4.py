# Section 4: Conditional Statements (if / elif / else) 
print("Section 4: Conditional Statements (if / elif / else)")
print()

# Q13. Take marks as input and print grade: 
# - A -> 90 and above 
# - B -> 75 to 89 
# - C -> 50 to 74 
# - Fail -> below 50 
print("Q13. Take marks as input and print grade: A -> 90 and above, B -> 75 to 89, C -> 50 to 74, Fail -> below 50.")
marks = float(input("Enter marks: "))  
if marks >= 90:
    print("Grade: A")       
elif marks >= 75:               # 'elif' is used to check multiple conditions.
    print("Grade: B")           # If the first condition is false, it checks the next condition.
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")
print()

# Q14. Write a program to check whether a number is even or odd. 
print("Q14. Write a program to check whether a number is even or odd.")
num = int(input("Enter a number: "))
if num % 2 == 0:        # modulus operator is used to check the remainder when num is divided by 2. 
    print("EVEN")       # If the remainder is 0, then the number is even, otherwise it is odd.
else:
    print("ODD")
print()

# Q15. Take age as input and determine: 
# - Child 
# - Teenager 
# - Adult 
# - Senior Citizen 
print("Q15. Take age as input and determine: Child, Teenager, Adult, Senior Citizen.")
age = int(input("Enter age: "))    
if age < 1:
    print("Invalid age")
elif age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior Citizen")
print()

# Q16. Create a simple calculator using if-elif-else.
# Operations: 
# - Addition 
# - Subtraction 
# - Multiplication 
# - Division 
print("Q16. Create a simple calculator using if-elif-else. Operations: Addition, Subtraction, Multiplication, Division.")
equation = input("Enter simple equation (e.g., 1+2): ")
num1, operation, num2 = equation.split()  # split() is used to split the input string into three parts: num1, operation, and num2.
num1 = int(num1)                          # Convert num1 from string to integer
num2 = int(num2)  

if operation == "+":
    print(f" {num1} + {num2} = {num1 + num2}")
elif operation == "-":
    print(f" {num1} - {num2} = {num1 - num2}")
elif operation == "*":
    print(f" {num1} * {num2} = {num1 * num2}")
elif operation == "/":
    print(f" {num1} / {num2} = {num1 / num2}")
else:
    print("Invalid operation")