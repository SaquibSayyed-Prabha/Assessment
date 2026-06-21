# Assignment 2 - Dictionaries, Sets & Functions
print("Assignment 2 – Dictionaries, Sets & Functions")
print()

# Section 1: 
# Dictionary Challenges
print("Section 1: Dictionary Challenges")
print()

# Q1. Create a dictionary to store: 
# - Student name 
# - Age 
# - Course 
# - City 
# Print all dictionary values. 
print("Q1. Create a dictionary to store: Student name, Age, Course, City and print all dictionary values.")
student_details = {
    "name": "Saquib",
    "age": 18,
    "course": "AI&ML",
    "city": "Pune"
}
for value in student_details.values():
    print(value)
print()

# Q2. Create a dictionary of employee details and access: 
# - Employee name 
# - Salary 
# - Department 
# using keys. 
print("Q2. Create a dictionary of employee details and access: Employee name, Salary, Department using keys.")
employee_details = {
    "name": "Saquib",
    "salary": 50000,
    "department": "Computer Science"
}
print("Employee Name:", employee_details["name"])
print("Salary:", employee_details["salary"])
print("Department:", employee_details["department"])
print()

# Q3. Add a new key-value pair to an existing dictionary. 
# Example: 
# - Add "email" to student details. 
print("Q3. Add a new key-value pair to an existing dictionary.")
student_details["email"] = "abc@xyz.com"
print(student_details)
print()

# Q4. Update the value of an existing key in a dictionary. 
print("Q4. Update the value of an existing key in a dictionary.")
print("Before updating age:\n", student_details)
student_details["age"] = 19
print("After updating age:\n", student_details)
print()

# Q5. Remove a key from a dictionary using: 
# - pop() 
# - del 
print("Q5. Remove a key from a dictionary using: pop() and del")
student_details.pop("email")
print("After using pop():\n", student_details)
del student_details["city"]
print("After using del():\n", student_details)
print()

# Q6. Print all: 
# - Keys 
# - Values 
# - Key-value pairs 
# from a dictionary using loops. 
print("Q6. Print all: Keys, Values, Key-value pairs from a dictionary using loops.")
print("Keys:")
for key in student_details:
    print(key)
print("Values:")
for value in student_details.values():
    print(value)
print("Key-value pairs:")
for key, value in student_details.items():
    print(key, ":", value)
print()

# Q7. Count how many subjects are present in a student marks dictionary. 
print("Q7. Count how many subjects are present in a student marks dictionary.")
student_marks = {
    "Math": 85,
    "Science": 90,
    "English": 78,
    "History": 88,
    "Geography": 92
}
print("Number of subjects:", len(student_marks))
print()

# Q8. Create a dictionary containing marks of 5 subjects and calculate the total marks. 
print("Q8. Create a dictionary containing marks of 5 subjects and calculate the total marks.")
total_marks = sum(student_marks.values())
print("Total marks:", total_marks)
print()

# Q9. Check whether a key exists in a dictionary or not. 
print("Q9. Check whether a key exists in a dictionary or not.")
if "Math" in student_marks:
    print("Math is present in the dictionary.")
else:
    print("Math is not present in the dictionary.")
print()

# Q10. Create a dictionary of products with prices and display only products having price greater than 500. 
print("Q10. Create a dictionary of products with prices and display only products having price greater than 500.")
products = {
    "Laptop": 50000,
    "Mouse": 150,
    "Keyboard": 300,
    "Monitor": 800,
    "Headphones": 600
}
print("Products with price greater than 500:")
for product, price in products.items():
    if price > 500:
        print(product, ":", price)
print()

# Section 2: Set Challenges 
print("Section 2: Set Challenges")
print("\n\n")

# Q11. Create a set containing 5 numbers and print all elements. 
print("Q11. Create a set containing 5 numbers and print all elements.")
set1 = {1, 2, 3, 4, 5}
print("Elements in the set:")
for i in set1:
    print(i, ",",end="")
print()

# Q12. Add new elements into a set using add(). 
print("Q12. Add new elements into a set using add().")
set1.add(6)
set1.add(7)
print("After adding new elements:")
for i in set1:
    print(i, ",",end="")
print()

# Q13. Remove an element from a set using: 
# - remove() 
# - discard() 
print("Q13. Remove an element from a set using: remove() and discard()")
set1.remove(3)
set1.discard(4)
print("After removing elements:")
for i in set1:
    print(i, ",",end="")
print()

# Q14. Create two sets and perform: 
# - Union 
# - Intersection 
# - Difference 
# operations. 
print("Q14. Create two sets and perform: Union, Intersection, Difference operations.")
setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}
print("Set A:", setA)
print("Set B:", setB)
print("Union:", setA.union(setB))
print("Intersection:", setA.intersection(setB))
print("Difference (A-B):", setA.difference(setB))
print()

# Q15. Find common elements between two sets. 
print("Q15. Find common elements between two sets.")
common = setA.intersection(setB)
print("Common elements between Set A and Set B:", common)
print()

# Q16. Check whether a particular value exists in a set. 
print("Q16. Check whether a particular value exists in a set.")
product = {"Penicl", "Eraser", "Notebook", "Ruler", "Marker", "Bag"}
print("Products in the set:", product)
search = input("Enter a product name to search: ")
if search in product:
    print(f"{search} is present in the set.")
else:
    print(f"{search} is not present in the set.")
print()

# Q17. Take a list containing duplicate values and convert it into a set. 
print("Q17. Take a list containing duplicate values and convert it into a set.")
my_list = [1, 2, 3, 4, 5, 1, 3, 4, 5, 6, 8, 1]
my_set = set(my_list)
print("Original list:", my_list)
print("Converted set:", my_set)
print()

# Q18. Create a set of student names and display the total number of unique students. 
print("Q18. Create a set of student names and display the total number of unique students.")
students = {"Saquib", "Atharva", "Suraj", "Rohit", "Ishwari", "Chetana"}
print("Unique students:", len(students))
print()

# Q19. Create two sets of numbers and check whether both sets are equal or not. 
print("Q19. Create two sets of numbers and check whether both sets are equal or not.")
setX = {1, 2, 3, 4, 5}
setY = {5, 4, 3, 2, 1}
print("Set X:", setX)
print("Set Y:", setY)
if setX == setY:
    print("EQUAL")
else:
    print("UNEQUAL")
print()

# Q20. Remove all elements from a set using clear(). 
print("Q20. Remove all elements from a set using clear().")
setX.clear()
print("After clearing setX:", setX)
print("\n\n")

# Section 3: Function Challenges
print("Section 3: Function Challenges")
print()

# Q21. Create a function that prints: 
# "Welcome to Python Programming" 
print("Q21. Create a function that prints: Welcome to Python Programming")
def message():
    print("Welcome to Python Programming")

message()
print()

# Q22. Create a function to add two numbers and display the result. 
print("Q22. Create a function to add two numbers and display the result.")
def add_numbers(num1, num2):
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is: {result}")
add_numbers(10, 20)
print()

# Q23. Create a function that accepts a name as a parameter and prints: 
# "Hello, Saquib!" 
print("Q23. Create a function that accepts a name as a parameter and prints: Hello, Saquib!")
def greet():
    name = input("Enter your name: ")
    print(f"Hello, {name}!")

greet()
print()

# Q24. Create a function to find the square of a number. 
print("Q24. Create a function to find the square of a number.")
def square(num):
    return num ** 2

number = int(input("Enter a number to find its square: "))
print(f"The square of {number} is: {square(number)}")
print()

# Q25. Write a function to check whether a number is even or odd. 
print("Q25. Write a function to check whether a number is even or odd.")
def check(num):
    if num % 2 == 0:
        print(f"{num} is an EVEN.")
    else:
        print(f"{num} is an ODD.")
number = int(input("Enter a number to check whether it is even or odd: "))
check(number)
print()

# Q26. Create a function to calculate the area of a rectangle. 
print("Q26. Create a function to calculate the area of a rectangle.")
def area(l, b):
    return l * b
length = int(input("Enter the length of the rectangle: "))
breadth = int(input("Enter the breadth of the rectangle: "))
print("The area of the rectangle is:", area(length, breadth))
print()

# Q27. Write a function that returns the greater number between two numbers. 
print("Q27. Write a function that returns the greater number between two numbers.")
def greater(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return "Both numbers are equal."
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
print("The greater number is:", greater(number1, number2))
print()

# Q28. Create a function to print numbers from 1 to 10. 
print("Q28. Create a function to print numbers from 1 to 10.")
def print_numbers():
    for i in range(1, 11):
        print(i, ",", end="")
print_numbers()
print()

# Q29. Write a function to calculate the sum of all numbers in a list. 
print("Q29. Write a function to calculate the sum of all numbers in a list.")
def total_sum(num):
    return sum(num)
numbers_list = [1, 2, 3, 4, 5]
print("The sum of all numbers in the list is:", total_sum(numbers_list))
print()

# Q30. Create a function that checks whether a student is pass or fail based on marks. 
# Condition: 
# - Pass → marks >= 35 
# - Fail → marks < 35 
print("Q30. Create a function that checks whether a student is pass or fail based on marks.")
def result(marks):
    if marks < 0 or marks > 100:
        return "Invalid marks. Please enter a value between 0 and 100."
    elif marks >= 35:
        return "PASS"
    else:
        return "FAIL"
print("Enter the marks:")
marks = int(input())
print("Result:", result(marks))
print()

# Q32. Create a function using keyword arguments. 
print("Q32. Create a function using keyword arguments.")
def addition(*args):
    total = sum(args)
    print("The sum of the numbers is:", total)
addition(10, 20, 30)
addition(2, 4, 6, 8)
addition(1, 2)
print()

# Q33. Write a function that accepts multiple numbers using *args and prints them. 
def numb(*args):
    print("The numbers are:")
    for num in args:
        print(num, ",", end=" ")
numb(10, 20, 30)
numb(2, 4, 6, 8)
numb(1, 2)
print()

# Q34. Create a function that returns: 
# - Maximum number 
# - Minimum number 
# from a list. 
print("Q34. Create a function that returns: Maximum number and Minimum number from a list.")
def max_min(num_list):
    max_num = max(num_list)
    min_num = min(num_list)
    return max_num, min_num
numbers = [10, 20, 5, 15, 30]
maximum, minimum = max_min(numbers)
print("Numbers in the list:", numbers)
print("Maximum number:", maximum)
print("Minimum number:", minimum)  
print()

# Q35. Write a function to count vowels in a string. 
print("Q35. Write a function to count vowels in a string.")
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

string = input("Enter a string to count vowels: ")
print("The number of vowels in the string is:", count_vowels(string))
print()