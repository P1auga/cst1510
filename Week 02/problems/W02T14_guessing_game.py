from random import randint

secret = randint(1, 100)
tries = 0

while True:
    try:
        guess = input("Guess the number (or 'quit'): ")
    except EOFError:
        print(f"The number was {secret}. Tries: {tries}")
        break

    if guess.strip().lower() == "quit":
        print(f"The number was {secret}. Tries: {tries}")
        break

    try:
        guess = int(guess)
    except ValueError:
        print("That is not a number.")
        continue

    tries += 1

    if guess < secret:
        print("Too small")
    elif guess > secret:
        print("Too large")
    else:
        print(f"Correct! You needed {tries} tries")
        break
