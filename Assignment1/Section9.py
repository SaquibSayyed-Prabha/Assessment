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