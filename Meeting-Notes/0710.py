# Array Operations & Arithmetic Operations


# -  Array Operations & Arithmetic Operations
# - Array Operations are mathematical Operations performed directly on numpy Arrays.


# import numpy as np

# salary = np.array([25000,30000,35000])
# # print(salary)
# bonus_salary = salary + 5000
# print(bonus_salary)

# // Arithmetic Operations
# Operator:
# +,-,*,/,//,%,**


# 1: Addition
# +:
# Ex:
# import numpy as np
# arry1 = np.array([10,20,30])
# arry2 = np.array([1,2,3])
# result = arry1 + arry2
# print(result)



# 2: Substraction
# -:
# Ex:
# import numpy as np
# arry1 = np.array([10,20,30])
# arry2 = np.array([1,2,3])
# result = arry1 - arry2
# print(result)


# // Comparison Operators & Aggregate Functions

# - Comparison Operators are used to compare the elements of an array.

# Operator:
# >
# <
# >=
# <=
# ==
# !=

# import numpy as np

# marks = np.array([45,60,75,80,95])
# print(marks>70)



# import numpy as np

# marks = np.array([45,60,75,80,95])
# print(marks<70)



# import numpy as np

# marks = np.array([45,60,75,80,95,70])
# print(marks==70)



# import numpy as np

# marks = np.array([45,60,75,80,95,70])
# print(marks==70)



# // Aggregate Functions
# - Aggregate Functions calculate a single value from multiple array elements.
# - They help us analyze data quickly.
# Exa:
# Total marks
# Average salary
# Highest marks
# Lowest salary

# Aggregate Functions:
# sum()
# mean()
# median()
# std()
# var() 
# min()
# max()

# import numpy as np

# marks = np.array([45,60,75,80,95,70])
# # print(np.sum(marks))
# total = np.sum(marks)
# print(total)


# import numpy as np

# marks = np.array([45,60,75,80,95,70])
# m1 = np.mean(marks)
# print(m1)


# // Sorting ,Searching & Unique Values.

# - Sorting  Means arranging data in a specific order.
# 1: Ascending order
# 2: Descending order


# 1: Ascending order
# import numpy as np
# marks = np.array([45,60,75,80,95,70])
# print(np.sort(marks))

# 2: Descending order
# Syntax:
# np.sort(array_name)[::-1]


# Ex:
# import numpy as np
# marks = np.array([45,60,75,80,95,70])
# print(np.sort(marks)[::-1])


# // Searching Array.
# - Searching means finding the position or index of elements in an array.
# 1: np.where()
# 2: np.seatchsorted()


# 1: np.where()
# - Returns the index position where the given condition is True.

# Syntax:
# np.where(condition)


# import numpy as np
# marks = np.array([45,70,75,80,95,70])
# print(np.where(marks==70))

# import numpy as np
# marks = np.array([45,70,75,80,95,70])
# print(np.where(marks>50))