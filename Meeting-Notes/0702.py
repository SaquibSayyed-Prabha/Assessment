# ******************  NumPy **********************
# - NumPy stands for Numerical Python.
# - It is a Python library used for working with arrays,mathematical calculations,data analysis,Ai,Ml.

# * Advantages of NumPy:
# - Fast
# - Less Memory
# - Multi-dimensional arrays
# - mathematical Operations
# - Statistical Functions
# - Easy Data Manipulation


# - Installing NumPy
# 1: Open Command Prompt
#    pip install numpy  or py -m pip install numpy

# 2: Upgrade NumPy
#    pip install --upgrade numpy

# 3: Check Installation
#    pip show numpy

# 4: jupyter notebook


# - Arrays in numpy:
# - In NumPy array() Function is powerful method for creating arrays from Python data Structures.


# array Types:
# 1: 1 D array
# 2: 2 D array
# 3: 3 D array


# 1: 1 D array:
# - A one-dimensional array contains only one row of data.

# Example:

# import numpy as np

# # arr = np.array([5,10,15,20])

# # print(arr)

# # arr2 = np.array(["Sumit","Ram","Krushna"])
# # print(arr2)


# 2: 2 D array:
# - A two-dimensional array contains rows and columns.

# Example:

# import numpy as np

# marks = np.array([
#     [80,90,20],
#     [60,75,85],
#     [90,95,99]
# ])

# print(marks)


# 3: 3 D array:
# - A 3 dimensional array contains multiple 2D array.

# Example:

# import numpy as np

# arr = np.array([
#     [
#         [1,2],
#         [3,4]
#     ],
#     [
#         [5,6],
#         [7,8]
#     ],
#     [
#         [9,10],
#         [11,12]
#     ]
# ])

# print(arr)


# - Array  Attributes.
# - NumPy provides useful information about arrays.

# 1: ndim
# - Returns the number of dimensions.

# 2: shape
# - Returns rows and columns

# 3. size
# - Returns total number of elements.

# 4. dtype:
# - Returns data Type of array


# ---------------- creating arrays using zeros()

# zeros()
# - create an array filled with zeros.

# Syntax:
# np.zeros(shape)


# ones()
# - Create an array filled with ones.

# full()
# - Create an aaray filled with a specific values.
# Syntax:
# np.full(shape,value)


# - creating Arrays using eye()


# - creating Arrays using arange()
# - Works like Python range() but returns a NumPy aaray.

# Syntax:
# np.arange(start,stop,step)


# linspace()
# - Create evenly spaced numbers between two values.
# Syntax:
# np.linspace(start,stop,number_of_values)

# Example:

# a1 = np.linspace(1,10,5)
# print(a1)

# import numpy as np

# arr = np.array([5,10,15,20])
# # print(arr)

# arr2 = np.array(["Sumit","Ram","Krushna"])
# # print(arr2.dtype)

# # ndim-
# # print(arr.ndim)

# # print(arr.size)
# # a1 = np.arange(1,11)

# a1 = np.linspace(1,10,5)
# print(a1)


# import numpy as np

# arr3 = np.array([
#     [
#         [1,2],
#         [3,4]
#     ],
#     [
#         [5,6],
#         [7,8]
#     ],
#     [
#         [9,10],
#         [11,12]
#     ]
# ])

# print(arr3.size)
# print(arr3.dtype)

