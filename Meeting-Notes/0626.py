import pandas as pd

emp = {
    "Name":["Suraj","Amit","Priya","Sneha","Rahul","Pooja"],
    "Department":["IT","HR","IT","HR","Finance","IT"],
    "Salary":[50000,40000,55000,45000,60000,52000],
    "Age":[21,22,20,23,24,22]
}

df = pd.DataFrame(emp)
# print(df)

# print(df.sort_values("Salary"))
# df.sort_values("Age")

# df.sort_values("Salary",ascending=False)

# df.sort_values(["Department","Salary"])

# print(df["Department"].unique())

# df["Department"].value_counts()

# df.groupby("Department")["Salary"].sum()

# df.groupby("Department")["Salary"].mean()


# df.groupby("Department")["Salary"].min()
# df.groupby("Department")["Salary"].max()

# df.groupby("Department")["Name"].count()

# print(df.groupby("Department")["Salary"].agg(["sum","mean","min","max","count"]))