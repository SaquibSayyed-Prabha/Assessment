# *** Bar Chart
# - A Bar Chart is a graph that represents categorical data using rectangular bars.
# - The height(or lenght) of each bar represents the value of that category.

# - Bar Chart is  used to compare values between different categories.



# Why Use a Bar Chart?
# - Bar Chart make it easy to:
#  - compare categories
#  - identify the highest value
#  - identify the lowest value
#  - Analyze bussiness reports
#  - Present data clearly.


# - Vertical Bar Chart

# Syntax:
# plt.bar(x,y)
#  x -> categories
#  y -> values

# Example:

# import matplotlib.pyplot as plt

# products = ["Laptop","Mobile","Tablet","Headphones"]
# sales = [25,40,15,30]

# plt.bar(products,sales)

# plt.show()




# - Horizontal Bar Chart
#  -  A Horizontal Bar Chart Display bars from left to right instead of bottom to top.

#  Syntax:
#  plt.barh(x,y)

# Example:
# import matplotlib.pyplot as plt

# products = ["Laptop","Mobile","Tablet","Headphones"]
# sales = [25,40,15,30]

# plt.barh(products,sales)

# plt.show()



# * Changing Bar Widht:
# Syntax:
# plt.bar(x,y,Widht=0.5)

# Example:
# import matplotlib.pyplot as plt

# products = ["Laptop","Mobile","Tablet","Headphones"]
# sales = [25,40,15,30]

# plt.bar(products,sales,width=0.9)

# plt.show()



# * Bar Colors
# Syntax:
# plt.bar(x,y,color="Orange")

# Example:
# 1:

# import matplotlib.pyplot as plt

# products = ["Laptop","Mobile","Tablet","Headphones"]
# sales = [25,40,15,30]

# plt.bar(products,sales,color="purple")

# plt.show()

# 2:
# import matplotlib.pyplot as plt

# products = ["Laptop","Mobile","Tablet","Headphones"]
# sales = [25,40,15,30]
# colors=["red","orange","blue","purple"]
# plt.bar(products,sales,color=colors)

# plt.show()


# *Edge color:
# - The edgecolor parameter changes the border color of the bars.

# Syntax:
# plt.bar(x,y,edgecolor="black")

# Example:
# import matplotlib.pyplot as plt

# products = ["Laptop","Mobile","Tablet","Headphones"]
# sales = [25,40,15,30]
# colors=["red","orange","blue","purple"]
# plt.bar(products,sales,color=colors,edgecolor="black")

# plt.show()



# * Adding Labels
# - title
# - X-axis Label
# - Y-axis Label

# Example:
# import matplotlib.pyplot as plt

# products = ["Laptop","Mobile","Tablet","Headphones"]
# sales = [25,40,15,30]
# plt.bar(products,sales,color="orange")
# plt.title("Product Sales")
# plt.xlabel("Products")
# plt.ylabel("Units Sold")
# # plt.grid(axis="x")
# plt.show()


# *** Pie Chart
# - A Pie chart is a circular graph divided into slices.
# - A Pie Chart is used to Display the percentage or proportion of each category in a dataset.



# Example:
# - Creating a Pie Chart
# Syntax:
# plt.pie(values)

# Example:
# import matplotlib.pyplot as plt

# sales = [40,25,20,15]

# plt.pie(sales)
# plt.show()


# Adding Labels:
# - Labels Display the name of each category.

# Syntax:
# plt.pie(values,labels=labels)

# Example:
# import matplotlib.pyplot as plt

# products = ["Laptop","Mobile","Tablet","Watch"]
# sales = [40,25,20,15]

# plt.pie(sales,labels=products)
# plt.show()


# * Changing Slice Colors:
# Syntax:
# plt.pie(values,colors=colors)

# Example:
# import matplotlib.pyplot as plt

# products = ["Laptop","Mobile","Tablet","Watch"]
# sales = [40,25,20,15]
# colors=["red","orange","blue","purple"]

# plt.pie(sales,labels=products,colors=colors)
# plt.show()


# * Display percentage(autopct)

# Syntax:
# plt.pie(values,autopct="%1.1f%%")

# Explanation:
# "%1.1f%%

# 1.1f -> Display one digit after the decimal point.
# %% ->Display the % symbol.

# Example:
# import matplotlib.pyplot as plt

# products = ["Laptop","Mobile","Tablet","Watch"]
# sales = [40,25,20,15]
# colors=["red","orange","blue","purple"]

# plt.pie(sales,labels=products,colors=colors,autopct="%1.1f%%")
# plt.show()




# ** Explode
# - The Explode parameter separates one or more slices from the Pie Chart to highlight them.

# Syntax:
# explode(0,0.1,0,0)

# Explanation:
# 0 -> Slice stays in its original position.
# 0.1 -> slice moves slightly outward.

# Example:

# import matplotlib.pyplot as plt

# products = ["Laptop","Mobile","Tablet","Watch"]
# sales = [40,25,20,15]
# colors=["red","orange","blue","purple"]
# explode=[0,0,0,0.3]
# plt.pie(sales,labels=products,colors=colors,autopct="%1.1f%%",explode=explode)
# plt.show()



# * Shadow 
# - The Shadow parameter adds a Shadow behind the Pie Chart.

# Syntax:
# Shadow=True.

# Example;
# import matplotlib.pyplot as plt

# products = ["Laptop","Mobile","Tablet","Watch"]
# sales = [40,25,20,15]
# colors=["red","orange","blue","purple"]
# explode=[0,0,0,0.3]
# plt.pie(sales,labels=products,colors=colors,autopct="%1.1f%%",explode=explode,shadow=True)
# plt.show()



# * Start Angle:
# - The StartAngle parameter rotates the Pie Chart.
# By default ,the chart starts at 0.

# Syntax:
# startangle=90


# Example:

# import matplotlib.pyplot as plt

# products = ["Laptop","Mobile","Tablet","Watch"]
# sales = [40,25,20,15]
# colors=["red","orange","blue","purple"]
# explode=[0,0,0,0.3]
# plt.pie(sales,labels=products,colors=colors,autopct="%1.1f%%",startangle=90)
# plt.show()



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