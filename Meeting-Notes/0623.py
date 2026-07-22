import pandas as pd

student_data = {
 "Name":["Soham","Amit","Priya","Sneha","Rahul"],
  "Age":[21,22,20,23,24],
  "Marks":[85,90,95,80,70],
   "City":["Pune","Mumbai","Nashik","Delhi","Pune"]
}

df = pd.DataFrame(student_data)

# print(df)

# df.head()
# df.head(3)

# df.tail()
# df.tail(2)

# df.shape

# df.columns

# df.info()

# df.describe()

# df["Name"]

# df["Marks"]

# df[["Name","City"]]

# df[df["Marks"]>=90]

# df[df["City"]=="Pune"]


# df[(df["Marks"]>=90) & (df["City"]=="Pune")]


# df[(df["Marks"]>=90) | (df["City"]=="Pune")]