"""Hangman - reveal letters of a random word, six lives."""

import random

WORD_LIST = ["server", "python", "network", "backup", "monitor"]

chosen_word = random.choice(WORD_LIST)

placeholder = ["_" for _ in chosen_word]
lives = 6
guessed = set()

print(" ".join(placeholder))

while "_" in placeholder and lives > 0:
    guess = input("Guess a letter: ").strip().lower()

    if len(guess) != 1 or not guess.isalpha():
        print("One letter at a time.")
        continue

    if guess in guessed:
        print(f"You already guessed {guess}.")
        continue

    guessed.add(guess)

    if guess in chosen_word:
        for position, letter in enumerate(chosen_word):
            if letter == guess:
                placeholder[position] = guess
    else:
        lives -= 1
        print(f"{guess} is not in the word. Lives left: {lives}")

    print(" ".join(placeholder))

if "_" not in placeholder:
    print("You win!")
else:
    print(f"You lose. The word was {chosen_word}.")
