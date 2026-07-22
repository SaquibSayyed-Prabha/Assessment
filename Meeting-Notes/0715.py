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



# *** Filtering Arrays
#  - Filtering means selecting only those elements that satisfy a given condition.

#  syntax:
#  array[condition]

# Example:
# # Display values greater than 50

# import numpy as np

# numbers = np.array([10,40,60,80,25,95])

# print(numbers[numbers > 50])


# Example:
# # Display even numbers

# import numpy as np

# numbers = np.array([10,40,60,80,25,95])

# print(numbers[numbers %2==0])


# *** Conditional Selection
#  - Conditional Selection allows us to select data based on one more condition.

# Example:
# marks greater than or equal to 75.
# import numpy as np

# numbers = np.array([10,40,60,80,25,95])
# print(numbers[numbers >=75])


# Example:
# Display numbers less than 30.
# import numpy as np

# numbers = np.array([10,40,60,80,25,95])
# print(numbers[numbers <30])


# - Boolean Masking
#  -  A Boolean mask is an array of True and False values used to filter data.

#  Example:
#  import numpy as np
# marks = np.array([55,72,81,68,95])

# mask = marks >=75
# print(mask)

# print(marks[mask])


# - Multiple Conditions
#   Use & (AND) and | (OR).

#   Example:

#   # find marks between 70 and 90.
# import numpy as np
# marks = np.array([65,72,81,95,68,88,99])
# print(marks[(marks>=70) & (marks<=90)])



# ***  Statistical Analysis ,Feature matrix(x),Target Variable(y)


# Statistical Analysis
# - Statistical Analysis means finding useful information from data using mathematical calculations.
# It helps us understand:
# Average values
# Highest value
# Lowest value


# Example:
# import numpy as np
# salary = np.array([25000,30000,35000,40000,45000])
# # print(Salary)

# print("Find Total Salary:")
# total=np.sum(salary)
# print(total)

# print("Find Average Salary:")
# print(np.mean(salary))

# print("Find Maximum Salary:")
# print(np.max(salary))

# print("Find Manimum Salary:")
# print(np.min(salary))

# print("Find Standard Deviation:")
# print(np.std(salary))

# print("Find Variance:")
# print(np.var(salary))



# - Feature Matrix:
#  - Feature means input data
#  - Maching learning always learns from Features.
#  - Features are stored inside X.

# Example:

# Study Hourse       Attendance             marks
#  2                  90                    35
#  5                  95                    70
#  8                  98                    95

# Study Hourse,Attendance  = are Features
# marks = is Target


# Example:

# - Features Selection.

# import numpy as np

# data = np.array([
#     [2,90,35],
#     [5,95,70],
#     [8,98,95]
# ])

# X = data[:,0:2]
# print(X)




#  - Target Variable(y)
#  - Target means output
#  - It is what we want to predict.
#  - Target is stored inside y. 

#  import numpy as np

# data = np.array([
#     [2,90,35],
#     [5,95,70],
#     [8,98,95]
# ])

# y = data[:,2]
# print(y)


