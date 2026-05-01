import pandas as pd

df = pd.read_csv("data.csv")

print("Average Scores:")
print(df.mean(numeric_only=True))

print("\nTop Student:")
print(df.loc[df["Math"].idxmax()])

print("\nLowest Student:")
print(df.loc[df["Math"].idxmin()])
