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