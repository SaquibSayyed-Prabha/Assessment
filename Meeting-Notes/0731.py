# *** Feature Engineering & Feature Selection


# Introduction to Feature Engineering

# * What is Feature Engineering?
#  Feature Engineering is the process of creating, modifying, or transforming existing data into more useful features that help,
#  a Machine Learning model make better predictions.
#  A feature is simply a column (input variable) in a dataset.
#  Feature Engineering improves the quality of the dataset before training a Machine Learning model.


# Example:

# Original Dataset
# Age      Experience
# 22        1
# 25        3
# 30        6
# 35       10


# After Feature Engineering

# Age     Experience    Experience Level
# 22        1             Beginner
# 25        3             Intermediate
# 30        6             Experienced
# 35        10            Expert


# The new column Experience Level is created from the Experience column.
# This new feature may help a Machine Learning model better understand employee experience.



# * Why is Feature Engineering Important?
#    Raw data is often not suitable for Machine Learning.
#    Feature Engineering helps by:
#    Creating meaningful features.
#    Improving prediction accuracy.
#    Making patterns easier for the model to learn.
#    Reducing unnecessary complexity.
#    Increasing model perform



# ** Types of Feature Engineering
# -There are many Feature Engineering techniques.

# The most common are:

# *Type 1 – Creating New Features

# Example:
#  Python  Java       #C   
#  80       70        90
#  75       85        80

# Create:

# Total Marks
# 240
# 240

# Example:

# import pandas as pd

# data = {
#     "Java":[80,75],
#     "Python":[70,77],
#     "Html":[60,69]
# }

# df = pd.DataFrame(data)

# df["Total_Marks"] = df["Java"] + df["Python"] + df["Html"]
# print(df)  





# *Type 2 – Transform Existing Features

# -Modify existing values.

# Example:
# Convert salary from dollars to thousands.
# Salary
# 50000
# 60000

# New Column:
# Salary (Thousands)
# 50
# 60

# Example:

# import pandas as pd

# data = {
#     "Salary":[50000,60000]
# }

# df = pd.DataFrame(data)

# df["Salary_Thousands"] = df["Salary"]/1000
# print(df)



# *Type 3 – Combining Features
# -Combine multiple columns into one.

# Example:

# City    State
# Pune    Maharashtra
# Mumbai  Maharashtra

# Create:
# Address
# Pune, Maharashtra
# Mumbai, Maharashtra


# Example:

# import pandas as pd

# data = {
#     "City":["Pune","Mumbai"],
#     "State":["Maharashtra","Maharashtra"]
# }

# df = pd.DataFrame(data)
# # print(df)

# df["Address"] = df["City"] + ", " + df["State"]

# print(df)


# *Type 4 – Splitting Features
# -Split one column into multiple columns.

# Example:

# Full_Name
#  Ajay bhosale


# Split into:

# First Name    Last Name
#  Ajay          bhosale


# Example:

# import pandas as pd

# data = {
#     "Full_Name":["Ajay Patil","Ganesh Shah"]
# }

# df = pd.DataFrame(data)
# df[["First_name","Last_name"]] = df["Full_Name"].str.split(" ",expand=True)

# print(df)




# *** Feature Selection


# What is Feature Selection?
# Feature Selection is the process of selecting only the important features (columns) from a dataset that are useful for training a,
# Machine Learning model.
# Instead of using every column, we choose only those that help improve the model's performance.


# Example
# Original Dataset


# Employee ID     Name      Age       Experience        Salary
# 101             Amit       25         2                30000
# 102             Rahul      30         5                50000
# 103             Sneha      28         4                 45000

# -dataset contains 5 columns.


# Selected Features
# Age   Experience
# 25      2
# 30      5
# 28      4

# Suppose we want to predict Salary.

# Useful features:
# Age
# Experience

# Target:
# Salary

# Unnecessary columns:
# Employee ID
# Name


# *Why is Feature Selection Important?
#  Using too many unnecessary columns can make the Machine Learning model:
#   -Slower
#   -More complex
#   -Less accurate
# -Feature Selection helps by keeping only useful information.


# Advantages
#   -Improves model accuracy.
#   -Reduces training time.
#   -Makes the model simpler.
#   -Reduces memory usage.
#   -Removes irrelevant information.
#   -Helps prevent overfitting.


# *Selecting Important  Features (Columns)
# We can select only the required columns using Pandas.

# Example:

# import pandas as pd

# data = {
#     "Name":["Sham","Ran","Om","Priya"],
#     "Age":[22,24,30,35],
#     "Ex":[1,3,6,10],
#     "Salary":[25000,35000,55000,80000]
# }

# df = pd.DataFrame(data)

# # print(df)

# X = df[["Age","Ex"]]

# print(X)




# *** Correlation-Based Feature Selection

# ** What is Correlation?
# -Correlation measures the relationship between two numerical variables.
# -It tells us how strongly two columns are related.

# For example:
# If one feature increases and another also increases, they have Positive Correlation.
# If one feature increases and another decreases, they have Negative Correlation.
# If there is no relationship, they have No Correlation.

# -Correlation helps us decide which features are useful for a Machine Learning model.


# -Correlation Value Range

# Correlation values always lie between:
# -1  to  +1


# Correlation Value   Meaning
# +1                   Perfect Positive Correlation
# 0                    No Correlation
# -1                   Perfect Negative Correlation


# *** Positive Correlation
# -When one variable increases and the other variable also increases, it is called Positive Correlation.

# Example
# Experience (Years)   Salary
# 1                     25000
# 3                     35000
# 5                     50000
# 8                     70000



# This is Positive Correlation.




# *** Negative Correlation
# -When one variable increases and the other variable decreases, it is called Negative Correlation.


# Example
# Study Hours      Mobile Usage (Hours)
# 2                8
# 4                6
# 6                4
# 8                2


# -This is Negative Correlation.



# *** No Correlation
# -When two variables have no clear relationship, they have No Correlation.



# Example
# Shoes Size Exam Marks
# 7         80
# 8         65
# 9         90
# 10        72

# - There is no meaningful relationship between shoes size and exam marks.