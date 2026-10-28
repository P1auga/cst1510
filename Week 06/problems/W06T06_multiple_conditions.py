import pandas as pd

df = pd.read_csv('data/students.csv')

mask = (
    df['Course'].isin(['Computer Science', 'Data Science'])
    & (df['Grade'] > 75)
    & (df['Attendance'] > 80)
)
print("Computer Science / Data Science, Grade > 75, Attendance > 80:")
print(df.loc[mask, ['Name', 'Course', 'Grade', 'Attendance']])

print("\nAt risk of failing (Grade < 60):")
print(df.loc[df['Grade'] < 60, ['Name', 'Grade']])

print("\nScholarship students from Manchester with Grade > 80:")
manc = (df['City'] == 'Manchester') & (df['Scholarship'] == 'Yes') & (df['Grade'] > 80)
print(df.loc[manc, ['Name', 'Grade', 'Scholarship']])
