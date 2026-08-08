# *** Decision Tree

# A Decision Tree is a Supervised Machine Learning algorithm used for Classification and Regression problems.

# It makes predictions by asking a series of questions or conditions.

# - Decision Tree = Questions → Decisions → Final Prediction


#                   Question
#                  /        \
#               Answer     Answer
#                /            \
#           Question         Result
#           /     \
#        Result   Result



# **Why is Decision Tree Used?
# Decision Tree is popular because:
#  Easy to understand
#  Easy to visualize
#  Works for both Classification and Regression
#  Handles numerical and categorical data
#  Requires less data preparation


# Real-World Applications
#  Loan Approval Prediction
#  Customer Purchase Prediction
#  Employee Promotion Prediction
#  Medical Disease Prediction
#  Student Performance Prediction
#  Fraud Detection



# Decision Tree Structure

#                Root Node
#                     |
#              Is Age > 25?
#               /          \
#             No            Yes
#             |              |
#        Salary > 30000?   Purchased
#         /        \
#       No         Yes
#       |            |
#  Not Purchased  Purchased




# **Important Terms

# -Root Node
#  The Root Node is the first decision in the tree.
#  It contains the most important feature.


# **Decision Node
#  A Decision Node asks another question after the root node.

# Example:
# Salary > 30000?



# **Leaf Node
# A Leaf Node is the final result or prediction.
# Example:
# Purchased
# Not Purchased



# **Advantages of Decision Tree
#  Simple to understand
#  Easy to explain
#  No feature scaling required
#  Handles missing values better than some algorithms
#  Can work with numerical and categorical data



# **Disadvantages of Decision Tree
#  Can overfit the training data
#  Small changes in data may create a different tree
#  Less accurate than ensemble methods like Random Forest in many cases


# **Import Required Libraries
#  import pandas as pd
#  from sklearn.tree import DecisionTreeClassifier


#  Example:

#  import pandas as pd
# from sklearn.tree import DecisionTreeClassifier


# # Create Dataset

# # No = 0
# # Yes = 1

# data = {
#     "Age":[18,20,22,24,26,28,30,32],
#     "Salary":[18000,22000,26000,30000,35000,40000,45000,50000],
#     "Purchased":[0,0,0,1,1,1,1,1]
# }

# df = pd.DataFrame(data)

# # Features

# X = df[["Age","Salary"]]

# # Target
# y = df["Purchased"]

# # Create Model

# model =  DecisionTreeClassifier(random_state=42)

# # train model
# model.fit(X,y)

# # Prediction
# pred = model.predict([[25,32000]])

# print("Prediction:",pred[0])

# # Accuracy
# print("Accuracy:",model.score(X,y))