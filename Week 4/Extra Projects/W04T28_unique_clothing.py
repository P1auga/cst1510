with open("DATA/clothing_stock.txt") as file:
    items = [line.strip() for line in file if line.strip()]

unique = set(items)

with open("unique_clothing_stock.txt", "w") as file:
    for item in sorted(unique):
        file.write(item + "\n")

print("Unique entries:", len(unique))
