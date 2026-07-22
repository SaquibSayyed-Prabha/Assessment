import pandas as pd

data = {
  "Name":["Jay","Amit","Jay","Sneha","Rahul"],
    "Age":[21,None,21,23,None],
    "Marks":[85,90,85,80,70]
}

df = pd.DataFrame(data)

# print(df)

# print(df.isnull())

# df.isnull().sum()

# df.notnull()

# df.fillna(0)

# avg_age = df["Age"].mean()
# df["Age"] = df["Age"].fillna(avg_age)
# print(df)


# df.dropna()

# print(df.duplicated())

# df.drop_duplicates()