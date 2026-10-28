import pandas as pd

df = pd.read_csv('data/students.csv')

bins = [0, 59, 69, 79, 89, 100]
labels = ['F', 'D', 'C', 'B', 'A']
df['Grade_Band'] = pd.cut(df['Grade'], bins=bins, labels=labels)

print(df[['Name', 'Grade', 'Grade_Band']])

print("\nStudents per band:")
print(df['Grade_Band'].value_counts())

top = df[df['Grade_Band'].isin(['A', 'B'])]
print("\nCourse with most A/B students:")
print(top['Course'].value_counts())
