items = ["Milk", "Bread", "Eggs", "Rice", "Apples"]

with open("shopping.txt", "w") as file:
    for item in items:
        file.write(item + "\n")

with open("shopping.txt") as file:
    shopping = [line.strip() for line in file]

for item in shopping:
    print("You need to buy:", item)
print("Total items:", len(shopping))
