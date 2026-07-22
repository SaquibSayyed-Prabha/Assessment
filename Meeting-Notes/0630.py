# 3. Correlation
# Def - Correlation tells us how Strongly two columns are related.

# Correlation values are always between -1 and +1

# Correlation value                    Meaning
# +1                                 Perfect Positive Relationship
# 0                                  No Relationship
# -1                                 Rerfect Negative Relationship



# Positive Correlation
#  - When one value increases ,another also increases

# Example:
# Study Hourse        Marks
#   2                 40
#   3                 50
#   4                 60


# More study -> More Marks
# Correlation = +1


# Negative Correlation
#  - When one value increases,another descreases

# Example:
# Exercise              weight
#  1hr                   80
#  2hr                   77
#  3hr                   74

# More Exercise -> Less weight
# Correlation = -1


# No Correlation
# Example:
# shoe size    Salary
#  7            30000
#  9            40000
#  10            20000

# Correlation = 0

# - Why is Correlation important
# - Suppose your dataset contains:
# Age,Salary,Experience and Purchased

# if Salary and Experience are highly related (0.95)
# then both columns contains almost the same Information,then sometimes we
# remove one column,this is called Feature Selection.

# Example:
# import pandas as pd

# data = {
#   "Age":[20,25,30,35,40],
#    "Salary":[20000,25000,30000,35000,40000],
#    "Experience":[1,2,3,4,5]
# }

# df = pd.DataFrame(data)

# # print(df)
# print(df.corr(numeric_only=True))


# *********** Handling Categorical Data *******************
# - Machine Leaning cannot understand text
# - it only understands Numbers. Therefore we must convert text into Numbers.
# - its called Handling Categorical data.

# Example:
# Dataset

# Name       Gender     City
# Rahul      Male        Pune
# Priya      Female      Mumbai
# Amit       Male        Delhi

# Data types:

# 1: Numericl Data
# Age
# Salary
# Height
# Marks
# Weight


# 2:Categorical Data
# Male
# Female
# Pune
# Delhi
# Red
# Blue


# Why convert ?

# Machine Leaning  understands only
# 0,1,2,3,4...

# Not a Male,Female 
# so we encode them


# -------- Encoding Basics ---------------
#  - Encoding means converting text into Numbers.
#  - There are many methods:

#    Most Common methods:
#      1: lable Encoding
#      2: One Hot Encoding


# Method 1: lable Encoding
# - Each Category was given a Number.

# Example:
# Original Data:
# Gender-
# Male
# Female
# Male


# After Encoding:
# Gender-
# 1
# 0
# 1

# Here:
# Male -> 1
# Female -> 0


# import pandas as pd
# from sklearn.preprocessing import LabelEncoder

# data = {
#   "Age":[20,25,30,35,40],
#     "Gender":['Male','Female','Male','Male','Female'],
#    "Salary":[20000,25000,30000,35000,40000],
#    "Experience":[1,2,3,4,5]
# }

# df = pd.DataFrame(data)

# le = LabelEncoder()

# df["Gender"] = le.fit_transform(df["Gender"])

# print(df)
# # print(df.corr(numeric_only=True))


# - Problem with lable Encoding
# Suppose:
# Red =0
# Blue=1
# Green=2

# Machine Thinks : 
# Green > Blue > Red

# Actually Colors have no order
#  - this is incorrect.

# import pandas as pd
# from sklearn.preprocessing import LabelEncoder

# data = {
#   "Age":[20,25,30,35,40],
#     "Gender":['Male','Female','Male','Male','Female'],
#    "Salary":[20000,25000,30000,35000,40000],
#    "Experience":[1,2,3,4,5]
# }

# df = pd.DataFrame(data)

# le = LabelEncoder()

# df["Gender"] = le.fit_transform(df["Gender"])

# print(df)
# # print(df.corr(numeric_only=True))