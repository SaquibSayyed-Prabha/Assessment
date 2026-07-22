# // Reshaping Arrays

# - Reshaping means changing tha shape (dimensions) of an array without changing its data.


# arr = [65,80,90,90,30,50,40,30,60,70,66,77]

# 3 rows and 4 columns

# 65   80  90  90
# 30   50  40  30
# 60   70  66  77



# - What is reshape()
# -> reshape() changes the dimensions of an array into a new shape.
#   it returns a new reshaped array without modifying the original array.

# Syntax:
# array_name.reshape(rows,columns)
# or
# np.reshape(array,(rows,columns))



# Rules of reshape:
# The total number of elements must be remain the same.
# Formula:
# Rows * Columns  = Total elements

# Example:
# Array containes 12 elements

# Valide Shapes:
# 12 * 1 = 12
# 6 * 2 = 12
# 4 * 3 = 12    
# 3 * 4 = 12
# 2 * 6 = 12
# 1 * 12 = 12

# 5 * 3 = 15 - it is invalide shape


# Example:
# Convert 1D array to 2D

# import numpy as np
# arr = np.array([10,20,30,40,50,60])
# new_arr = arr.reshape(2,3)
# print(new_arr)
# print(arr)


# Convert 2D Array to 3D Array

# import numpy as np
# arr = np.arange(1,13)
# # print(arr)
# new_arr = arr.reshape(3,2,2)
# print(new_arr)




# Convert 3D Array to 1D Array
# # Convert 3D Array to 1D Array

# import numpy as np
# arr = np.arange(1,9)
# three_d = arr.reshape(2,2,2)
# print(arr)
# print(three_d)
# print("1D array")
# print(three_d.reshape(8))