# -- Array Indexing --
# -> Indexing is used to access a specific element from a Numpy array,Every element in a numpy array has its own position,called an index.

# - Positive Indexing
# - Positive Indexing starts from the left side of the array.
#  - The first element always starts with index 0.

# - Negative Indexing
# - Negative Indexing starts from the right side of the array.
# - The last element always has index -1.




# **************** 2 D array Indexing ******************
# - A 2d array has rows and columns.
# to access an element we need :
#       row index
#       column index

# Syntax:

# array[row,column]


# **************** 3 D array Indexing ******************
# - A 3D array contains multiple 2D array.

# Syntax:
# array[array_index,row,column]


# ********** Array Slicing **************
# - Array Slicing is used to access multiple elements from a numpy array at the same time.
# Syntax:
# array[start:stop:step]



# ************ Fancy Indexing & Boolean Indexing
# - Fancy Indexing allows us to access multiple elements of an array at once by passing a list of 
#   array of index position:

#   Syntax:
#   array[index1,index2,index3]

 
#  - Boolean Indexing
#  - Boolean Indexing is used to filter array elements based on a condition.
#    : True
#    : False

# Syntax:
# array[condition]

# import numpy as np

# n1 = np.array([10,20,30,40,50])
# # print(n1)

# # print(n1[0])
# # print(n1[1])

# # print(n1[-1])
# # print(n1[-2])


# import numpy as np

# marks = np.array([
        
#     [10,20,30],
#     [40,50,60],
#     [70,80,90]
# ])

# # print(marks)
# # print(marks[0,0])
# # print(marks[1,2])
# # print(marks[2,1])
# # print(marks[-1,-1])

# import numpy as np

# arr = np.array([
#     [
#         [1,2],
#         [3,4]
#     ],
#     [
#         [5,6],
#         [7,8]
#     ]
# ])

# # print(arr)
# # print(arr[0,0,0])
# # print(arr[0,1,1])
# # print(arr[1,1,0])
# # print(arr[-1,-2,-2])

# import numpy as np

# n1 = np.array([10,20,30,40,50])

# # Slicing
# # print(n1[1:4])
# # print(n1[:3])
# # print(n1[2:])
# # print(n1[:])
# # print(n1[1:6:2])
# # print(n1[:-1])

# # Fancy indexing  1D array
# # print(n1[[1,3,4]])
# # print(n1[[0,3,2,0]])

# # Boolean index
# print(n1>30)
# print(n1<20)


# import numpy as np

# marks = np.array([
        
#     [10,20,30],
#     [40,50,60],
#     [70,85,90],
#     [100,110,120]
# ])

# # print(marks[0
# # print(marks[1])
# # print(marks[0:2])
# # print(marks[1:])


# # Fancy indexing  2D array
# # print(marks[[0,2]])
# # print(marks[[3,0,2]])
# # print(marks[[0,2],[1,2]])

# # Boolean index
# # print(marks[marks>70])
# # print(marks>70)
# # print(marks[(marks>=70) & (marks<=90)])


