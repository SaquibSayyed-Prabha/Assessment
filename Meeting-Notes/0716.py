# Project Name
# Employee Salary Analysis using NumPy


# Scenario
# A company has information about 10 employees.
# Each employee has:
# Employee ID
# Age
# Experience (Years)
# Monthly Salary
# Performance Rating
# The HR department wants to analyze the employee data before making promotion decisions.





# # Employee Salary Analysis using NumPy

# import numpy as np

# emp_data = np.array([
#     [101,25,2,25000,3],
#     [102,28,4,32000,4],
#     [103,30,5,40000,5],
#     [104,24,1,22000,2],
#     [105,35,8,60000,5],
#     [106,29,6,45000,4],
#     [107,40,10,70000,5],
#     [108,27,3,30000,3],
#     [109,32,7,52000,4],
#     [110,26,2,28000,3]
# ])

# print("All Data Set:")
# print(emp_data)

# print("Display Employee Salaries:")
# salary = emp_data[:,3]
# print(salary)

# print("Statistical Analysis:")

# print("Total Salary:",np.sum(salary))

# print("Average Salary:",np.mean(salary))

# print("Highest Salary:",np.max(salary))

# print("Lowest Salary:",np.min(salary))

# print("Standard Deviation:",np.std(salary))

# print("Variance:",np.var(salary))


# # Employee Age Analysis

# print("Employee Age Analysis:")
# age = emp_data[:,1]
# # print(age)
# print("Average Age:",np.mean(age))
# print("Maximum Age:",np.max(age))
# print("Minmum Age:",np.min(age))


# # Experience Analysis
# print("Experience Analysis:")
# exp = emp_data[:,2]
# print("Average Experience:",np.mean(exp))
# print("Maximum Exp:",np.max(exp))

# # Sort Employee Salaries
# print("Sort Employee Salaries:")
# print(np.sort(salary))

# # Search Salary
# print("Search Salary:")
# # Find Salary 45000
# print(np.where(salary==45000))

# print("Unique Performance Ratings:")
# rating = emp_data[:,4]
# # print(rating)
# print(np.unique(rating))

# print("Salary Increment Using Broadcasting:")
# # Increase every salary by Rs 5000.
# new_salary = salary + 5000
# print(new_salary)

# print("employee with salary greater than Rs 40000.:")
# print(emp_data[salary>40000])


# Pending Work:
# Employees with Salary Greater Than ₹40,000
# Employees with Experience Greater Than 5 Years
# Add Missing Salary
# Replace Missing Salary
# Generate Random Employee Bonus
# Final Salary
# Prepare Feature Matrix (X)
# Prepare Target Variable (y)
# Final Dataset