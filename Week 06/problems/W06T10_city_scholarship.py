import pandas as pd

df = pd.read_csv('data/students.csv')

print("Students per city:")
print(df.groupby('City')['Name'].count())

print("\nAverage grade per city (highest first):")
print(df.groupby('City')['Grade'].mean().round(1).sort_values(ascending=False))

print("\nAverage grade by scholarship:")
print(df.groupby('Scholarship')['Grade'].mean().round(1))

print("\nStudents per city and scholarship:")
print(df.groupby(['City', 'Scholarship'])['Name'].count())

scholars = df[df['Scholarship'] == 'Yes'].groupby('City')['Name'].count()
print("\nCity with most scholarship students:", scholars.idxmax(), scholars.max())
