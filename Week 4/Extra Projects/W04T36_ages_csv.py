people = []
with open("DATA/ages.csv") as file:
    next(file)              # skip header
    for line in file:
        name, age = line.strip().split(",")
        people.append((name, int(age)))

oldest = max(people, key=lambda person: person[1])
youngest = min(people, key=lambda person: person[1])
average = sum(age for _, age in people) / len(people)

print("Oldest:", oldest[0], oldest[1])
print("Youngest:", youngest[0], youngest[1])
print("Average age:", average)

with open("adults.txt", "w") as file:
    for name, age in people:
        if age > 20:
            file.write(f"{name}: {age}\n")
