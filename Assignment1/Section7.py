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