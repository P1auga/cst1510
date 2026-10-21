count = int(input("Enter the number of students: "))

top_name = ""
top_score = -1

for i in range(count):
    name = input("Enter a student name: ")
    score = float(input("Enter the score: "))
    if score > top_score:
        top_score = score
        top_name = name

print(f"{top_name} has the highest score: {top_score:g}")
