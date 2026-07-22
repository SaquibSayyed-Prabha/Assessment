# Topic: figure Management(figsize,tight_layout(),savefig(),DPI)


# What is figure Management?
# -> figure Management refers to controlling the appearance and layout of an entire figure.
# It Includes:
# figure size
# Spacing
# Resolution
# Saving Charts
# Layout Adjustment


# figure size (figsize)
# - figsize changes the width and height of the figure.

# Syntax:
# plt.figure(figsize=(width,height))
# width -> inches
# height -> inches


# Example:

# import matplotlib.pyplot as plt

# plt.figure(figsize=(10,5))

# plt.plot([1,2,3,4],[10,20,15,30])

# plt.title("Sales Report")

# plt.show()




# * What is tight_layout()?
# -> tight_layout() automatically Adjusts spacing between subplots.
# It Prevents:
# - Overlapping titles
# - Overlapping Labels
# - Hidden axes


# Syntax:
# plt.tight_layout()


# Example:

# import matplotlib.pyplot as plt

# plt.figure(figsize=(8,5))

# plt.subplot(1,2,1)

# plt.plot([1,2,3],[10,20,30])

# plt.title("Line Chart")

# plt.subplot(1,2,2)

# plt.bar(["A","B","C"],[20,35,25])

# plt.title("Bar Chart")

# plt.tight_layout()

# plt.show()


# ** savefig()
# - savefig() saves the current figure as an image or document file.

# Why use savefig()?
# - It allows you to: save reports,share charts with others,print graphs.

# Syntax:
# plt.savefig("filename.png")


# Example: Save as PNG 

# import matplotlib.pyplot as plt

# plt.figure(figsize=(10,5))

# plt.plot([1,2,3,4],[10,20,15,30])

# plt.title("Student Report")

# plt.savefig("student_report.png")

# plt.show()



# Example: Save as JPG

# import matplotlib.pyplot as plt

# plt.figure(figsize=(10,5))

# plt.plot([1,2,3,4],[10,20,15,30])

# plt.title("Student Report")

# plt.savefig("student_report1.jpg")

# plt.show()


# Example: Save as PDF

# import matplotlib.pyplot as plt

# plt.figure(figsize=(10,5))

# plt.plot([1,2,3,4],[10,20,15,30])

# plt.title("Student Report")

# plt.savefig("student_report1.pdf")

# plt.show()



# * What is DPI?
# -> DPI stands for Dots Per Inch.
# It determines the image quality(resolution).

# Higher DPI = Better quality


# Common DPI values:
# DPI         values
# 72          Low
# 100         Standard
# 150         Good
# 300         High(Print quality)

# Syntax:

# plt.savefig("chart.png",dpi=300)


# Example:

# import matplotlib.pyplot as plt

# plt.figure(figsize=(10,5))

# plt.bar([1,2,3,4],[10,20,15,30])

# plt.title("Student Report")

# plt.savefig("student_bar_report.png",dpi=300)

# plt.show()


# *** Styles

# - A Style is a predefined design that changes the appearance of a chart without Changing
#   the data.

# Styles automatically modify:
# background color
# grid style
# Font style
# line colors
# marker colors
# overall theme




# * Viewing Available Styles

# Syntax:

# print(plt.style.available)

# Example:

# import matplotlib.pyplot as plt

# print(plt.style.available)




# Applying a Styles:

# Syntax:

# plt.style.use("style_name")


# ggplot style:
# - The ggplot style is inspired by the R ggplot2 library.
# It provides:
# - Light gray background
# - White grid lines
# - Attractive colors
# - Professional appearance

# Style:

# plt.style.use("ggplot")


# Example:

# import matplotlib.pyplot as plt

# plt.figure(figsize=(10,5))
# plt.style.use("ggplot")
# plt.plot([1,2,3,4],[10,20,15,30],marker="o")

# plt.title("Student Report")

# plt.savefig("student_report.png")

# plt.show()



# * dark_background

# Syntax:

# plt.style.use("dark_background")

# Example:
# import matplotlib.pyplot as plt

# plt.figure(figsize=(10,5))
# plt.style.use("dark_background")
# plt.bar([1,2,3,4],[10,20,15,30])

# plt.title("Student Report")

# plt.show()


# Example:

# import matplotlib.pyplot as plt
# plt.style.use("classic")
# plt.figure(figsize=(10,5))

# plt.plot([1,2,3,4],[10,20,15,30])

# plt.title("Sales Report")
# plt.show()