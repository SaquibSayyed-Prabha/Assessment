# *** Linear Regression


# What is Regression?
# - Regression is a Machine Learning technique used to predict continuous numerical values.

# Examples
#  -House Price Prediction
#  -Employee Salary Prediction
#  -Student Marks Prediction
#  -Temperature Prediction
#  -Sales Prediction



# What is Linear Regression?
# -Linear Regression is a Machine Learning algorithm that predicts a numerical value by finding the best-fit straight line,
#  between the input (X) and output (y).



# *** Why is Linear Regression Used?
# Linear Regression is used because it is:
#  -Easy to understand
#  -Fast to train
#  -Good for predicting numerical values
#  -Widely used in business and AI/ML projects




# ***Real-World Applications
#  -House Price Prediction
#  -Employee Salary Prediction
#  -Sales Forecasting
#  -Stock Price Analysis (basic)
#  -Temperature Prediction
#  -Electricity Consumption Prediction



# *** Steps to Build a Linear Regression Model
# The process is simple.

# Create Dataset
#       ↓
# Features (X)
#       ↓
# Target (y)
#       ↓
# Create Model
#       ↓
# Train Model
#       ↓
# Prediction
#       ↓
# Evaluate Model


# **** Import Required Libraries

# import pandas as pd
# from sklearn.linear_model import LinearRegression


# Example:
# import pandas as pd
# from sklearn.linear_model import LinearRegression

# # Create Dataset
# data = {
#     "Experience":[1,2,3,4,5],
#     "Salary":[25000,30000,38000,45000,52000]
# }

# df = pd.DataFrame(data)

# # Features
# X = df[["Experience"]]

# # Target
# y = df["Salary"]

# # Create Model
# model = LinearRegression()

# # Train Model
# model.fit(X,y)

# prediction = model.predict([[6]])

# print("Predicted Salary:",round(prediction[0],-3))





# Example:

# House Price Prediction :-

# import pandas as pd
# from sklearn.linear_model import LinearRegression

# data = {
#     "Area":[800,1000,1200,1500,1800,2000,2200,2500],
#     "Price":[2500000,3200000,3900000,4800000,5800000,6500000,7200000,8200000]
# }

# df = pd.DataFrame(data)

# print("House Dataset:")
# print(df)

# X = df[["Area"]]

# y = df["Price"]

# model = LinearRegression()

# model.fit(X,y)

# # Predict New House Price

# new_area = 1700

# prediction = model.predict([[new_area]])

# print("\n House Area:",new_area,"sq.ft")
# print("Predicted Price:₹",round(prediction[0]))






