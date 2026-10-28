import pandas as pd

df = pd.read_csv('data/students.csv')

print("Data types:")
print(df.dtypes)

print("\nSummary statistics:")
print(df.describe())

print("\nAverage grade:", round(df['Grade'].mean(), 1))
print("Maximum attendance:", df['Attendance'].max())
print("Youngest student's age:", df['Age'].min())
