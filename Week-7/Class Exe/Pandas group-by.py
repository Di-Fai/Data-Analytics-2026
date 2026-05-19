import pandas as pd

data = {
    "Department": ["IT", "HR", "IT", "Sales", "HR", "Sales"],
    "Employee": ["Amy", "Bob", "Cara", "Dan", "Eva", "Frank"],
    "Salary": [70000, 50000, 80000, 60000, 55000, 65000]
}

df = pd.DataFrame(data)
print(df)
print()

# Group by department
grouped = df.groupby("Department")  

print("SUM")
print(grouped["Salary"].sum())

print("\nMEAN")
print(grouped["Salary"].mean())

print("\nCOUNT")
print(grouped["Employee"].count())
