with open("DATA/python_zen.txt") as file:
    lines = file.readlines()

with open("numbered_zen.txt", "w") as file:
    file.write(lines[0])
    for number, line in enumerate(lines[1:], start=1):
        file.write(f"{number}. {line}")

print("Wrote", len(lines) - 1, "numbered lines")
