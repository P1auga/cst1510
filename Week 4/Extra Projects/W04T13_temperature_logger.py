with open("temps.txt", "w") as file:
    for day in range(1, 6):
        temp = int(input(f"Temperature for day {day}: "))
        file.write(f"Day {day}: {temp}\u00b0C\n")

total = 0
count = 0
with open("temps.txt") as file:
    for line in file:
        total += int(line.split(":")[1].strip().rstrip("\u00b0C"))
        count += 1

print("Average temperature:", total / count)
