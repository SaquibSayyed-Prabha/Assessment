# Assignment 9 - File Handling 
print("Assignment 9 – File Handling")
print()

# Q1. Create a file named student.txt and write your name into it. 
print("Q1. Create a file named student.txt and write your name into it. ")
file = open("Student.txt","x")
file = open("Student.txt","w")
file.write("Name: Saquib Sayyed")
file.close()
print()

# Q2. Read data from student.txt. 
print("Q2. Read data from student.txt. ")
file = open("Student.txt","r")
data = file.read()
print(data)
file.close()
print()

# Q3. Append your city name to the file. 
print("Q3. Append your city name to the file. ")
file = open("Student.txt","a")
file.write("\nCity: Pune")
file.close()
file = open("Student.txt","r")
data = file.read()
print(data)
file.close()
print()

# Q4. Read the file using readline(). 
print("Q4. Read the file using readline(). ")
file = open("Student.txt","r")
data = file.readline()
print(data)
file.close()
print()

# Q5. Check whether a file exists or not. 
print("Q5. Check whether a file exists or not.")
import os
if os.path.exists("students.txt"):
    print("File Exists")
else:
    print("File not found")
print()

# Q6. Create a program to store 5 student names in a file and display them. 
print("Q6. Create a program to store 5 student names in a file and display them. ")
file = open("Student.txt","w")
file.write("")
file = open("Student.txt","a")
for i in range(5):
    name = input(f"Enter Student {i+1} name: ")
    file.write(f"\nStudent {i+1}: {name}")
file = open("Student.txt","r")
data = file.read()
print(data)
file.close()
print()
