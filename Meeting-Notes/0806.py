# *** K-Nearest Neighbors (KNN)

#  -KNN is one of the simplest Machine Learning algorithms. It predicts the output by looking at the nearest data points.
#  -It is mainly used for Classification, but it can also be used for Regression.


# ***Why is KNN Used?
#  -KNN is used because it is:
#  -Easy to understand
#  -Easy to implement
#  -Good for small datasets
#  -Works well for classification problems

# ***Real-World Applications
#  -Fruit Classification
#  -Handwritten Digit Recognition
#  -Face Recognition
#  -Medical Disease Prediction
#  -Customer Classification
#  -Product Recommendation
#  -Loan Approval



# ***What Does "K" Mean?
# -K represents the number of nearest neighbors the algorithm considers before making a prediction.

# Example:
# K = 3
# The algorithm checks the 3 nearest data points.

# K = 5
# The algorithm checks the 5 nearest data points.


# ***How KNN Works
# Load Dataset
#       ↓
# Create Features (X)
#       ↓
# Create Target (y)
#       ↓
# Choose K Value
#       ↓
# Train Model
#       ↓
# Find Nearest Neighbors
#       ↓
# Predict Output



# ***Choosing the K Value
# *Choosing the correct K is important.

# K Value                Result
# Small K (1,3)        Can overfit the data
# Medium K (5,7)       Usually gives good results
# Large K              May underfit the data


# K = 3 or K = 5 is a good choice.


# Example:


# Rahul new Employee
#  Developer or Desiner

# Developer
# Developer
# Rahul
# Developer
# Desiner




# k=3
# Developer=2
# Desiner=1

# Rahul is Developer




# Example:

# Age      Purchased
# 18        No
# 20        No
# 22        No
# 24        Yes
# 25        -
# 26        Yes
# 28        Yes
# 30        Yes


# New Customer
# Age  =25

# K=3

# 22 = No
# 24 = Yes
# 26 = Yes

# Yes = 2
# No = 1

# Age 25 Customer Yes.



# ***Import Required Libraries

# import pandas as pd
# from sklearn.neighbors import KNeighborsClassifier


# Example:

# import pandas as pd
# from sklearn.neighbors import KNeighborsClassifier


# # Create Dataset
# # No=0
# # Yes=1
# data = {
#     "Age":[18,20,22,24,26,28,30,32,34],
#     "Purchased":[0,0,0,1,1,1,1,1,1]
# }

# df = pd.DataFrame(data)

# # Features

# X = df[["Age"]]

# # Target
# y = df["Purchased"]


# # Create Model
#                                # k=3
# model = KNeighborsClassifier(n_neighbors=3)

# # Train Model
# model.fit(X,y)

# # Prediction
# pred = model.predict([[40]])

# print("Prediction:",pred[0])

# # Accuracy
# print("Accuracy:",model.score(X,y))