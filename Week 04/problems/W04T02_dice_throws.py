import random

throws = [random.randint(1, 6) for _ in range(7)]
random.shuffle(throws)
print("Shuffled:", throws)

throws.sort(reverse=True)
print("Descending:", throws)

for value in sorted(set(throws)):
    print(f"{value} occurred {throws.count(value)} times")
