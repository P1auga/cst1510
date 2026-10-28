import pandas as pd

df = pd.read_csv('data/students_missing.csv')

print("Missing values per column:")
print(df.isnull().sum())

print("\nRows with at least one missing value:")
print(df[df.isnull().any(axis=1)])

df['Grade'] = df['Grade'].fillna(round(df['Grade'].mean(), 1))
df['Scholarship'] = df['Scholarship'].fillna('Unknown')
df['Course'] = df['Course'].fillna('Unknown')
df = df.dropna(subset=['Attendance', 'Age'])

print("\nMissing values after cleaning:")
print(df.isnull().sum())

df.to_csv('data/students_clean.csv', index=False)
