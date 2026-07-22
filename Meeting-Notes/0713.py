# Monday - 13/07/2026


# flatten()
# - The flatten() function Converts a multi - dimensional array into a one-dimensional(1D)
#   Array.
#   It always returns a copy of the original array.

# Syntax:-
# array.flatten()

# Example:
# import numpy as np

# arr = np.array([
#     [10,20,30],
#     [40,50,60]
# ])
# new_arr = arr.flatten()
# print(new_arr)
# print(arr)




# ravel()
# -> The ravel() function Converts a multi - dimensional array into a one-dimensional(1D)
#   Array.

# Unilike flatten(), it usually returns a view of the original array insted of a copy.
# if the returned array is modified ,the original array may be change.


# Syntax:
# array.ravel()

# Example:-
# import numpy as np

# arr = np.array([
#     [10,20,30],
#     [40,50,60]
# ])

# new_arr = arr.ravel()
# print(new_arr)
# print(arr.ravel())


# transpose()
# -> The transpose() function swaps rows and columns of an array.
# For Matrix:
# Rows become Columns
# Columns become Rows

# Syntax:
# array.transpose()


# Example:-
# import numpy as np

# arr = np.array([
#     [10,20,30],
#     [40,50,60]
# ])

# print(arr)
# print(arr.transpose())


# resize()
# -> The resize() function changes the size of an array.
# resize() can:
# Increase the number of elements.
# Decrease the number of elements.


# Syntax:
# np.resize(array,new_shape)

# import numpy as np
# arr = np.array([10,20,30,40])
# print(np.resize(arr,(2,2)))


# *** Increase the number of elements.
# Example:
# import numpy as np
# arr = np.array([1,2,3])
# print(np.resize(arr,(2,4)2))


# *** Decrease the number of elements.
# Example:
# import numpy as np
# arr = np.arange(1,10)
# print(np.resize(arr,(2,3)))


# concatenate()
# -> concatenate() joins two or more arrays into a single array.

# Syntax:
# np.concatenate((array1,array2,...),axis=0)

# axis=0 -> join by rows (Vertical)
# axis=1 -> join by columns(Horizontal)

# Example:
# import numpy as np
# arr1 = np.array([
#     [10,20],
#     [30,40]
# ])

# arr2 = np.array([
#     [50,60],
#     [70,80]
# ])

# print(np.concatenate((arr1,arr2),axis=0))


# Example:
# import numpy as np
# arr1 = np.array([
#     [10,20],
#     [30,40]
# ])

# arr2 = np.array([
#     [50,60],
#     [70,80]
# ])

# print(np.concatenate((arr1,arr2),axis=1))



# hstack()
# -> hstack() means Horizontal stack.
#  it joins array side by side(columns-wise).

# Syntax:
# np.hstack((arr1,arr2))

# Example:
# import numpy as np
# arr1 = np.array([10,20,30])
# arr2 = np.array([40,50,60])
# print(np.hstack((arr1,arr2)))


# vstack()
# -> vstack() means Vertical stack.
# it joins array one below another(row-wise).
# Syntax:
# np.vstack((arr1,arr2))

# Example:
# import numpy as np
# arr1 = np.array([10,20,30])
# arr2 = np.array([40,50,60])
# print(np.vstack((arr1,arr2)))


# split()
# -> split() divides an array into multiple smaller arrays.
# Syntax:
# np.split(array,number_of_parts)

# Example:
# import numpy as np
# arr = np.array([10,20,30,40,50,60])
# result = np.split(arr,3)
# print(result)




# *** Broadcasting
# ->Broadcasting is a feature in NumPy that allows arithmetic operations between arrays of different shapes without manually repeating data.
# Instead of creating a new array with repeated values, NumPy automatically expands the smaller array when possible.




# Scalar Broadcasting.
# - A scalar is a single values.
#  - when a scalar is used with an array,Numpy automatically applies the operation to every
#    elements.

# import numpy as np
# marks = np.array([10,20,30,40,50,60])
# print(marks+5)


# import numpy as np
# marks = np.array([10,20,30,40,50,60])
# print(marks*5)




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