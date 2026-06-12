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