# ID,Name,Gender,Course,Marks,Attendance
# 101,Rahul,Male,Python,85,92
# 102,Priya,Female,Python,78,88
# 103,Amit,Male,Python,92,96
# 104,Sneha,Female,Python,65,81
# 105,Sopan,Male,Python,74,85
# 106,Pooja,Female,Python,89,94
# 107,Karan,Male,Python,58,72
# 108,Anjali,Female,Python,95,98
# 109,Vikas,Male,Python,69,80
# 110,Neha,Female,Python,82,90
# 111,Arjun,Male,Python,77,87
# 112,Kavya,Female,Python,91,95
# 113,Sameer,Male,Python,55,70
# 114,Meera,Female,Python,73,84
# 115,Akash,Male,Python,88,93



# import pandas as pd
# import matplotlib.pyplot as plt

# # Load Dataset
# df = pd.read_csv("students.csv")

# print("Student Dataset")
# print(df)

# # -------------------------------
# # 1. Bar Chart - Marks
# # -------------------------------

# plt.figure(figsize=(10,5))
# plt.bar(df["Name"], df["Marks"])
# plt.title("Student Marks")
# plt.xlabel("Students")
# plt.ylabel("Marks")
# plt.xticks(rotation=45)
# plt.grid(axis='y')
# plt.show()

# # -------------------------------
# # 2. Pie Chart - Gender
# # -------------------------------

# gender = df["Gender"].value_counts()

# plt.figure(figsize=(6,6))
# plt.pie(gender,
#         labels=gender.index,
#         autopct="%1.1f%%",
#         startangle=90)

# plt.title("Gender Distribution")
# plt.show()

# # -------------------------------
# # 3. Histogram - Marks
# # -------------------------------

# plt.figure(figsize=(8,5))
# plt.hist(df["Marks"], bins=5)
# plt.title("Marks Distribution")
# plt.xlabel("Marks")
# plt.ylabel("Number of Students")
# plt.grid()
# plt.show()

# # -------------------------------
# # 4. Line Chart
# # -------------------------------

# plt.figure(figsize=(10,5))
# plt.plot(df["Name"], df["Attendance"], marker='o')
# plt.title("Attendance of Students")
# plt.xlabel("Students")
# plt.ylabel("Attendance (%)")
# plt.xticks(rotation=45)
# plt.grid()
# plt.show()

# # -------------------------------
# # 5. Scatter Plot
# # -------------------------------

# plt.figure(figsize=(8,5))
# plt.scatter(df["Attendance"], df["Marks"])
# plt.title("Attendance vs Marks")
# plt.xlabel("Attendance")
# plt.ylabel("Marks")
# plt.grid()
# plt.show()

# # -------------------------------
# # Statistics
# # -------------------------------

# print("\nAverage Marks :", df["Marks"].mean())
# print("Highest Marks :", df["Marks"].max())
# print("Lowest Marks :", df["Marks"].min())

# topper = df[df["Marks"] == df["Marks"].max()]

# print("\nTopper")
# print(topper)

