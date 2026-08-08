# *** Introduction to Feature Scaling 

# *** What is Feature Scaling?
# -Feature Scaling is the process of converting numerical features into a similar range.
# -Instead of changing the meaning of the data, it only changes the scale.


# Age = 20 to 60
# Salary = 20000 to 100000


# Example:
# age = 25 years,
# Salary = 30000

# Scaling:
# age=0.25
# Salary=0.30

# *** Problems Without Feature Scaling


# Problem 1 – Large Values Dominate
# Example:
# Feature    Value
# Age        25
# Salary      60000

# Salary has much larger numbers than Age.
# Many algorithms will give more importance to Salary.



# Problem 2 – Slower Model Training
# Unscaled data can cause algorithms such as Gradient Descent to take longer to find the best solution.
# Result:
# More iterations
# Longer training time


# Problem 3 – Lower Prediction Accuracy
# Because one feature dominates the others, the model may not learn correctly.
# This can reduce prediction accuracy.




# ***When is Feature Scaling Required?
# -Feature Scaling is required when numerical features have very different ranges.

# Algorithms That Usually Require Feature Scaling
#  -K-Nearest Neighbors (KNN)
#  -K-Means Clustering
#  -Support Vector Machine (SVM)
#  -Logistic Regression
#  -Linear Regression (especially with Gradient Descent)
#  -Neural Networks
#  -Principal Component Analysis (PCA)



# *** StandardScaler


# 1. What is StandardScaler?
# Definition
#  -StandardScaler is a preprocessing technique that converts numerical features into a standardized scale.

# After applying StandardScaler:
#  Mean becomes 0
#  Standard Deviation becomes 1
# -This process is called Standardization or Z-score Normalization.


# Import
# from sklearn.preprocessing import StandardScaler



# Formula of StandardScaler
# The mathematical formula is:

# Standardized Value = (X − Mean) / Standard Deviation
# or
# Z = (X − μ) / σ

# Where:
# Symbol     Meaning
# X          Original Value
# μ          Mean
# σ          Standard Deviation




# Example
# Age values:
# 20
# 25
# 30
# 35


# Mean:
# 27.5
# Standard Deviation:
# 5.59
# For Age = 20
# (20 − 27.5) / 5.59

# = -1.34
# The same calculation is applied to every value.


# Example:1

# import pandas as pd
# from sklearn.preprocessing import StandardScaler

# data = {
#     "Age":[22,25,30,35]
# }

# df = pd.DataFrame(data)
# print(df)
# scaler = StandardScaler()
# scaled = scaler.fit_transform(df)
# print("Scaled Age Column")
# print(scaled)



# Example:2
# import pandas as pd
# from sklearn.preprocessing import StandardScaler

# data = {
#     "Age":[22,25,30,35],
#     "Salary":[25000,35000,55000,80000]
# }

# df = pd.DataFrame(data)
# print(df)
# scaler = StandardScaler()
# scaled = scaler.fit_transform(df)
# print("Scaled Age Column")
# print(scaled)



# Example:3
# import pandas as pd
# from sklearn.preprocessing import StandardScaler

# data = {
#     "Age":[22,25,30,35],
#     "Salary":[54000,333000,54343,54544]
# }

# df = pd.DataFrame(data)
# print(df)

# # Scaled value
# scaler = StandardScaler()

# scaled = scaler.fit_transform(df)
# print("Scaled Values")
# print(scaled)


# * Convert Scaled Data Back to DataFrame
# Example:--
# import pandas as pd
# from sklearn.preprocessing import StandardScaler

# data = {
#     "Age":[22,25,30,35],
#     "Salary":[25000,35000,55000,80000]
# }

# df = pd.DataFrame(data)
# scaler = StandardScaler()
# scaled = scaler.fit_transform(df)

# scaled_df = pd.DataFrame(scaled,columns=df.columns)
# print(scaled_df)


# Example:
# import pandas as pd
# from sklearn.preprocessing import StandardScaler

# data = {
#     "Age":[22,25,30,35],
#     "Salary":[54000,333000,54343,54544]
# }

# df = pd.DataFrame(data)
# print(df)

# # Scaled value
# scaler = StandardScaler()

# scaled = scaler.fit_transform(df)
# print("Scaled Values")
# print(scaled)

# scaled_df = pd.DataFrame(scaled,columns=df.columns)

# print(scaled_df)



# *Advantages of StandardScaler
#  Improves model performance.
#  Speeds up convergence for many algorithms.
#  Removes scale differences between features.
#  Works well with normally distributed data.
#  Commonly used in Machine Learning pipelines.



# When to Use StandardScaler:
# - Logistic Regression
# - SVM
# - KNN
# - PCA
# - Neural Networks
# ** MinMaxScaler

# 1. What is MinMaxScaler?
# MinMaxScaler is a feature scaling technique that transforms numerical values into a fixed range.
# By default, it scales every value between:
# 0 and 1
# The smallest value becomes 0, and the largest value becomes 1.
# All other values are scaled proportionally between 0 and 1.



# Import
# from sklearn.preprocessing import MinMaxScaler



# Example 
# Before Scaling
# Age
# 20
# 25
# 30
# 35

# Range:
# 20 → 35



# After MinMaxScaler
# Age
# 0.00
# 0.33
# 0.67
# 1.00

# Now every value lies between 0 and 1.




# Formula of MinMaxScaler
# The mathematical formula is:
# Scaled Value = (X − Minimum) / (Maximum − Minimum)

# Where:
# Symbol           Meaning
#  X               Original Value
# Minimum         Smallest value in the column
# Maximum         Largest value in the column



# Example Calculation
# Age values:
# 20
# 25
# 30
# 35
# Minimum
# 20
# Maximum
# 35

# For Age = 25
# (25 − 20) / (35 − 20)

# = 5 / 15

# = 0.33



# Scaling Between 0 and 1
# After MinMaxScaler:
# Minimum Value → 0
# Maximum Value → 1
# Remaining values → Between 0 and 1



# Example:1
# import pandas as pd
# from sklearn.preprocessing import MinMaxScaler

# data = {
#     "Age":[22,25,10,35]
# }

# df = pd.DataFrame(data)
# scaler = MinMaxScaler()
# scaled = scaler.fit_transform(df)

# print(scaled)


# Example 2
# import pandas as pd
# from sklearn.preprocessing import MinMaxScaler

# data = {
#     "Age":[22,25,10,35],
#     "Salary":[24000,50000,30000,135000]
# }

# df = pd.DataFrame(data)
# scaler = MinMaxScaler()
# scaled = scaler.fit_transform(df)

# print(scaled)




# * Convert Scaled Data Back to DataFrame

# import pandas as pd
# from sklearn.preprocessing import MinMaxScaler

# data = {
#     "Age":[22,25,10,35],
#     "Salary":[24000,50000,30000,135000]
# }

# df = pd.DataFrame(data)
# scaler = MinMaxScaler()
# scaled = scaler.fit_transform(df)

# # print(scaled)
# scaled_df = pd.DataFrame(scaled,columns=df.columns)

# print(scaled_df)import pandas as pd
# from sklearn.preprocessing import MinMaxScaler

# data = {
#     "Age":[22,25,10,35],
#     "Salary":[24000,50000,30000,135000]
# }

# df = pd.DataFrame(data)
# scaler = MinMaxScaler()
# scaled = scaler.fit_transform(df)

# # print(scaled)
# scaled_df = pd.DataFrame(scaled,columns=df.columns)

# print(scaled_df)


# // When to Use MinMaxScaler
# - You want values between 0 and 1.
# - Features have different ranges.
# - image pixel values need scaling.