# Introduction to Scikit-learn

# *1. What is Scikit-learn?
# Definition
# Scikit-learn (also called sklearn) is one of the most popular Python libraries for Machine Learning.
# It provides ready-made tools and algorithms that help us build machine learning models without implementing complex mathematical formulas from scratch.

# *2. Why is Scikit-learn Used in AI/ML?

# Before training a machine learning model, data needs to be prepared and cleaned.
# Scikit-learn helps us:
#  Split data into training and testing sets.
#  Handle missing values.
#  Encode categorical data.
#  Scale numerical features.
#  Select important features.
#  Train machine learning models.
#  Evaluate model performance.
#  Make predictions.

# Applications of Scikit-learn
# Scikit-learn is widely used in:
#  Customer Churn Prediction
#  Employee Salary Prediction
#  House Price Prediction
#  Student Performance Prediction
#  Spam Email Detection
#  Fraud Detection
#  Disease Prediction
#  Product Recommendation Systems

# *3. Features of Scikit-learn

# 1. Easy to Learn
# Scikit-learn has a simple and beginner-friendly syntax.

# 2. Open Source
# It is free to use and supported by a large developer community.

# 3. Data Preprocessing
# It provides tools to:
# Handle missing values
# Encode categorical data
# Scale numerical data
# Split datasets

# 4. Machine Learning Algorithms
# Scikit-learn includes many algorithms, such as:
# Linear Regression
# Logistic Regression
# Decision Tree
# Random Forest
# K-Nearest Neighbors (KNN)
# Support Vector Machine (SVM)
# Naive Bayes
# K-Means Clustering

# *4. Installing Scikit-learn
# Using pip
# Open Command Prompt, Terminal, or PowerShell and run:
# pip install scikit-learn

# If Using Jupyter Notebook
# !pip install scikit-learn

# If Using Anaconda
# conda install scikit-learn

# Check Installation
# import sklearn

# print(sklearn.__version__)
# Example Output
# 1.7.0
# (Version may vary depending on your installation.)

# 1. Importing Scikit-learn

# Unlike NumPy or Pandas, Scikit-learn is divided into many modules.
# We import only the module we need.

# Example 1 – Import Train-Test Split
# from sklearn.model_selection import train_test_split

# Example 2 – Import StandardScaler
# from sklearn.preprocessing import StandardScaler

# Example 3 – Import LabelEncoder
# from sklearn.preprocessing import LabelEncoder

# Example 4 – Import SimpleImputer
# from sklearn.impute import SimpleImputer

# Why Do We Import Specific Modules?

# Scikit-learn contains hundreds of functions.
# Importing only the required module:
# Saves memory
# Improves readability
# Makes the code easier to maintain


# ** Understanding Dataset, Features (X) & Target Variable (y)

# 1. What is a Dataset?
# Definition
# A Dataset is a collection of related data organized in rows and columns.
# In Machine Learning, datasets are used to train, test, and evaluate models.
# Each row is called a record or observation, and each column is called a feature or attribute.

# 2. Dataset Overview
# Before building a Machine Learning model, we must understand the dataset.

# Read Dataset
# import pandas as pd

# df = pd.read_csv("employees.csv")

# View First 5 Rows
# df.head()

# View Last 5 Rows
# df.tail()

# Dataset Information
# df.info()
# Output includes:
# Number of rows
# Number of columns
# Data types
# Missing values

# Statistical Summary
# df.describe()
# Displays:
# Count
# Mean
# Standard Deviation
# Minimum
# Maximum
# Quartiles

# Column Names
# df.columns

# Dataset Shape
# df.shape
# Example Output:
# (100, 5)
# Meaning:
# 100 Rows
# 5 Column

# 1. Features (X)
# Definition
# Features are the input variables used to make predictions.
# They are represented by X.

# Example
# Employee Dataset

# Age    Experience  Education    Salary
#  22       1         Graduate     25000
#  23       2         Post-Graduate   55000

# If we want to predict Salary, then:

# Features are:
# Age
# Experience
# Education

# Creating Features (X)
# X = df[["Age", "Experience", "Education"]]

# 1. Target Variable (y)
# Definition
# The Target Variable is the value we want the Machine Learning model to predict.
# It is represented by y.

# Example
# Employee Dataset

# Age    Experience  Education    Salary
#  22       1         Graduate     25000
#  23       2         Post-Graduate     55000

# Target Variable:
# y = df["Salary"]

# Example of X and y
# import pandas as pd

# df = pd.read_csv("employees.csv")

# X = df[["Age", "Experience", "Education"]]

# y = df["Salary"]

# Difference Between X and y

# Features (X)        Target Variable (y)

# Input Data           Output Data

# Used to make         Value to be predicted
# predictions

# Multiple columns     Usually one column

# 1. Independent Variables
# Definition
# Independent Variables are the variables that influence the prediction.
# These are also called Features (X).

# Example
# Employee Salary Prediction
# Independent Variables:
# Age
# Experience
# Education
# These values help predict Salary.

# 1. Dependent Variable
# Definition
# The Dependent Variable depends on the Independent Variables.
# It is also called the Target Variable (y).

# Example
# Employee Salary depends on:
# Age
# Experience
# Education
# Therefore:
# Salary = Dependent Variable

# 1. Supervised Learning
# Definition
# Supervised Learning is a type of Machine Learning where the dataset contains both:
# Features (X)
# Target Variable (y)
# The model learns from labeled data.

# Example
# Predict Student Pass/Fail

# Study Hours     Attendance     Result
#   2               70           Fail
#   5               90           Pass
#   6               95           Pass

# Here:

# Features:
#  Study Hours
#  Attendance

# Target:
#  Result

# Examples of Supervised Learning
#  Salary Prediction
#  House Price Prediction
#  Student Result Prediction
#  Disease Prediction
#  Email Spam Detection

# 1. Unsupervised Learning
# Definition
# Unsupervised Learning uses datasets that do not have a target variable.
# The model finds hidden patterns or groups in the data.

# Example
# Customer Dataset

# Age       Income      Spending Score
# 22         30000         65
# 30         60000         45

# No target column exists.
# The algorithm groups similar customers together.

# Examples of Unsupervised Learning
# Market Basket Analysis
# Product Recommendation
# Data Clustering
# Pattern Detection



# Supervised vs Unsupervised Learning

# Supervised Learning         Unsupervised Learning
#  Has Target Variable          No Target Variable
#  Uses Labeled Data            Uses Unlabeled Data
#  Makes Predictions            Finds Hidden Patterns
# Example: Salary Prediction    Example: Customer Segmentation





# ***Train-Test Split

# 1. Why Split Data?
# Definition
# Before training a Machine Learning model, the dataset is divided into two parts:
#  Training Dataset
#  Testing Dataset
# This ensures the model is evaluated on new, unseen data instead of the same data it was trained on.


# Example
# Suppose you have 100 employee records.
# A common split is:
# 80 records → Training Dataset
# 20 records → Testing Dataset



# 2. Training Dataset
# Definition
# The Training Dataset is the portion of the data used to teach the Machine Learning model.
# The model learns patterns, relationships, and rules from this data.



# 3. Testing Dataset
# Definition
# The Testing Dataset is used after training to evaluate the model's performance.
# The model has never seen this data before.

# Purpose of Testing Data
# Evaluate model accuracy.
# Measure prediction performance.
# Check whether the model generalizes well to new data.


# 4. train_test_split()
# Definition
# train_test_split() is a function from Scikit-learn that automatically divides the dataset into training and testing sets.

# Import Statement
# from sklearn.model_selection import train_test_split

# Syntax
# X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)


# Parameter              Description
#  X                    Features (Input Data)
#  y                    Target Variable (Output Data)
# test_size             Percentage of data used for testing
# random_state          Controls random splitting for reproducible results


# 5. Understanding test_size
# Definition
# test_size specifies how much of the dataset should be used for testing.
# The remaining data is used for training.


# Examples
# 80% Training – 20% Testing
# test_size=0.2

# 70% Training – 30% Testing
# test_size=0.3

# 75% Training – 25% Testing
# test_size=0.25



# Visualization
# 100 Records

# 80 → Training
# 20 → Testing

# or
# 100 Records

# 70 → Training
# 30 → Testing



# 6. Understanding random_state
# Definition
# random_state controls how the data is shuffled before splitting.
# It ensures that you get the same split every time you run the program


# Example Without random_state
# train_test_split(
#     X,
#     y,
#     test_size=0.2
# )
# Every execution may produce a different train-test split.


# Example With random_state
# train_test_split(
#     X,
#     y,
#     test_size=0.2,
#     random_state=42
# )
# Every execution produces the same split, making experiments reproducible.


# Common Values
# random_state=0
# random_state=42
# random_state=100
# The number itself has no special meaning—it is simply a fixed seed.