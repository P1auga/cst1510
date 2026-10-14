student_data = [
    [101, 'Alice', 85, 92, 88],
    [102, 'Bob', 78, 81, 75],
    [103, 'Charlie', 90, 85, 89],
    [104, 'David', 65, 70, 72],
    [105, 'Eve', 88, 95, 90]
]

for student in student_data:
    student.append(round(sum(student[2:5]) / 3, 2))

averages = [student[5] for student in student_data]
print("Highest average:", max(averages))
print("Lowest average:", min(averages))

print("Above 75 in all subjects:")
for student in student_data:
    if all(score > 75 for score in student[2:5]):
        print(" ", student[1])
