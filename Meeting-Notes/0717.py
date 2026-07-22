# Matplotlib
# - Matplotlib is an open-source Python library used to create graphs,charts,and data visualizations.
# It helps convert numerical data into visual charts that are easy to understand.


# Why Do we Need Matplotlib?

# Example:
# Month         Sales
#  Jan          25000
#  Feb          32000
#  March        40000
#  Apr          38000


# Ai/Ml workflow
# collect data
#    |
# CLean data
#    |
# Analyze data
#    |
# visualize data(Matplotlib)
#    |
# Train Maching Learning Model     
#    |
# Predict Result


# Features of Matplotlib
# - easy to learn
# - Open source
# - Multiple charts Types
# - Highly Customizable


# Matplotlib Installation
# python --version
# pip --version
# pip install matplotlib  or (python -m pip install matplotlib)
# pip install --upgrade matplotlib
# pip show matplotlib




# *********  Importing Matplotlib
# import matplotlib.pyplot as plt

# matplotlib -> Main library
# pyplot -> Module used for plotting graphs
# plt -> Alias(short name)


# What is pyplot module?
# -> pyplot is most commonly used module in matplotlib.
# it provides functions to:
# - create charts
# - Display charts
# - Customize charts
# - save charts


# Common pyplot functions-
# plot() - Create a line chart
# show() - Display the chart
# title() - Add a chart title
# xlabel() - Add X-axix label
# ylabel() - Add Y-axix label
# legend() - Display legend
# grid() - show grid
# figure() - Create a new figure


# Example:

# import matplotlib.pyplot as plt

# x = [1,2,3,4,5]   # x-axis
# y = [10,20,15,25,30] # Y - axis

# plt.plot(x,y)
# plt.show()


# import matplotlib.pyplot as plt

# x = [1,2,3,4,5]   # x-axis
# y = [10,20,15,25,30] # Y - axis

# plt.plot(x,y)
# plt.show()



# *** What is Line Chart?
# -> A line chart is a graph that connects data points using straight lines.
# it is mainly used to show:-
# Trend
# Growth
# Comparison
# Changes over time

# import matplotlib.pyplot as plt

# x = [1,2,3,4,5]   # x-axis
# y = [10,20,15,25,30] # Y - axis

# plt.plot(x,y)
# plt.show()



# Figure
# - A Figure is the complete chart window where graphs are drawn.

# syntax:
# plt.figure()



# Figure Size:
# By default,Matplotlib creates a standard-sized figure.
# you can change it using figsize.

# syntax:
# plt.figure(figsize=(width,height))


# Example:
# import matplotlib.pyplot as plt

# x = [1,2,3,4,5]   # x-axis
# y = [10,20,15,25,30] # Y - axis

# plt.figure(figsize=(10,9))

# plt.plot(x,y)
# plt.show()



# Axes
# - Axes are the area where the graph is actually drawn.

# every graph contains:
# X - axis(Horizontal)
# Y - axis(Vertical)


# Example:
# import matplotlib.pyplot as plt

# flg = plt.figure()
# ax = flg.add_subplot()
# ax.plot([1,2,3],[10,20,30])
# plt.show()


# Matplotlib
# - Matplotlib is an open-source Python library used to create graphs,charts,and data visualizations.
# It helps convert numerical data into visual charts that are easy to understand.


# Why Do we Need Matplotlib?

# Example:
# Month         Sales
#  Jan          25000
#  Feb          32000
#  March        40000
#  Apr          38000


# Ai/Ml workflow
# collect data
#    |
# CLean data
#    |
# Analyze data
#    |
# visualize data(Matplotlib)
#    |
# Train Maching Learning Model     
#    |
# Predict Result


# Features of Matplotlib
# - easy to learn
# - Open source
# - Multiple charts Types
# - Highly Customizable


# Matplotlib Installation
# python --version
# pip --version
# pip install matplotlib  or (python -m pip install matplotlib)
# pip install --upgrade matplotlib
# pip show matplotlib




# *********  Importing Matplotlib

# import matplotlib.pyplot as plt

# matplotlib -> Main library
# pyplot -> Module used for plotting graphs
# plt -> Alias(short name)


# What is pyplot module?
# -> pyplot is most commonly used module in matplotlib.
# it provides functions to:
# - create charts
# - Display charts
# - Customize charts
# - save charts


# Common pyplot functions-
# plot() - Create a line chart
# show() - Display the chart
# title() - Add a chart title
# xlabel() - Add X-axis label
# ylabel() - Add Y-axis label
# legend() - Display legend
# grid() - show grid
# figure() - Create a new figure


# Example:

# import matplotlib.pyplot as plt

# x = [1,2,3,4,5]   # x-axis
# y = [10,20,15,25,30] # Y - axis

# plt.plot(x,y)
# plt.show()


# *** What is Line Chart?
# -> A line chart is a graph that connects data points using straight lines.
# it is mainly used to show:-
# Trend
# Growth
# Comparison
# Changes over time

# import matplotlib.pyplot as plt

# x = [1,2,3,4,5]   # x-axis
# y = [10,20,15,25,30] # Y - axis

# plt.plot(x,y)
# plt.show()



# Figure
# - A Figure is the complete chart window where graphs are drawn.

# syntax:
# plt.figure()



# Figure Size:
# By default,Matplotlib creates a standard-sized figure.
# you can change it using figsize.

# syntax:
# plt.figure(figsize=(width,height))


# Example:
# import matplotlib.pyplot as plt

# x = [1,2,3,4,5]   # x-axis
# y = [10,20,15,25,30] # Y - axis

# plt.figure(figsize=(10,9))

# plt.plot(x,y)
# plt.show()


# Figure = Notebook
# Axes = Notebook Page



# Axes
# - Axes are the area where the graph is actually drawn.

# every graph contains:
# X - axis(Horizontal)
# Y - axis(Vertical)


# Example:
# import matplotlib.pyplot as plt

# flg = plt.figure()
# ax = flg.add_subplot()
# ax.plot([1,2,3],[10,20,30])
# plt.show()


# Figure
#  ----------------------------
# |                            |
# |        Axes                |
# |   ---------------------    |
# |  |                     |   |
# |  |      Graph          |   |
# |  |                     |   |
# |   ---------------------    |
# |____________________________|


# *** Multiple lines 
# - Multiple lines are used to compare two or more datasets on the same graph.

# Example:
# import matplotlib.pyplot as plt
# subject = [1,2,3,4,5]
# student_a = [75,80,78,90,88]
# student_b = [70,85,80,86,92]

# plt.plot(subject,student_a)
# plt.plot(subject,student_b)
# plt.show()