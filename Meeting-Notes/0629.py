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

# Example:-

# Suppose:
# Age increases
# Salary also increases

# Then:
#  Positive Correlation

# Correlation values:

# value          Meaning:
#   1            Strong Positive
#   0            No Relation
#  -1            Strong Negative