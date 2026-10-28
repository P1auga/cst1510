import pandas as pd

df = pd.read_csv('data/students.csv')

df['Result'] = df['Grade'].apply(lambda g: 'Pass' if g >= 60 else 'Fail')
df['Combined_Score'] = (df['Grade'] * 0.7 + df['Attendance'] * 0.3).round(1)

print(df[['Name', 'Grade', 'Attendance', 'Result', 'Combined_Score']].head(10))

print("\nPass / Fail counts:")
print(df['Result'].value_counts())
