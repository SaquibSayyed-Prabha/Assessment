# ***  Histogram & Scatter Plot

# * What is a Histogram?
# -> A Histogram is a chart used to Display the distribution of numerical data.


# Creating a Histogram.

# Syntax:
# plt.hist(data)


# Example:
# import matplotlib.pyplot as plt

# marks = [45,55,60,65,70,75,80,85,90,95]

# plt.hist(marks)
# plt.show()



# Bins:
# - A bin is a range of values.
# The bins parameter dicides how many groups the data should be divided into.

# Syntax:
# plt.hist(data,bins=5)

# import matplotlib.pyplot as plt

# marks = [
#     35, 38, 40, 42, 45,
#     46, 48, 50, 52, 55,
#     56, 58, 60, 61, 62,
#     64, 65, 66, 68, 70,
#     71, 72, 74, 75, 76,
#     78, 80, 81, 82, 84,
#     85, 86, 88, 90, 91,
#     92, 94, 95, 97, 99
# ]

# plt.hist(marks,bins=5)
# plt.show()


# * Changing Colors
# Syntax:
# plt.hist(data,color="orange")

# Example:

# import matplotlib.pyplot as plt

# marks = [
#     35, 38, 40, 42, 45,
#     46, 48, 50, 52, 55,
#     56, 58, 60, 61, 62,
#     64, 65, 66, 68, 70,
#     71, 72, 74, 75, 76,
#     78, 80, 81, 82, 84,
#     85, 86, 88, 90, 91,
#     92, 94, 95, 97, 99
# ]
# plt.hist(marks,bins=3,color="orange",width=10)
# plt.show()



# - Edge color

# Syntax:
# edgecolor="color_name"

# Example:
# import matplotlib.pyplot as plt

# marks = [
#     35, 38, 40, 42, 45,
#     46, 48, 50, 52, 55,
#     56, 58, 60, 61, 62,
#     64, 65, 66, 68, 70,
#     71, 72, 74, 75, 76,
#     78, 80, 81, 82, 84,
#     85, 86, 88, 90, 91,
#     92, 94, 95, 97, 99
# ]
# plt.hist(marks,bins=3,color="orange",width=10,edgecolor="black")
# plt.show()


# ** labels
# import matplotlib.pyplot as plt

# marks = [
#     35, 38, 40, 42, 45,
#     46, 48, 50, 52, 55,
#     56, 58, 60, 61, 62,
#     64, 65, 66, 68, 70,
#     71, 72, 74, 75, 76,
#     78, 80, 81, 82, 84,
#     85, 86, 88, 90, 91,
#     92, 94, 95, 97, 99
# ]
# plt.hist(marks,bins=3,color="orange",width=10,edgecolor="black")
# plt.title("Student Marks")
# plt.xlabel("Marks")
# plt.ylabel("Number of Students")
# plt.show()



# *** Scatter Plot
# - A Scatter Plot Display the relationship between two numerical variables.
# - Each point on the graph represents one observation.

# * Creating a Scatter Plot.

# Syntax:

# plt.scatter(x,y)

# Example:

# import matplotlib.pyplot as plt

# hours = [2,3,4,5,6,7]
# marks = [45,55,60,72,80,88]

# plt.scatter(hours,marks)

# plt.show()



# * Changing Colors

# Syntax:

# plt.scatter(x,y,color='red')

# Example:

# import matplotlib.pyplot as plt

# hours = [2,3,4,5,6,7]
# marks = [45,55,60,72,80,88]

# plt.scatter(hours,marks,color='orange')

# plt.show()



# * Changing Marker Style.
# - The Marker parameter changes the shape of the points.

# Syntax:

# plt.scatter(x,y,marker='*')

# Example:


# Marker Styles:
# o,*,+,x,D,s,^

# * Changing marker size(s)
# - The s parameter changes the size of the scatter points.

# Syntax:

# plt.scatter(x,y,s=100)

# Example:

# import matplotlib.pyplot as plt

# hours = [2,3,4,5,6,7]
# marks = [45,55,60,72,80,88]

# plt.scatter(hours,marks,color='orange',marker='*',s=500)

# plt.show()



# * Transparency (alpha)

# - The alpha parameter controls the Transparency of the markers.
# - alpha = 1.0 -> Fully visible
# - alpha = 0.5 -> Semi-Transparent
# - alpha = 0.2 -> More-Transparent


# Syntax:

# plt.scatter(x,y,alpha=0.7)

# Example:
# import matplotlib.pyplot as plt

# hours = [2,3,4,5,6,7]
# marks = [45,55,60,72,80,88]

# plt.scatter(hours,marks,color='blue',alpha=0.5,s=500)

# plt.show()



# Example:

# import matplotlib.pyplot as plt

# hours = [2,3,4,5,6,7]
# marks = [45,55,60,72,80,88]

# plt.scatter(hours,marks,color='blue',alpha=0.5,s=500)
# plt.title("Study Hourse vs Marks")
# plt.xlabel("Study Hours")
# plt.ylabel("Marks")
# plt.show()


# ***
# Multiple Charts using subplot()

# What is subplot()?
# -> subplot() is a matplotlib function used to Display Multiple graphs inside a single figure(window).


# subplot()

# +--------------------------------------+
# |        Sales Dashboard               |
# |                                      |
# |  Line Chart      Bar Chart           |
# |                                      |
# |  Pie Chart       Scatter Plot        |
# +--------------------------------------+

# All charts appear in one window.


# Syntax:
# plt.subplot(rows,columns,position)

# Example:

# plt.subplot(2,2,1)

# 2 - Number of rows
# 2 - Number of columns
# 1 - position of the chart


# Example:
# - single subplot

# import matplotlib.pyplot as plt

# plt.subplot(1,1,1)
# plt.plot([1,2,3],[10,20,30])

# plt.show()

# Example:
# - two Chart Together
# import matplotlib.pyplot as plt

# # First Chart
# plt.subplot(1,2,1)
# x=[1,2,3]
# y=[10,20,30]

# plt.plot(x,y)
# plt.title("Line Chart")


# # Second Chart

# plt.subplot(1,2,2)
# x=["A","B","C"]
# y=[20,35,25]
# plt.bar(x,y)
# plt.title("Bar Chart")
# plt.show()




# import matplotlib.pyplot as plt

# plt.figure(figsize=(10,6))

# # First Chart
# plt.subplot(2,2,1)
# x=[1,2,3]
# y=[10,20,30]

# plt.plot(x,y)
# plt.title("Line Chart")


# # Second Chart

# plt.subplot(2,2,2)
# x=["A","B","C"]
# y=[20,35,25]
# plt.bar(x,y)
# plt.title("Bar Chart")


# # Third chart

# plt.subplot(2,2,3)

# plt.pie([40,30,20,10],labels=["A","B","C","D"])

# plt.title("Pie Chart")

# # 4th chart
# plt.subplot(2,2,4)

# plt.scatter([1,2,3,4],[10,20,15,30])

# plt.title("Scatter")
# plt.show()