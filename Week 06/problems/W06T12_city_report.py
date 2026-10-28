import pandas as pd

df = pd.read_csv('data/students.csv')

overall_mean = df['Grade'].mean()

# Pass_Rate from the mean of a boolean per city (groupby.apply is scalar/reindexed in pandas 3.0)
pass_rate = df.assign(passed=df['Grade'] >= 60).groupby('City')['passed'].mean() * 100

report = df.groupby('City').agg(
    Students=('Name', 'count'),
    Avg_Grade=('Grade', 'mean'),
    Avg_Attendance=('Attendance', 'mean'),
).round(1)

report['Pass_Rate'] = pass_rate.round(1)
report['Performance'] = report['Avg_Grade'].apply(
    lambda g: 'Above Average' if g > overall_mean else 'Below Average'
)

report = report.sort_values('Avg_Grade', ascending=False)
report.to_csv('data/city_report.csv', index=False)
print(report)
