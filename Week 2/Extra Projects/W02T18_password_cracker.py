actual = "MDX123"
guess = input("Enter the password guess: ")

if guess == actual:
    print("Password cracked!")
else:
    matches = sum(1 for a, b in zip(actual, guess) if a == b)
    length = max(len(actual), len(guess))  # extra/missing characters count against the guess
    print(f"{round(matches / length * 100)}% accuracy")
