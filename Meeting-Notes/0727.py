# import pandas as pd
# from sklearn.model_selection import train_test_split

# # Read Dataset
# df = pd.read_csv("employees.csv")
# # print(df)

# # Features
# X = df[["Age","Experience"]]

# # Target
# y = df["Salary"]

# # Train-Test split
# X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# print(X_train)
# print(X_train.shape)
# print("______________________________")
# print(X_test)
# print("______________________________")
# print(y_train)
# print("______________________________")
# print(y_test)


# The .shape attribute tells us the number of rows and columns.




# *** Handling Missing Values & Encoding.


# * Missing Values
# - A Missing Values is a Value that is not available or not recorded in a Dataset.
# In pandas , Missing Values are usually represented as:
# - NaN (Not a number)
# - None.


# Example:

# Name   Age    Salary
# Amit   20     30000
# Rahul  NaN     34000
# Sneha  25     NaN



# ** Types of Missing Values.

# 1: Numerical Missing Values.
# - Missing Values in Numerical columns.

# Example:
# Age     Salary
# 23       30000
# NaN      45000
# 30       NaN


# 2. Categorical Missing Values
# - Missing Values in text columns.

# Example:

# City:
# Pune
# NaN
# Delhi
# Mumbai
# NaN



# ** Finding Missing Values.

# - isnull()

# Syntax:
# df.isnull()

# Example:
# import pandas as pd
# import numpy as np

# data = {
#     "Age":[25,np.nan,30],
#     "Salary":[30000,45000,np.nan]
# }

# df = pd.DataFrame(data)
# print(df)
# print(df.isnull())


# Example:
# import pandas as pd
# import numpy as np

# data = {
#     "Age":[25,np.nan,30],
#     "Salary":[30000,45000,np.nan]
# }

# df = pd.DataFrame(data)
# # print(df)
# print("____________________________________________")
# # print(df.isnull())
# # print(df.fillna(1))
# # Replace missing Age using mean.
# a_age=df["Age"].mean()
# df["Age"] = df["Age"].fillna(a_age)

# # Replace missing Salary using Median
# df["Salary"] = df["Salary"].fillna(df["Salary"].median())
# print(df)




# ** SimpleImputer
# - SimpleImputer is a Scikit-Learn class used to automatically Replace missing Values.
# - It is comonly used in Maching Learning Preprocessing pipelines.


# Example:

# // Mean Strategy

# from sklearn.impute import SimpleImputer
# import pandas as pd
# import numpy as np

# data = {
#    "Age":[20,25,np.nan,35]
# }

# df = pd.DataFrame(data)

# print(df)
# print("____________________")
# imputer = SimpleImputer(strategy="mean")

# df["Age"] = imputer.fit_transform(df[["Age"]])
# print(df)




# ** available strategys

# Strategy           Purpose

# "mean"       - Replace using mean
# "median"   - Replace using median
# "most_frequent" - Replace using Mode
# "constant"  - Replace using a fixed Value