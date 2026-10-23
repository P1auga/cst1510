"""Number Guessing Game - hard-coded secret, counts the guesses."""

SECRET = 37

guesses = 0

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    guesses += 1

    if guess > SECRET:
        print("Too high.")
    elif guess < SECRET:
        print("Too low.")
    else:
        print(f"You got it in {guesses} guesses.")
        break
