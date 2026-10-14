import re

with open("DATA/Les_Brown.txt") as file:
    text = file.read()

# the source hard-wraps lines that often cut a word in half (yo/u, say/s),
# so rebuild the words before sentence splitting
text = re.sub(r"(\w)\n(\w)", r"\1\2", text)
text = re.sub(r"\s+", " ", text)
text = text.replace("â€TM", "'")

sentences = re.split(r"(?<=[.!?])\s+", text)

dreams = [sentence.strip() for sentence in sentences
          if sentence.strip() and "dream" in sentence.lower()]

with open("dream_sentences.txt", "w") as file:
    for sentence in dreams:
        file.write(sentence + "\n")

print("Dream sentences written:", len(dreams))
