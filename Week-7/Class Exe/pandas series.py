# Exercise: Pandas Series Functions
# This activity creates and explores a Pandas Series using numeric values.

import pandas as pd
import numpy as np

# Create a Pandas Series
data = [10, 20, 30, 20, np.nan]

s = pd.Series(data)

# Display the original Series
print("Original Series:")
print(s)

print("\nSum:")
print(s.sum())

print("\nMean:")
print(s.mean())

print("\nMaximum value:")
print(s.max())

print("\nMinimum value:")
print(s.min())

print("\nFirst three values:")
print(s.head(3))

print("\nCheck for missing values:")
print(s.isnull())

print("\nReplace missing values with 0:")
print(s.fillna(0))

print("\nSorted values:")
print(s.sort_values())

print("\nCount repeated values:")
print(s.value_counts())