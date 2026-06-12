# Assignment 1 - Python Basics + Control Flow
print("Assignment 1 - Python Basics + Control Flow")

# Section 1: 
# print(), input(), Variables & Naming Rules
print("Section 1: print(), input(), Variables & Naming Rules")
print()     #print function by default adds a new line

# Q1. Write a program to display your name, college name, and favorite programming language using print().
print("Q1. Write a program to display your name, college name, and favorite programming language using print().")
print("This is Sayyed Saquib")   # print() is used to display the output on the console
print("I am studying at Zeal Polytechnic, Pune")
print("I like to learn and work with Python programming language") 
print()
 
# Q2. Take user input for name and age, then display: "Hello Saquib, you are 18 years old." 
print("Q2. Take user input for name and age, then display: 'Hello Saquib, you are 18 years old.'")
name = input("Enter your name: ")                         #input() is used to take user input as a string by default
age = int(input("Enter your age: "))                      #int() is used to convert the input string to an integer
print("Hello ", name, ", you are ", age, " years old.")   #f-string is used to format the string with variables
print()

# Q3. Create variables for: 
# - Student name 
# - Roll number 
# - Percentage 
# - Passed status 
# Print all values in a formatted way.
print("Q3. Create variables for: Student name, Roll number, Percentage, Passed status. Print all values in a formatted way.")
student_name = "Saquib" # string value
roll_number = 54        # integer value
percentage = 85.5       # float value
passed_status = True    # boolean value
print(f"Student Name:  {student_name}")
print(f"Roll Number:   {roll_number}")
print(f"Percentage:    {percentage}")
print(f"Passed Status: {passed_status}")
print() 

# Q4. Identify which of the following variable names are invalid and rewrite them correctly: 
# - 1name 
# - student-name 
# - class
# - total marks 
# - user_name 
print("Q4. Identify which of the following variable names are invalid and rewrite them correctly:")
print("1. 1name        - is invalid because identifiers cannot start with a digit.")
print("2. student-name - is invalid because identifiers cannot contain symbols.")
print("3. class        - is invalid because it is a reserved keyword and identifiers cannot be the same as reserved keywords.")
print("4. total marks  - is invalid because identifiers cannot contain spaces.")
print("5. user_name    - is valid. Identifiers can contain letters, digits, and underscores.")
print("\n\n")                   # \n is used for new line

# Section 2: 
# Data Types & Type Conversion
print("Section 2: Data Types & Type Conversion")
print()

# Q5. Create variables of type: 
# - int 
# - float 
# - str 
# - bool 
# Print each variable with its data type using type(). 
print("Q5. Create variables of type: int, float, str, bool. Print each variable with its data type using type().")
num = 10        # integer value contains whole numbers without a decimal point
dec = 10.5      # float value contains numbers with a decimal point
word = "Hello"  # string value has a sequence of characters enclosed in quotes
flag = True     # boolean value contains either True or False
# type() is used to check the data type of a variable
print(f"Integer variable num: {num}, datatype: {type(num)}")
print(f"Float variable dec: {dec}, datatype: {type(dec)}")
print(f"String variable word: {word}, datatype: {type(word)}")
print(f"Boolean variable flag: {flag}, datatype: {type(flag)}")
print()

# Q6. Take two numbers as input from the user and display their sum. 
print("Q6. Take two numbers as input from the user and display their sum.")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2
print(f"{num1} + {num2} = {sum}")
print()

# Q7. Take a decimal number as input and convert it into: 
# - integer 
# - string 
# Display all converted values. 
print("Q7. Take a decimal number as input and convert it into integer and string.")  
decimal = float(input("Enter a decimal number: "))
number = int(decimal)
sequence = str(decimal)
print(f"Original decimal number: {decimal}, datatype: {type(decimal)}")
print(f"Converted to integer: {number},\ndatatype: {type(number)}")
print(f"Converted to string: {sequence},\ndatatype: {type(sequence)}")
print()

# Q8. Take user input for age and check whether the input type is string or integer. 
print("Q8. Take user input for age and check whether the input type is string or integer.")
age = input("Enter your age: ")
print(f"Input type: {type(age)}")
print("\n\n")                   

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
print("\n\n")

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
print("\n\n")

# Section 5: Loops (for & while) 
print("Section 5: Loops (for & while)")
print()

# Q17. Print numbers from 1 to 20 using a for loop. 
print("Q17. Print numbers from 1 to 20 using a for loop.")
for i in range(1, 21):   # range() is used to generate a sequence of numbers. Here, it generates numbers from 1 to 20 (21 is exclusive).
    print(i)
print()

# Q18. Print all even numbers between 1 and 50. 
print("Q18. Print all even numbers between 1 and 50.")
for i in range(1, 51):
    if i % 2 == 0:        
        print(i)
print()

# Q19. Print the multiplication table of a user-input number. 
print("Q19. Print the multiplication table of a user-input number.")
num = int(input("Enter a number: "))
for i in range(1, 11):                      # for loop is used to iterate over a sequence of numbers. 
    print(f"{num} x {i} = {num * i}")
print()

# Q20. Use a while loop to print numbers from 10 to 1. 
print("Q20. Use a while loop to print numbers from 10 to 1.")
i = 10
while i >= 1:             # while loop is used to execute a block of code repeatedly as long as the condition is true.
    print(i)
print()

# Q21. Write a program to calculate the sum of numbers from 1 to 100. 
print("Q21. Write a program to calculate the sum of numbers from 1 to 100.")
total_sum = 0
for i in range(1, 101):
    total_sum += i
print(f"Sum of numbers from 1 to 100: {total_sum}")
print()

# Q22. Take a number from the user and count how many digits it contains. 
print("Q22. Take a number from the user and count how many digits it contains.")
num = input("Enter a number: ")
digit_count = len(num)
print(f"Number of digits in {num}: {digit_count}")
print()

# Section 6: break & continue 
print("Section 6: break & continue")
print()

# Q23. Print numbers from 1 to 20, but stop the loop when the number becomes 15. 
print("Q23. Print numbers from 1 to 20, but stop the loop when the number becomes 15.")
for i in range(1, 21):
    if i == 15:
        break   # break is used to exit the loop when the condition is met.
    print(i)
print()

# Q24. Print numbers from 1 to 20, skipping all multiples of 3. 
print("Q24. Print numbers from 1 to 20, skipping all multiples of 3.")
for i in range(1, 21):
    if i % 3 == 0:
        continue    # continue is used to skip the current iteration of the loop when the condition is met.
    print(i)
print()

# Q25. Create a password checking system that keeps asking until the correct password is entered. 
print("Q25. Create a password checking system that keeps asking until the correct password is entered.")
correct_password = "password123"
while True:
    password = input("Enter password: ")
    if password == password:
        print("Password correct!")
        break
    else:
        print("Incorrect password. Try again.")
print()

# Section 7: Nested Loops 
print("Section 7: Nested Loops")
print()

# Q26. Print the following pattern: 
# * 
# ** 
# *** 
# **** 
# ***** 
print("Q26. Print the following pattern:")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")  # end="" is used to print the stars on the same line without adding a new line after each star.
    print()  
print()

# Q27. Print a multiplication table from 1 to 5 using nested loops. 
print("Q27. Print a multiplication table from 1 to 5 using nested loops.")
for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()
print()

# Q28. Create a number square pattern: 
# 1111 
# 2222 
# 3333 
# 4444 
print("Q28. Create a number square pattern:")
for i in range(1, 5):
    for j in range(4):
        print(i, end="")
    print()
print()

# Section 8: Lists 
print("Section 8: Lists")
print()

# Q29. Create a list of 5 student names and print: 
# - First student 
# - Last student 
# - Total number of students 
print("Q29. Create a list of 5 student names and print: First student, Last student, Total number of students.")
students = ["Saquib", "Atharva", "Suraj", "Rohit", "Chetana"]
print(f"First student: {students[0]}")                 # List indexing starts from 0, so students[0] gives the first student in the list.
print(f"Last student: {students[-1]}")                 # Negative indexing is used to access elements from the end of the list.   
print(f"Total number of students: {len(students)}")    # len() is used to get the total number of elements in the list.
print()

# Q30. Take 5 numbers from the user and store them in a list. 
print("Q30. Take 5 numbers from the user and store them in a list.")
numbers = []
for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)
print(f"Numbers entered: {numbers}")
print()

# Q31. Perform the following operations on a list: 
# - append() 
# - remove() 
# - pop() 
# - sort() 
print("Q31. Perform the following operations on a list: append(), remove(), pop(), sort().")
list1 = [5, 2, 9, 1, 3]
print("Original list:", list1)
list1.append(4)                   # append() is used to add an element to the end of the list.
print("After append(4):", list1)
list1.remove(2)                   # remove() is used to remove the first occurrence of an element from the list.
print("After remove(2):", list1)
list1.pop()                       # pop() is used to remove the last element from the list.
print("After pop():", list1)
list1.sort()                      # sort() is used to sort the elements of the list in ascending order.
print("After sort():", list1)
print()

# Q32. Print all elements of a list using a loop. 
print("Q32. Print all elements of a list using a loop.")
Gen_AI = ["ChatGPT", "Grook", "Gemini", "Claude", "Meta"]
print("List of Generative AI models:")
for model in Gen_AI:
    print(model)
print()

# Q33. Find: 
# - Maximum value 
# - Minimum value 
# - Sum of all elements 
# from a number list. 
print("Q33. Find: Maximum value, Minimum value, Sum of all elements from a number list.")
num_list = [10, 5, 8, 3, 12]
print("Maximum value:", max(num_list))
print("Minimum value:", min(num_list))
print("Sum of all elements:", sum(num_list))
print()

# Q34. Create a list of 10 numbers and print: 
# - First 5 elements 
# - Last 3 elements 
# - Alternate elements using slicing 
print("Q34. Create a list of 10 numbers and print: First 5 elements, Last 3 elements, Alternate elements using slicing.")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("First 5 elements:", numbers[:5])          # Slicing is used to access a range of elements from the list.
print("Last 3 elements:", numbers[-3:])          # Negative indexing is used to access elements from the end of the list.
print("Alternate elements:", numbers[::2])       # Step size is used to access every second element.
print("\n\n")

# Section 9: Tuples 
print("Section 9: Tuples")
print()

# Q35. Create a tuple containing: 
# - Name 
# - Age 
# - City 
# Print all values separately. 
print("Q35. Create a tuple containing: Name, Age, City. Print all values separately.")
person = ("Saquib", 18, "Pune")  
print("Name:", person[0])
print("Age:", person[1])
print("City:", person[2])
print()

# Q36. Try changing a tuple value and observe what happens. 
print("Q36. Try changing a tuple value and observe what happens.")
my_tuple = (1, 2, 3)
print("Original tuple:", my_tuple)
                                   # Tuples are immutable, which means that once a tuple is created, its values cannot be changed.
try:                               # Using try-except block to catch the TypeError that occurs when trying to change a tuple value.
    my_tuple[0] = 10               # This will raise a TypeError because tuples do not support item assignment.
except TypeError as e:
    print("Error:", e)
print()

# Q37. Create a tuple with 5 numbers and find: 
# - Maximum value 
# - Minimum value 
# - Total sum 
print("Q37. Create a tuple with 5 numbers and find: Maximum value, Minimum value, Total sum.")
num_tuple = (10, 5, 8, 3, 12)
print("Maximum value:", max(num_tuple))      # max() is a built-in function used to find the maximum value.
print("Minimum value:", min(num_tuple))      # min() is a built-in function used to find the minimum value.
print("Total sum:", sum(num_tuple))          # sum() is a built-in function used to calculate the total sum of all elements.
print()

# Q38.Perform tuple packing and unpacking using student details. 
print("Q38. Perform tuple packing and unpacking using student details.")
student_details = ("Sayyed", 18, "Pune")  # Tuple packing is the process of creating a tuple by grouping multiple values together.
name, age, city = student_details          # Tuple unpacking is the process of assigning the values from a tuple to individual variables.
print("Name:", name)
print("Age:", age)
print("City:", city)
print()

# Q39. Create a mini ATM menu: 
# - Check balance 
# - Deposit 
# - Withdraw 
# - Exit 
# Use loops and conditional statements. 
print("Q39. Create a mini ATM menu: Check balance, Deposit, Withdraw, Exit. Use loops and conditional statements.")
balance = 1000.0
while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = input("Enter: ")
    
    if choice == '1':
        print(f"Your current balance: ${balance:.2f}")
    elif choice == '2':
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print(f"${amount:.2f} deposited successfully. New balance: ${balance:.2f}")
    elif choice == '3':
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient funds.")
        else:
            balance -= amount
            print(f"${amount:.2f} withdrawn successfully. New balance: ${balance:.2f}")
    elif choice == '4':
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
print()

# Q40. Create a student result management program using lists and conditions. 
# Requirements: 
# - Store student marks 
# - Calculate average 
# - Display grade with respect to students
# - Show student with highest marks
print("Q40. Create a student result management program using lists and conditions.")
students = []
marks = []

for i in range(5):
    name = input(f"Enter name of student {i+1}: ")
    students.append(name)
    mark = float(input(f"Enter marks of student {i+1}: "))
    marks.append(mark)

# Calculate average
average = sum(marks) / len(marks)
print(f"\nAverage marks: {average:.2f}")    

# Display grade for each student
for i in range(len(students)):
    if marks[i] >= 90:
        grade = "A"
    elif marks[i] >= 75:
        grade = "B"
    elif marks[i] >= 50:
        grade = "C"
    else:
        grade = "Fail"
    print(f"{students[i]}: Marks = {marks[i]}, Grade = {grade}")

# Show highest marks
highest_mark = max(marks)
highest_student = students[marks.index(highest_mark)]
print(f"Highest marks: {highest_mark} ({highest_student})")