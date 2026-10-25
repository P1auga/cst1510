"""Banker Roulette - pick who pays, two ways."""

import random

friends = ["Alice", "Bob", "Charlie", "Dana", "Eve"]

print(random.choice(friends))

index = random.randint(0, len(friends) - 1)
print(friends[index])
