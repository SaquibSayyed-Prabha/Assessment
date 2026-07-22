# Exception Handling

# What is Exception Handling.
 # Exception Handling is a process used to handle runtime errors in a program so that the program does not crash unexpectedly.
 
 # compile time error
    #syntax wrong
    # :(
     
 # runtime error
 


# Example

# num=10
# print(num/0)


# What is Exception
# An Exception is an error that occurs during the execution(runtime) of a program

# Common Exception

# ZeroDivisionError
# ValueError
# TypeError
# NameError
# IndexError
# KeyError
# FileNotFoundError


# try and except

# Syntax:
# try:
#  # Risky code
# except:
#  # Error handling code

# Ex
# try:
#  num = 10/0
# except:
#  print("Error Occurred")


# Example

# try:
#  num = int(input("Enter a Number:"))
#  result = 10/num
#  print(result)
# except ZeroDivisionError:
#  print("Cannot divide by zero:")
# except ValueError:
#  print("Please enter only numbers:")


# Using Exception Object

# try:
#  num = 10/0
# except ZeroDivisionError as e:
#  print("Error:",e)


# else block
# The else block executes only when no exception occurs.

# Syntax:
# try:
#  #  Risky code
# except:
#  # Error handling
# else:
#  # Executes if no error

# try:
#    num = int(input("Enter a Number:"))
#    result = 10/num
#    print(result)
# except ZeroDivisionError:
#    print("Cannot divide by zero:")
# else:
#  print("Program executed successfully")


# finally block
# The finally block always executes whether an exception occurs or not.

# try:
#  print(10/0)
# except:
#  print("Error")
# finally:
#  print("This block always executes") 

# Complted Example

# try:
#  num = int(input("Enter a Number"))
#  result = 100 / num
# except ZeroDivisionError:
#  print("Cannot divide by zero")
# except ValueError:
#  print("Invalid input")
# else:
#  print("Result:",result)
# finally:
#  print("Program Ended")

# raise key word
# we can create our own exception using the raise keyword



# age = int(input("Enter a Age:"))
# if age<18:
#  raise ValueError("Age must be 18 or above")

# print("Eligible")

# Custom Exception

# class InvalidAgeError(Exception):
#  pass

# age = 15
# if age<18:
#  raise InvalidAgeError("Age must be greater than 18")

# Real life example
# ATM

# try:
#  balance = 5000
#  amount = int(input("Enter a Amount:"))
 
#  if amount > balance:
#   raise ValueError("Insufficient Balance")
#  else:
#   print("Withdrawal Successfully")
# except ValueError as e:
#  print(e)
# finally:
#  print("Thank You For Using ATM")

