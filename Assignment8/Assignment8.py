# Assignment 8 - Exception Handling 
print("Assignment 8 – Exception Handling")
print()

# Q1. Handle Division by Zero 
# Write a program that: 
# - Takes two numbers as input. 
# - Divides the first number by the second number. 
# - Handles the ZeroDivisionError exception. 
print("Q1. Handle Division by Zero")
try:
    num = int(input("Enter a Number:"))
    result = 100/num
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Please enter only real numbers")
print()


# Q2. Handle Invalid Number Input 
# Write a program that: 
# - Takes a number from the user. 
# - Handles the ValueError exception if the user enters text instead of a number. 
print("Q2. Handle Invalid Number Input ")
try:
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))
    result = num1 / num2
except ValueError:
    print("Invalid Input")
print()


# Q3. Using try and except 
# Write a program that: 
# - Creates a list containing 5 numbers. 
# - Takes an index from the user. 
# - Prints the element at that index. 
# - Handles the IndexError exception. 
print("Q3. Using try and except ")
l1 = [1, 2, 3, 4, 5]
try:
    num = int(input("Enter index: "))
    print(l1[num])

except IndexError:
    print("Index out of range")
print()


# Q4. Using else Block 
# Write a program that: 
# - Takes two numbers as input. 
# - Performs division. 
# - Uses else to display the result when no exception occurs. 
print("Q4. Using else Block ")
try:
    num1 = int(input("Enter a Number"))
    num2 = int(input("Enter 1st number: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid Input")
else:
    print("Result = ", result)
print()


# Q5. Using finally Block 
# Write a program that: 
# - Opens a file using open(). 
# - Uses try-except-finally. 
# - Prints a message in the finally block. 
print("Q5. Using finally Block")
try:
    file = open("File.txt","r")
except FileNotFoundError:
    print("File Not Fund")
finally:
    print("This block always executes") 
print()


# Q6. Multiple Exceptions 
# Write a program that: 
# - Takes a number and an index from the user. 
# - Handles both: 
#     1. ValueError 
#     2. IndexError 
print("Q6. Multiple Exceptions ")
l1 = [1, 2, 3]
try:
    num1 = int(input("Enter a Number: "))
    ind1 = int(input("Enter index: "))
    l1.insert(num1, ind1)
except ValueError:    
    print("Invalid input")
except IndexError:
    print("Index out of range")
print()


# Q7. Custom Exception 
# Create a custom exception named NegativeNumberError. 
# - Take a number from the user. 
# - Raise the exception if the number is negative. 
# - Display an appropriate error message. 
print("Q7. Custom Exception ")
class NegativeNumberError(Exception):
    pass

num = int(input("Enter a number: "))
if num < 0:
    raise NegativeNumberError("Negative numbers are not allowed. ")