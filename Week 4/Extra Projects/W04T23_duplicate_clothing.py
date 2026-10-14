seen = set()
duplicates = set()

with open("DATA/clothing_stock.txt") as file:
    for line in file:
        item = line.strip()
        if not item:
            continue
        if item in seen:
            duplicates.add(item)
        seen.add(item)

if duplicates:
    for item in sorted(duplicates):
        print("Duplicate:", item)
else:
    print("No duplicates found")
