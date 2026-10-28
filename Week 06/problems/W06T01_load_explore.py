import pandas as pd

df = pd.read_csv('data/students.csv')

print("First 5 rows:")
print(df.head())

print("\nLast 3 rows:")
print(df.tail(3))

print("\nShape:", df.shape)

print("Columns:", df.columns.tolist())
