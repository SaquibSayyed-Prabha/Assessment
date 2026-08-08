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




# ======================================================================================================================================================
# *** Correlation Matrix
# -A Correlation Matrix is a table that shows the correlation between all numerical columns in a dataset.
#  Each value represents how strongly two columns are related.


# Example Dataset:

# Age    Experience   Salary
# 22      1             25000
# 25      3             35000
# 30      6             55000
# 35     10             80000


# Example:

# import pandas as pd

# data = {
#   "Age":[22,25,30,35],
#   "Experience":[1,3,6,10],
#    "Salary":[25000,35000,50000,80000]
# }

# df = pd.DataFrame(data)

# print(df.corr())




# *** Selecting Features Using Correlation

# Example:

# import pandas as pd

# data = {
#   "Age":[22,25,30,35],
#   "Experience":[1,3,6,10],
#   "Salary":[25000,35000,50000,80000]
# }

# df = pd.DataFrame(data)

# print(df.corr())

# # Feature select
# X = df[["Age","Experience"]]

# # Target Select
# y = df["Salary"]

# print(X)
# print(y)


# *** Heatmap Visualization
# - A Heatmap is a graphical representation of the Correlation Matrix.
#  It uses colors to show the strength of correlation.


# Example:

# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt


# data = {
#   "Age":[22,25,30,35],
#   "Experience":[1,3,6,10],
#   "Salary":[25000,35000,50000,80000]
# }

# df = pd.DataFrame(data)


# correlation = df.corr()

# plt.figure(figsize=(6,4))

# sns.heatmap(correlation,annot=True,cmap="coolwarm")

# plt.title("Correlation HeatMap")

# plt.show()



# Example:
# import pandas as pd

# data = {
#     "Emp_id":[101,102,103],
#     "Name":["Amit","Rahul","Sneha"],
#     "Age":[25,30,28],
#     "Experience":[2,5,4],
#     "Department":["IT","HR","Finance"],
#     "Salary":[30000,50000,45000]
# }

# df = pd.DataFrame(data)

# # Remove unnecessary columns
# df = df.drop(columns=["Emp_id","Name"])

# # Features
# X = df[["Age","Experience","Department"]]

# # Target
# y = df["Salary"]

# print(X)
# print(y)



# 1.What is Machine Learning?
# -Machine Learning (ML) is a branch of Artificial Intelligence (AI) that enables computers to learn from data and make predictions or decisions without being explicitly programmed for every task.



# Why Machine Learning is Used?
# Machine Learning helps computers make intelligent decisions automatically.
# It is used because:
# It learns from data.
# It improves prediction accuracy.
# It saves time.
# It handles large amounts of data.
# It finds hidden patterns.

# Real-World Applications
# Email Spam Detection
# Face Unlock in Mobile
# Netflix Movie Recommendation
# YouTube Video Recommendation
# Google Translate
# Google Maps Traffic Prediction
# Online Shopping Product Recommendation
# Fraud Detection
# House Price Prediction
# Medical Disease Prediction
# Voice Assistants (Alexa, Siri, Google Assistant)





# 2.Types of Machine Learning
# Machine Learning has three main types.

# 1. Supervised Learning
# In Supervised Learning, the dataset contains both input and correct output.
# The model learns using labeled data.


# Example
# Study Hours  Marks
# 2            35
# 4            50
# 6            75

# Input = Study Hours
# Output = Marks
# The model learns the relationship and predicts marks for new students.


# Real-Life Examples
# -House Price Prediction
# -Student Marks Prediction
# -Salary Prediction
# -Diabetes Prediction
# -Loan Approval Prediction



# 2. Unsupervised Learning
# In Unsupervised Learning, the dataset contains only input data.
# There are no correct answers (labels).
# The model finds hidden patterns or groups in the data.

# Example
# Suppose you have customer shopping data.
# The model groups customers based on similar buying behavior.


# Real-Life Examples
# -Customer Segmentation
# -Product Grouping
# -Market Basket Analysis



# 3. Reinforcement Learning

# In Reinforcement Learning, the computer learns by trial and error.
# It receives rewards for correct actions and penalties for wrong actions.

# Real-Life Examples
# -Self-driving Cars
# -Robot Navigation
# -Chess AI
# -Game Playing AI




# Machine Learning Workflow
# Machine Learning follows a sequence of steps.
# Collect Data
#       ↓
# Load Dataset
#       ↓
# Explore Data
#       ↓
# Data Cleaning
#       ↓
# Feature Selection
#       ↓
# Train-Test Split
#       ↓
# Choose ML Algorithm
#       ↓
# Train Model
#       ↓
# Prediction
#       ↓
# Evaluate Model




# Model
# -A Machine Learning Model is a program that learns patterns from training data and uses those patterns to make predictions.


# Prediction
# -A Prediction is the output produced by a trained machine learning model for new input data.

# Machine Learning Data Preprocessing Challenge

# Use the provided employee_dataset.csv and complete the following preprocessing steps in order.

# Tasks
# Load Dataset
# Read the CSV file using Pandas.
# Display the first 5 records.
# Display dataset information (info()).
# Display summary statistics (describe()).
# Handle Missing Values
# Check for missing values.
# Fill missing values using an appropriate method.
# Remove Duplicate Records
# Check how many duplicate rows exist.
# Remove all duplicate records.
# Verify that duplicates have been removed.
# Encode Categorical Data
# Identify categorical columns.
# Convert categorical values into numerical values using LabelEncoder.
# Feature Engineering
# Create at least one new feature using existing columns.
# Example: Create Experience_Level from Experience.
# Feature Selection
# Remove unnecessary columns that are not useful for prediction.
# Display the final selected features.
# Feature Scaling
# Apply StandardScaler to all numerical feature columns.
# Do not scale the target column.
# Create Features (X)
# Create the input feature dataset (X).
# Create Target Variable (y)
# Create the target variable (y) using the Salary column.
# Train-Test Split
# Split the dataset into 80% Training and 20% Testing using train_test_split.
# Display the shapes of X_train, X_test, y_train, and y_test.





# Load Dataset
#       │
#       ▼
# Handle Missing Values
#       │
#       ▼
# Remove Duplicate Records
#       │
#       ▼
# Encode Categorical Data
#       │
#       ▼
# Feature Engineering
#       │
#       ▼
# Feature Selection
#       │
#       ▼
# Feature Scaling
#       │
#       ▼
# Create Features (X)
#       │
#       ▼
# Create Target Variable (y)
#       │
#       ▼
# Train-Test Split


# ***What is MVC?
# MVC (Model-View-Controller) is a software design pattern that separates an application into three parts:

# Model → Database and data operations
# View → Response sent to the client (JSON in REST API)
# Controller → Handles requests and business logic

# ***MVC Architecture

# React Frontend
#       │
#       ▼
# Flask Controller
#       │
#       ▼
# Model
#       │
#       ▼
# SQLite Database
#       │
#       ▼
# Controller
#       │
#       ▼
# JSON Response
#       │
#       ▼
# React Frontend

# ***MVC Components

# 1. Model
# **Responsible For:

# - Database Tables
# - Insert Data
# - Update Data
# - Delete Data
# - Fetch Data

# 1. Controller
# **Responsible For:

# - Receiving Requests
# - Calling Model
# - Returning JSON Response

# 1. View

# - The View is the JSON Response returned to the frontend.

# Example:
# {
#       "id":1,
#       "name":"xyz",
#       ---
# }

# ***Backend Folder Structure



# student_management_api/
# │
# ├── app.py
# ├── config.py
# ├── requirements.txt
# │
# ├── controllers/
# │      ├── __init__.py
# │      └── student_controller.py
# │
# ├── models/
# │      ├── __init__.py
# │      └── student_model.py
# │
# ├── routes/
# │      ├── __init__.py
# │      └── student_routes.py
# │
# ├── database/
# │      └── students.db
# │
# └── utils/
#        └── helper.py

# *** API Flow
# React

# ↓

# Routes

# ↓

# Controller

# ↓

# Model

# ↓

# SQLite

# ↓

# Controller

# ↓

# JSON Response

# ↓

# React






