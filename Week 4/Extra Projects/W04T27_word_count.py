import re

with open("DATA/Les_Brown.txt") as file:
    text = file.read()

words = re.findall(r"[a-z]+", text.lower())

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

with open("word_count.txt", "w") as file:
    for word, count in counts.items():
        file.write(f"{word}: {count}\n")

print("Unique words:", len(counts))
