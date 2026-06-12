# Section 1: print(), input(), Variables & Naming Rules
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
print("Hello ", name, ", you are ", age, " years old.")   
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