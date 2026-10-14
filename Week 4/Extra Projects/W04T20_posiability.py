with open("DATA/Les_Brown.txt") as file:
    text = file.read()

resonates = "It is possible"
updated = text.replace(resonates, resonates.upper())

with open("posiability.txt", "w") as file:
    file.write(updated)

print("Replaced occurrences:", text.count(resonates))
