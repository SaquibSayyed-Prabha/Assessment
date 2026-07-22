# ****** Data Preparation ******

# Process:-

# Dataset
#    |
# Data Cleaning
#    |
# Data Exploration
#    |
# Feature Selection



# // Sample Dataset


# 1. Data Exploration
# Def - Data Exploration means understanding the dataset before building a model.

# - Common Exploration Functions

# - View First Rows
# df.head()

# - View Last Rows
# df.tail()

# - Dataset Shape
# df.shape
# - Output 
#    (5,4)

# - Dataset Information
# df.info()

# - Statistical Summary
# df.describe()


# - Why Data Exploration?
# - Data understanding
# - Data quality
# - Missing values
# - Useful columns


# 2. Feature Selection
# Def - A Feature is simply a column used to Train a Machine Leaning Model.

# Example Dataset:

# Age   Salary   Gender Purchase
# Here:
# Age
# Salary
# Gender
# are Features.
# Purchased
# is the Target column.

# What is Target?
# -> Target is the value we want to predict.

# Example:
# Will Customer purchase?

# Target:
# Purchased

# // Selcting Features
# x = df[["Age","Salary"]]
# print(x)

# // Selecting Target
# x = df["Purchased"]
# print(x)

# // Why Feature Selection
# - Not every column is useful.

# Example:
# Name,Mobile Number,Salary,Ex,skill

# For Salary Prediction:
# Mobile Number is not useful.

# Therefore we select only important Features.




# 3. Correlation
# Def - Correlation tells us how Strongly two columns are related.

# Correlation values are always between -1 and +1

# Correlation value                    Meaning
# +1                                 Perfect Positive Relationship
# 0                                  No Relationship
# -1                                 Rerfect Negative Relationship



# 1: Positive Correlation
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

# Name       Gender     City     Age   Marks
# Rahul      Male        Pune    21    60
# Priya      Female      Mumbai  22    65
# Amit       Male        Delhi   21    90

# Data types:

# 1: Numericl Data
# Age
# Marks

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

# Therefore we use One hot Encoding:

# Method 2: One Hot Encoding
# - A new column  created for each category in a column.

# Example:
# Gender:-
# Male
# Female
# Male

# After Encoding:
# name           Male     Female
# Rahul           1        0
# Siya             0        1
# Sumit            1        0


# Example:

# import pandas as pd

# data = {
#     "Gender":["Male","Female","Male","Female"]
# }

# df = pd.DataFrame(data)

# # encoded = pd.get_dummies(df["Gender"])

# encoded = pd.get_dummies(df["Gender"],dtype=int)

# print(encoded)


# **************** Train/Test Dataset Concept *******************
# - We never Train a Machine Leaning model on the entire dataset.
# - We divide the dataset into:
#              1: Training Data
#                 - Used to teach the model
#              2: Testing Data
#                 - Used to evalute the model.

# Real Life Example:
# Suppose:
# 1000 Records

# Split:
# 80%  Training

# 20%  Testing


#                  Complete Dataset
#                          |
#                          |
#              --------------------------------------
#             |                                       |
#    Training Data                                     Testing Data


# Example:


# import pandas as pd
# from sklearn.model_selection import train_test_split

# data = {
#      "Age":[20,25,30,35,40],
#      "Salary":[20000,25000,30000,35000,40000],
#      "Gender":["Male","Female","Male","Female","Male"],
#      "Purchased":[0,1,2,1,0]
# }

# df = pd.DataFrame(data)

# x = df[["Age","Salary"]]
# y = df["Purchased"]

# x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

# print(x_train)
# print(x_test)