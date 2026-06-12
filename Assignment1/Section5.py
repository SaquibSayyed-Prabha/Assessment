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