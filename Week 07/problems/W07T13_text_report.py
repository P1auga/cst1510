STOPWORDS = ['the', 'a', 'is', 'and', 'of', 'to', 'in']


def text_report(text):
    clean = text.lower()
    for mark in ['.', ',', '!', '?', ';', ':']:
        clean = clean.replace(mark, '')

    words = clean.split()
    sentences = sum(text.count(mark) for mark in ['.', '!', '?'])
    avg_length = sum(len(word) for word in words) / len(words)

    print("=" * 50)
    print("TEXT REPORT".center(50))
    print("=" * 50)
    print("Total characters:".ljust(25), len(text))
    print("Total words:".ljust(25), len(words))
    print("Total sentences:".ljust(25), sentences)
    print("Average word length:".ljust(25), round(avg_length, 2))

    counts = {
        "uppercase": sum(1 for char in text if char.isupper()),
        "lowercase": sum(1 for char in text if char.islower()),
        "digits": sum(1 for char in text if char.isdigit()),
        "spaces": sum(1 for char in text if char.isspace()),
    }
    counts["punctuation"] = len(text) - sum(
        [counts["uppercase"], counts["lowercase"], counts["digits"], counts["spaces"]]
    )

    print("-" * 50)
    print("Character breakdown")
    for key, value in counts.items():
        print(key.ljust(25), value)

    frequencies = {}
    for word in words:
        if word not in STOPWORDS:
            frequencies[word] = frequencies.get(word, 0) + 1

    top5 = sorted(frequencies.items(), key=lambda item: item[1], reverse=True)[:5]
    print("-" * 50)
    print("Top 5 words")
    for word, count in top5:
        print(word.ljust(25), count)

    longest = max(words, key=len)
    shortest = min(words, key=len)
    print("-" * 50)
    print("Longest word:".ljust(25), longest)
    print("Shortest word:".ljust(25), shortest)
    print("=" * 50)


corpus = """Artificial Intelligence is transforming every industry. From healthcare to finance,
AI systems are making decisions that affect millions of people. Machine Learning,
a subset of AI, enables computers to learn from data without being explicitly programmed.
Deep Learning takes this further with neural networks inspired by the human brain.
In 2024, Large Language Models like GPT have shown remarkable abilities in understanding
and generating human language. The future of AI is both exciting and challenging."""

text_report(corpus)

# Extension
from pathlib import Path

with open(Path(__file__).parent / 'data' / 'python_zen.txt') as file:
    zen = file.read()

text_report(zen)
