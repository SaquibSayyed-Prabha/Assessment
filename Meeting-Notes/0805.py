# *** Logistic Regression


# What is Classification?
# -Classification is a Machine Learning technique used to predict categories or labels instead of numbers.


# ***What is Logistic Regression?
#  -Logistic Regression is a Supervised Machine Learning algorithm used for Classification problems.
#  It predicts the probability of a category and then classifies the result into a class.



# ***Why is Logistic Regression Used?
# Logistic Regression is used because:
#  -It is simple and fast.
#  -It works well for binary classification.
#  -It predicts probabilities.
#  -It is easy to understand.



# Regression vs Classification

# Regression              Classification
# Predicts Numbers        Predicts Categories
# Example: Salary         Example: Pass/Fail
# Linear Regression       Logistic Regression




# Examples

# Regression
# Input
# Experience = 6 Years
# Output
# Salary = 52000


# Classification
# Input
# Study Hours = 6
# Output
# Pass



# *** Binary Classification
#  -Binary Classification means there are only two possible outputs.

# Examples
# Yes / No
# Pass / Fail
# True / False
# Spam / Not Spam
# Approved / Rejected



# *** Multi-Class Classification


# Multi-Class Classification means there are more than two classes.

# Example

# Cat
# Dog
# Horse

# or

# Grade A
# Grade B
# Grade C




# *** Import Required Libraries

# import pandas as pd
# from sklearn.linear_model import LogisticRegression


# Examples:

# import pandas as pd
# from sklearn.linear_model import LogisticRegression

# # Create Dataset
# # 0 = Fail
# # 1 = Pass

# data = {
#     "Study_Hours":[1,2,3,4,5,6,7,8,9],
#     "Result":[0,0,0,1,1,1,1,1,1]
# }

# df = pd.DataFrame(data)
# print(df)

# # Features
# X = df[["Study_Hours"]]

# # Target
# y = df["Result"]

# # Create Model

# model = LogisticRegression()

# # Train Model

# model.fit(X,y)

# # prediction

# pred = model.predict([[5]])

# print("Prediction:",pred[0])


# *** Model Score 
# syntax:
# score = model.score(X,y)

# Example:

# import pandas as pd
# from sklearn.linear_model import LogisticRegression

# # Create Dataset
# # 0 = Fail
# # 1 = Pass

# data = {
#     "Study_Hours":[1,2,3,4,5,6,7,8,9],
#     "Result":[0,0,0,1,1,1,1,1,1]
# }

# df = pd.DataFrame(data)
# print(df)

# # Features
# X = df[["Study_Hours"]]

# # Target
# y = df["Result"]

# # Create Model

# model = LogisticRegression()

# # Train Model

# model.fit(X,y)

# # prediction

# pred = model.predict([[5]])

# print("Prediction:",pred[0])

# # model score
# s1 = model.score(X,y)

# print("Model Score:",s1)

# Score
# 1.00  - Perfect Model
# 0.99  - Very Good Model
# 0.90 - Good Model
# 0.70 - Fair model(can be improved)
# 0.50 - Average Model
# 0.00 - Model Did not Learn Anything
# (-0.5) - Fail Model




# ** Predicts probability
# - predict_proba() returns the probability of each class.

# syntax:
# probability = model.predict_proba([[10]])


# Example:

# import pandas as pd
# from sklearn.linear_model import LogisticRegression

# # Create Dataset
# # 0 = Fail
# # 1 = Pass

# data = {
#     "Study_Hours":[1,2,3,4,5,6,7,8,9],
#     "Result":[0,0,0,1,1,1,1,1,1]
# }

# df = pd.DataFrame(data)
# print(df)

# # Features
# X = df[["Study_Hours"]]

# # Target
# y = df["Result"]

# # Create Model

# model = LogisticRegression()

# # Train Model

# model.fit(X,y)

# # prediction

# pred = model.predict([[5]])

# print("Prediction:",pred[0])

# # model score
# s1 = model.score(X,y)

# print("Model Score:",s1)

# # Probability

# print("Probability:",model.predict_proba([[5]]))


# Example: Predicts Multiple Students

# import pandas as pd
# from sklearn.linear_model import LogisticRegression

# # Create Dataset
# # 0 = Fail
# # 1 = Pass

# data = {
#     "Study_Hours":[1,2,3,4,5,6,7,8,9],
#     "Result":[0,0,0,1,1,1,1,1,1]
# }

# # Features
# X = df[["Study_Hours"]]

# # Target
# y = df["Result"]

# # Create Model

# model = LogisticRegression()

# # Train Model

# model.fit(X,y)

# # Multiple Students
# students = pd.DataFrame({
#     "Study_Hours":[1,5,4,9,2,12,0,100,43,56]
# })

# prediction = model.predict(students)
# probability = model.predict_proba(students)

# students["Prediction"] = prediction
# students["Fail_probability"] = probability[:,0]
# students["Pass_probability"] = probability[:,1]

# print(students)
# # model score
# s1 = model.score(X,y)
# print("Model Score:",s1)