count = int(input("Enter the number of students: "))

highest = -1
second = -1

for i in range(count):
    score = float(input("Enter the score: "))
    if score > highest:
        second = highest
        highest = score
    elif score > second:
        second = score

print(f"Highest score: {highest:g}")
print(f"Second highest score: {second:g}")
