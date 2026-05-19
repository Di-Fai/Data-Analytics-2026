
# Pandas statistical functions

import pandas as pd

data = {
    "student":["Amy", "Bob", "Cara", "Dan", "Eva"],
    "score":[85, 92, 78, 95, 100]
}

df = pd.DataFrame(data)
print(df)
print()

print("SUM:", df["score"].sum())
print("COUNT:", df["score"].count())
print("MEAN:", df["score"].mean())
print("MEDIAN:", df["score"].median())
print("MIN:", df["score"].min())
print("MAX:", df["score"].max())

print("\nAggregate Results:")
print(df["score"].agg(['sum', 'mean', 'median', 'min', 'max']))