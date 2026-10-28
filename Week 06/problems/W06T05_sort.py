import pandas as pd

df = pd.read_csv('data/students.csv')

print("Top 5 by Grade:")
print(df.sort_values('Grade', ascending=False).head())

print("\nSorted by City (A-Z) then Grade (low to high):")
print(df.sort_values(['City', 'Grade'], ascending=[True, True]).head(10))
