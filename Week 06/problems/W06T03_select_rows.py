import pandas as pd

df = pd.read_csv('data/students.csv')

grades_df = df[['Name', 'Course', 'Grade']]
print("First 8 rows of grades_df:")
print(grades_df.head(8))

print("\nRows 5 to 9 (iloc):")
print(df.iloc[5:10])

print("\nStudent at index 3 (loc):")
print(df.loc[3, ['Name', 'City']])
