import pandas as pd

df = pd.read_csv('data/students.csv')

london = df[df['City'] == 'London']
print("Students in London:", len(london))
print(london)

print("\nStudents with Grade below 65:")
print(df.loc[df['Grade'] < 65, ['Name', 'Grade']])

print("\nStudents per city:")
print(df['City'].value_counts())
