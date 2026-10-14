with open("my_profile.txt", "w") as file:
    file.write("Alex\n")
    file.write("20\n")
    file.write("Blue\n")

with open("my_profile.txt") as file:
    name, age, color = [line.strip() for line in file]

print("Name:", name)
print("Age:", age)
print("Favorite Color:", color)
