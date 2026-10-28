import pandas as pd

df = pd.read_csv('data/students.csv')

print("Most popular course:")
print(df['Course'].value_counts().idxmax(), df['Course'].value_counts().max())

print("\nTop 3 students by Grade:")
print(df.nlargest(3, 'Grade')[['Name', 'Course', 'Grade']])

df['Result'] = df['Grade'].apply(lambda g: 'Pass' if g >= 60 else 'Fail')
print("\nAverage attendance by result:")
print(df.groupby('Result')['Attendance'].mean().round(1))

corr = df['Attendance'].corr(df['Grade'])
print("\nCorrelation between Attendance and Grade:", round(corr, 3))
# 0.988 is a very strong positive relationship: students who attend more score higher.

report = df.assign(
    passed=df['Grade'] >= 60,
    schol=df['Scholarship'] == 'Yes',
).groupby('Course').agg(
    Student_Count=('Name', 'count'),
    Avg_Grade=('Grade', 'mean'),
    Avg_Attendance=('Attendance', 'mean'),
    Pass_Rate_Pct=('passed', 'mean'),
    Scholarship_Pct=('schol', 'mean'),
)
report['Avg_Grade'] = report['Avg_Grade'].round(1)
report['Avg_Attendance'] = report['Avg_Attendance'].round(1)
report['Pass_Rate_Pct'] = (report['Pass_Rate_Pct'] * 100).round(1)
report['Scholarship_Pct'] = (report['Scholarship_Pct'] * 100).round(1)

report.to_csv('data/eda_report.csv')
print("\nCourse summary:")
print(report)
