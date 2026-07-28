# Tue-28/07/2026

# ***  Encoding (Converting Categorical Data into Numerical Data)


# 1. What is Categorical Data?
# Definition
# Categorical Data is data that contains text values, names, or categories instead of numbers.
# Machine Learning algorithms cannot understand text directly, so categorical data must be converted into numbers.


# Examples of Categorical Data

# *Gender
#  Male
#  Female
#  Male
#  Female


# *Common Categorical Columns
#  Gender
#  City
#  Department
#  Education
#  Product Category
#  Country
#  Color


# 2. What is Numerical Data?
# Definition
# Numerical Data consists of numbers that can be used directly in mathematical calculations.
# Machine Learning algorithms can process numerical data without any conversion.



# Examples
# Age Salary
# 22  25000
# 25  35000
# 30   55000

# These values are already numeric, so no encoding is needed.



# 3. Why Encoding is Required?
# Definition
# Encoding is the process of converting categorical (text) data into numerical values.
# Most Machine Learning algorithms only work with numbers.



# Example
# Original Dataset

# *Gender
#  Male
#  Female
#  Male

# -Machine Learning cannot understand:

# After Encoding
# Gender
# 1
# 0
# 1
# -Now the model can process the data.



# 4. Types of Encoding
# There are two common encoding techniques:
#  -Label Encoding
#  -One-Hot Encoding


# 5. Label Encoding
# Definition
# Label Encoding converts each unique category into a unique integer.


# Example

# Original Data
# Gender
#  -Male
#  -Female
#  -Male
#  -Female


# After Label Encoding
# Gender
# 1
# 0
# 1
# 0

# Example: - 
# import pandas as pd

# from sklearn.preprocessing import LabelEncoder

# data = {
#     "Gender":["Male","Female","Male","Female"]
# }

# df = pd.DataFrame(data)

# print(df)

# encoder =LabelEncoder()

# df["Gender"] = encoder.fit_transform(df["Gender"])
# print("After Label Encoding:")
# print(df)



# * Advantages of Label Encoding

# Easy to use.
# Fast.
# Requires only one column.
# Suitable for ordinal data.


# Disadvantages
# Machine Learning models may think:
# 0 < 1 < 2
# which may create a false relationship between categories.
# Example:
# Male = 1

# Female = 0
# The numbers do not mean that one category is greater than the other.


# 6. One-Hot Encoding
# Definition
# One-Hot Encoding creates a separate binary column for each category.

# Example
# Original Dataset
# City

# Pune
# Mumbai
# Delhi
# Pune

# After One-Hot Encoding

# Delhi, Mumbai, Pune 
#  0       0       1
#  0       1       0
#  1       0       0
#  0       0       1

#  -Each category gets its own column.


# Example:--
# ----------------------------
# import pandas as pd
# from sklearn.preprocessing import OneHotEncoder

# data = {
#     "City":["Pune","Mumbai","Delhi","Pune"]
# }
# df = pd.DataFrame(data)

# print(df)

# encoder = OneHotEncoder(sparse_output=False)

# encoded = encoder.fit_transform(df[["City"]])

# print("One-Hot-Encoding")
# # Delhi, Mumbai,Pune

# # "City":["Pune","Mumbai","Delhi","Pune"]

# print("Delhi","Mumbai","Pune")
# print(encoded)



# Example:

# import pandas as pd
# from sklearn.preprocessing import OneHotEncoder

# data = {
#     "City":["Pune","Mumbai","Delhi","Pune"]
# }
# df = pd.DataFrame(data)

# # print(df)

# encoder = OneHotEncoder(sparse_output=False)

# encoded = encoder.fit_transform(df[["City"]])

# print("One-Hot-Encoding")
# # print(encoded)
# encoded_df = pd.DataFrame(encoded,columns=encoder.get_feature_names_out())
# print(encoded_df)



# Complete Example : ------
# -------------------------------------

# import pandas as pd
# from sklearn.preprocessing import LabelEncoder

# data = {
#     "Gender":["Male","Female","Male"],
#     "City":["Pune","Mumbai","Delhi"]
# }

# df = pd.DataFrame(data)

# # print(df)

# # label Encoding

# label = LabelEncoder()

# df["Gender"] = label.fit_transform(df["Gender"])


# # One-Hot Encodig in pandas


# city = pd.get_dummies(df["City"],prefix="City",dtype=int)

# df = pd.concat([df.drop("City",axis=1),city],axis=1)
# print(df)