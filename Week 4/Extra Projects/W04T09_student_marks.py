marks = [55, 82, 47, 91, 63, 38, 76]

print("Marks:", marks)
print("Average mark:", sum(marks) / len(marks))
print("Highest mark:", max(marks))
print("Lowest mark:", min(marks))

passed = [mark for mark in marks if mark >= 50]
print("Passed:", len(passed))
print("Failed:", len(marks) - len(passed))
