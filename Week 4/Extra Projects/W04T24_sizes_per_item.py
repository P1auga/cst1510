sizes = {}

with open("DATA/clothing_stock.txt") as file:
    for line in file:
        if not line.strip():
            continue
        item, size = [part.strip() for part in line.split(",")]
        sizes.setdefault(item, set()).add(size)

counts = {item: len(size_set) for item, size_set in sizes.items()}
print(counts)
