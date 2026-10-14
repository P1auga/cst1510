by_size = {}

with open("DATA/clothing_stock.txt") as file:
    for line in file:
        if not line.strip():
            continue
        item, size = [part.strip() for part in line.split(",")]
        by_size.setdefault(size, set()).add(item)

for size, items in sorted(by_size.items()):
    print(size, items)
