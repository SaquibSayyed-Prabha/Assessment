# Introduction to Seaborn

# Definition:

# Seaborn is a Python visualization library used to create beautiful statistical graphs with less code.


# Why is Seaborn Used in AI/ML?

# In Artificial Intelligence and Machine Learning, data must be understood before building a model.
# Seaborn helps us:
# Visualize datasets
# Find patterns
# Detect trends
# Compare categories
# Analyze relationships
# Identify outliers
# Understand feature correlations


# Applications of Seaborn

# Seaborn is widely used in:
# AI & Machine Learning
# Data Analytics
# Data Science
# Business Intelligence
# Financial Analysis
# Sales Analysis
# Healthcare Analytics
# Marketing Reports
# Educational Reports


# Features of Seaborn

# 1. Beautiful Charts

# Seaborn creates attractive charts with modern styles by default.

# 2. Simple Syntax

# Compared to Matplotlib, Seaborn requires fewer lines of code.

# 3. Statistical Visualization

# It is specially designed for statistical data analysis.
# Examples:
# Distribution
# Correlation
# Relationship Analysis
# Category Comparison

# 4. Built-in Themes

# Seaborn provides professional themes automatically.
# Examples:
# darkgrid
# whitegrid
# dark
# white
# ticks


# 5. Built-in Datasets

# Seaborn includes sample datasets for learning.
# Examples:
# tips
# iris
# titanic
# penguins
# flights

# 6. Works with Pandas

# Seaborn works directly with Pandas DataFrames.
# Example:

# import seaborn as sns
# import pandas as pd

# df = pd.read_csv("students.csv")

# sns.barplot(data=df, x="Name", y="Marks")


# 7. Easy Customization
# You can easily change:
# Colors
# Titles
# Labels
# Figure Size
# Themes


# Installing Seaborn
# Using pip
# Open Command Prompt or Terminal and run:

# pip install seaborn


# Importing Seaborn

# The standard way to import Seaborn is:

# import seaborn as sns

# Here:
# seaborn → Library Name
# sns → Alias (short name)


# Importing Required Libraries

# Most Seaborn programs also use:

# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd

# Library           Purpose

# seaborn           Statistical charts
# matplotlib        Display charts
# pandas            Read and manage datasets


# * First Seaborn Program

# import seaborn as sns
# import matplotlib.pyplot as plt

# tips = sns.load_dataset("tips")

# print(tips.head())



# When to Use Matplotlib?

# * Use Matplotlib when:

# Creating custom charts
# Fine control over graphs
# Drawing low-level visualizations
# Creating subplots and dashboards


# When to Use Seaborn?

# * Use Seaborn when:
# Working with datasets
# Creating statistical charts
# Performing data analysis
# Comparing categories
# Finding correlations
# Building AI/ML visualizations




# *** Basic Seaborn Charts


# 1:  Loading Built-in Datasets
# - Seaborn provides several sample datasets that help us learn data visualization without downloading external csv files.
# - These datasets are already available inside the Seaborn library.


# Syntax:

# import seaborn as sns
# df = sns.load_dataset("dataset_name")

# Example:

# import seaborn as sns

# tips = sns.load_dataset("tips")

# print(tips.head())


# * head() - return First 5 rows.
# * tail() - return last 5 rows.
# * info() - Display dataset information.
# * describe() - Display Statistical Summary.

# Example:
# import seaborn as sns

# tips = sns.load_dataset("tips")

# # print(tips.head())
# # print(tips.tail())
# # print(tips.info())
# print(tips.describe())


# ** Count Plot
# - A Count Plot Display the number of occurrences(frequency) of each Category.
# - It is used for categorical data.


# Syntax:
# sns.countplot(data=df,x="column_name")

# Example:
# import seaborn as sns
# import matplotlib.pyplot as plt

# tips = sns.load_dataset("tips")
# # print(tips.head)
# sns.countplot(data=tips,x="sex")
# plt.show()


# Example:
# import seaborn as sns
# import matplotlib.pyplot as plt

# t1 = sns.load_dataset("tips")
# sns.countplot(data=t1,x="day")

# plt.show()



# ** Bar Plot

# What is a Bar plot?
# -> A Bar Plot compares the average(or another aggregate) value of a numerical column across different categories.
# - By default , Seaborn calculates the mean of the numeric values.

# Syntax:

# sns.barplot(data=df,x="category",y="value")

# Example:
# import seaborn as sns
# import matplotlib.pyplot as plt

# tips = sns.load_dataset("tips")
# # print(tips)
# sns.barplot(data=tips,x="day",y="total_bill")

# plt.show()


# ** Line Plot
# What is line Plot.
# - A Line Plot shows how values change over time or in a sequence.
# it helps Identify:
# -trends
# -growth
# -Increase
# -Decrease


# Syntax:
# sns.lineplot(data=df,x="column1",y="column2")

# Example:

# import seaborn as sns
# import matplotlib.pyplot as plt

# months = ["Jan","Feb","Mar","Apr","May"]
# sales = [120,150,170,200,220]

# sns.lineplot(x=months,y=sales,marker="o")

# plt.show()


# ** Scatter Plot
# What is a Scatter Plot?
# -> A Scatter plot Display the relationship between two numerical variables.

# Syntax:
# sns.scatterplot(data=df,x="column1",y="column2")

# Example:

# import seaborn as sns
# import matplotlib.pyplot as plt

# height = [150,155,160,165,170,175]
# weight = [45,50,55,60,68,75]

# sns.scatterplot(x=height,y=weight)

# plt.show()


# Example:
# import seaborn as sns
# import matplotlib.pyplot as plt

# plt.figure(figsize=(10,6))

# tips = sns.load_dataset("tips")
# # print(tips)
# sns.barplot(data=tips,x="day",y="total_bill",color="red")

# plt.title("Average Bill by Day")
# plt.xlabel("Day")
# plt.ylabel("Average Bill")
# plt.show()


# ** Histogram
# - A Histogram is used to Display the Distribution of numerical data.

# Syntax:

# sns.histplot(data=df,x="column_name")

# Example:

# import seaborn as sns
# import matplotlib.pyplot as plt

# marks = [45,55,60,62,65,68,70,75,82,95]

# sns.histplot(x=marks)

# plt.show()


# Example: Using a Datasets

# import seaborn as sns
# import matplotlib.pyplot as plt

# t1 = sns.load_dataset("tips")

# sns.histplot(data=t1,x="total_bill")

# plt.show()


# Example: bins

# import seaborn as sns
# import matplotlib.pyplot as plt

# t1 = sns.load_dataset("tips")

# sns.histplot(data=t1,x="total_bill",bins=5)

# plt.show()




# Example:

# import seaborn as sns
# import pandas as pd

# d1 = pd.read_csv("student.csv")

# sns.barplot(data=d1,x="Name",y="Marks")