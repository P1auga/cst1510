def word_frequency(text):
    clean = text.lower()
    for mark in ['.', ',', '!', '?']:
        clean = clean.replace(mark, '')

    words = clean.split()
    counts = {}

    for word in words:
        counts[word] = counts.get(word, 0) + 1

    print("Top 5 words:")
    for word, count in sorted(counts.items(), key=lambda item: item[1], reverse=True)[:5]:
        print(f"  {word}: {count}")

    return counts


text = """Data science is the study of data. Data scientists use data to find patterns.
Machine learning is a part of data science. Scientists study data every day!
The science of data is growing, and data is everywhere."""

word_frequency(text)

# Extension
from pathlib import Path

with open(Path(__file__).parent / 'data' / 'Les_Brown.txt') as file:
    les_brown = file.read()

word_frequency(les_brown)
