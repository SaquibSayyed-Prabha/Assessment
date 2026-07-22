# File Handling

# What is File Handling.
# File Handling is the process of creating ,opening,reading,writing,updating,and deleting files using python.
# A File is used to store data permanently on a computer.

# 

# Advantages
 # Permanent Data Storage
 # Easy Data Management
 # Store Large Amounts of data
 # Data sharing
 


# Types of files

 # 1.  Text File(.txt)
     # notes,employee data,
     # Example
     # note.txt
     
# Binary File(.bin)
 # images,videos,Audio,pdf files
 # file_name.bin
 

# File handling Operations
# Open File
# Read File
# write File
# Append Data
# Close File
# Delete File


# open() function
 #Used to open a file.
 # Syntax
   # open(filename,mode) 
   
   
# File modes
# Mode       Meaning
# r          Read
# w          write
# a          append
# x          create
# r+         read+write
# w+         write + read
# a+         Append + Read



# 1: Read


# Example

# read() - reads entire file content.

# file = open("student.txt","r")
# data = file.read()
# print(data)
# file.close()

# readline() - reads one line at a time

# file = open("student.txt","r")
# data = file.readline()
# print(data)
# file.close()


# readlines() - Reads all lines and returns a list

# file = open("student.txt","r")
# data = file.readlines()
# print(data)
# file.close()



# 2: write

# Write()
# Used to write data into a file
# if file exists -> old data removed
# if file doesn't exist -> new file created

# Example


# file = open("student.txt","w")
# file.write("Welcome to Python")
# file.close()



# file = open("employee.txt","w")
# file.write("Welcome to Prabha tech")
# file.close()



# Append mode (a)
# Adds new data at the end of file.

# file = open("student.txt","a")
# file.write("Programing")
# file.close()


# Create File (x)

# Create a new file
# Raise error if file already exists


# Example
# file = open("intern.txt","x")
# file.close()


# file = open("intern.txt","w")
# file.write("Welcome to interns")
# file.close()


# Using with Statement
 # Automatically closes the file.

# Syntax 
# with open(filename,mode) as variable

# Example

# with open("student.txt","r") as file:
#  print(file.read())

# File exists check

# import os
# if os.path.exists("student.txt"):
#  print("File Exists")
# else:
#  print("File not found")

# Delete File

# import os
# os.remove("intern.txt")


# with open("student.txt","w") as file:
#  file.write("Java programming\n")
#  file.write("C++ programming\n")


# with open("student.txt","a") as file:
#  file.write("\nGoprogramming")