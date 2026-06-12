# Section 2: Data Types & Type Conversion
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