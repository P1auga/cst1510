import pandas as pd

df = pd.read_csv('data/students.csv')

stats = df.groupby('Course').agg(
    Count=('Name', 'count'),
    Avg_Grade=('Grade', 'mean'),
    Max_Grade=('Grade', 'max'),
    Avg_Attendance=('Attendance', 'mean'),
).round(1)

stats = stats.sort_values('Avg_Grade', ascending=False)
print(stats)
