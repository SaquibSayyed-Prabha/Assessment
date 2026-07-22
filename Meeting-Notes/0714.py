# - copy:
# - A copy creates a completely new array.
# - The copied array has its own memory location.
# - changing the copied array does not affect the original array.

# Syntax>
# array.copy()

# Example:-

# import numpy as np
# arr = np.array([10,20,30])
# new_arr = arr.copy()
# new_arr[0]=100
# print(new_arr)
# print(arr)


# - view()
#  - A view shares the same memory as the original array.
#  - changing the view also changes the original array.

#  Syntax:
#  array.view()

# import numpy as np

# arr = np.array([10,20,30])
# view_arr = arr.view()
# view_arr[0]=500
# print("Original array")
# print(arr)
# print("View array")
# print(view_arr)


# *** Random Module
# - The Random Module in numpy is used to generate random numbers.

# rand()
# randint()
# choice()
# seed()

# 1. rand()
# - rand() generates random decimal (floating-point) numbers between:-  0.0 -> 1.0

# syntax:
# np.random.rand()

# Example:
# import numpy as np
# print(np.random.rand())


# Generate a 2 * 3 matrix
# import numpy as np

# print(np.random.rand(2,3))


# 1.randint()
# -> randint() generates random integers within a specified range.

# syntax:
# np.random.randint(start,stop,size)
# start -> starting value
# stop -> Ending value
# size -> Number of value or array shape

# Example:
# import numpy as np

# print(np.random.randint(1,100))



# import numpy as np

# print(np.random.randint(1,100,10))


# choice()
# -> choice() randomly selects values from a given list or array.

# syntax:-
# np.random.choice(array,size)

# Example:-


# import numpy as np

# fruits = ["Apple","Mango","Banana","Orange"]
# print(np.random.choice(fruits))


# import numpy as np

# fruits = ["Apple","Mango","Banana","Orange"]
# print(np.random.choice(fruits,3))


# seed()
# -> seed() fixes the random numbers so that the same output is generated every time.

# syntax:
# np.random.seed()

# Example:
# import numpy as np

# np.random.seed(10)
# print(np.random.randint(1,100,5))




# *** Handling Missing Values , Filtering arrays & Conditional  Selection


# student dataset
# id   name   age   class  marks
# 1    a           2nd    40
# 2    b       20   3rd    



# What is np.nan ?
# - np.nan stands for not a Number.
# it is used to repesent missing or unknown values in a numpy array.

# syntax:
# np.nan

# Example:
# import numpy as np

# marks = np.array([85,90,np.nan,76,88])
# print(marks)


# Why Use np.nan?
#  Insted of writing: 0 or -1
# we use NaN because  it clearly indicates that the value is missing ,not zero.


# np.isnan()
# -> np.isnan() checks whether each element is NaN.
# it returns:
# True -> Missing value
# False -> Valid value


# syntax:
# np.isnan(array)


# Example:

# import numpy as np

# marks = np.array([85,90,np.nan,76,88,np.nan])
# print(np.isnan(marks))



# Coutnting Missing Values.

# Example:
# import numpy as np
# marks = np.array([60,90,np.nan,76,70,96,np.nan,95,np.nan])
# count = np.sum(np.isnan(marks))
# print(count)


# nan_to_num()
# -> it is replaces missing values(NaN) with a specified numbers.

# syntax:
# np.nan_to_num(array)

# Example:
# import numpy as np
# marks = np.array([60,90,np.nan,76,70,96,np.nan,95,np.nan])
# print(np.nan_to_num(marks))


# * Replace NaN with 50.
# import numpy as np
# marks = np.array([60,90,np.nan,76,70,96,np.nan,95,np.nan])
# print(np.nan_to_num(marks,nan=50))


