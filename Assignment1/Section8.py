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