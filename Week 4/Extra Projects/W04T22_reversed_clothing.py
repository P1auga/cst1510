with open("DATA/clothing_stock.txt") as file:
    items = [line.strip() for line in file if line.strip()]

items.reverse()

with open("reversed_clothing_stock.txt", "w") as file:
    for item in items:
        file.write(item + "\n")

print("Reversed items:", len(items))
