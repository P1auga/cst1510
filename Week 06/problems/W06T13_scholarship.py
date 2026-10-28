import pandas as pd

df = pd.read_csv('data/students.csv')

sch = df[df['Scholarship'] == 'Yes']
print("Percentage with a scholarship:", round(len(sch) / len(df) * 100, 1))

print("\nAverage grade by scholarship:")
print(df.groupby('Scholarship')['Grade'].mean().round(1))

by_course = df.assign(schol=df['Scholarship'] == 'Yes').groupby('Course').agg(
    Total=('Name', 'count'),
    With_Scholarship=('schol', 'sum'),
)
by_course['Scholarship_Rate'] = (by_course['With_Scholarship'] / by_course['Total'] * 100).round(1)
print("\nScholarship rate per course:")
print(by_course.sort_values('Scholarship_Rate', ascending=False))

print("\nAverage attendance by scholarship:")
print(df.groupby('Scholarship')['Attendance'].mean().round(1))

# Findings: 40% of students hold a scholarship, and they clearly do better on
# average (86.1 vs 69.5 for non-scholarship students), so awards do go to stronger
# students. Scholarship students also attend more (90.1 vs 75.5). Rates differ a lot
# per course, from 66.7% in Mathematics down to 16.7% in Data Science. So on this
# data the scholarship is a good marker of both grade and attendance.
