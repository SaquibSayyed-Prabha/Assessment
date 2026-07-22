# *** Multiple lines
# - Multiple lines are ued to compare two or more datasets on the same graph.

# Examplel:  Student A vs Student B

# import matplotlib.pyplot as plt

# subjects = [1,2,3,4,5]
# student_a = [75,80,78,90,88]
# student_b = [70,85,80,86,92]


# plt.plot(subjects,student_a)
# plt.plot(subjects,student_b)
# plt.show()



# *** Changing Line Color
# syntax:
# plt.plot(x,y,color="red")

# Example:
# import matplotlib.pyplot as plt

# subjects = [1,2,3,4,5]
# student_a = [75,80,78,90,88]

# plt.plot(subjects,student_a,color="orange")
# plt.show()


# *** Changing Line Style
# syntax:
# plt.plot(x,y,linestyle="--")

# Line Style:
# Style         Meaning 
# "-"            Solid Line
# "--"           Dashed Line
# ":"            Dotted Line
# "-."           Dash-Dot Line


# *** Changing Line width
# syntax:
# plt.plot(x,y,linewidth=3)

# Example:
# import matplotlib.pyplot as plt

# subjects = [1,2,3,4,5]
# student_a = [75,80,78,90,88]

# plt.plot(subjects,student_a,linewidth=3)
# plt.show()


# *** Marker Styles
# - Markers highlight individual data points on a graph.

# syntax:
# plt.plot(x,y,marker="o")

# Example:
# import matplotlib.pyplot as plt

# subjects = [1,2,3,4,5]
# student_a = [75,80,78,90,88]

# plt.plot(subjects,student_a,marker="o")
# plt.show()


# Common Marker Styles
# "o"  - circle
# "*" - star
# "." - point
# "+" - Plus
# "x" - Cross
# "s" - square
# "D" - Diamond
# "^" - Triangle Up
# "v" - Triangle Down


# Example:

# import matplotlib.pyplot as plt

# subjects = [1,2,3,4,5]
# student_a = [75,80,78,90,88]

# plt.plot(subjects,student_a,
#          marker="o",
#          color="red",
#          linestyle="--",
#          linewidth=3
#         )
# plt.show()



# *** Chart Customization


# * Why Chart Customization is Important?
# - A simple chart only Display data.
# A Customized chart helps users understand:
# - What the chart represents.
# - what the X-axis and Y-axis mean.
# - Which line belongs to which dataset.
# - The values more clearly.


# Before Customization:
# - No title
# - No labels
# - No legend
# - No grid


# * Chart title
# - A chart title describes what the graph represents.
# syntax:
# plt.title("Chart title")

# Example:
# import matplotlib.pyplot as plt

# subjects = [1,2,3,4,5]
# student_a = [75,80,78,90,88]
# plt.title("Student Marks")
# plt.plot(subjects,student_a)
# plt.show()



# * X-axis Label
# - The X-axis label describes the horizontal axis.

# syntax:
# plt.xlabel("X-axis Name)

# Example:
# import matplotlib.pyplot as plt
# months = [1,2,3,4]
# sales = [25000,30000,35000,40000]
# plt.plot(months,sales)
# plt.title("Sales Chart")
# plt.xlabel("Months")
# plt.show()



# * Y-axis Label
# - The Y-axis label describes the vertical axis.
# syntax:
# plt.ylabel("Y-axis Name)

# Example:

# import matplotlib.pyplot as plt
# months = [1,2,3,4]
# sales = [25000,30000,35000,40000]
# plt.plot(months,sales)
# plt.title("Sales Chart")
# plt.xlabel("Months")
# plt.ylabel("Sales (₹)")
# plt.show()




# *** grid
# - A grid Display horizontal and vertical lines that help us read values more accurately.

# syntax:
# plt.grid()

# Example:
# import matplotlib.pyplot as plt
# months = [1,2,3,4]
# sales = [25000,30000,35000,40000]
# plt.plot(months,sales)
# plt.title("Sales Chart")
# plt.xlabel("Months")
# plt.ylabel("Sales (₹)")
# plt.grid()
# plt.show()



# Example: Style
# import matplotlib.pyplot as plt
# months = [1,2,3,4]
# sales = [25000,30000,35000,40000]
# plt.plot(months,sales)
# plt.title("Sales Chart")
# plt.xlabel("Months")
# plt.ylabel("Sales (₹)")
# plt.grid(color="orange",linestyle=":")
# plt.show()


# *** legend
# - A legend explains which line represents which dataset.

# syntax:
# plt.legend()

# Example:
# import matplotlib.pyplot as plt

# subjects = [1,2,3,4,5]
# ganesh = [75,80,78,90,88]
# Ram = [70,85,80,86,92]
# Ajay = [69,82,86,79,90]
# plt.plot(subjects,ganesh,label="Ganesh")
# plt.plot(subjects,Ram,label="Ram")
# plt.plot(subjects,Ajay,label="Om")
# plt.legend()
# plt.show()


# Example:

# import matplotlib.pyplot as plt

# days = ["Mon","Tue","Wed","Thu","Fri"]
# attendance = [40,42,39,45,44]
# plt.figure(figsize=(8,5))
# plt.plot(days,attendance,color='red',marker='*',linewidth=2,label='Attendance')
# plt.title("Weekly Student Attendance")
# plt.xlabel("Days")
# plt.ylabel("Number of Students")
# plt.grid()
# plt.legend()
# plt.show()