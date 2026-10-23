"""Higher or Lower - guess which account has more followers, until you quit."""

a_name, a_followers = "hits_logs", 1200
b_name, b_followers = "srv_notes", 3400

keep_playing = True

while keep_playing:
    print(f"\nA: {a_name}   B: {b_name}")
    guess = input("Who has more followers? Type 'A' or 'B', or 'quit': ").strip().lower()

    if guess == "quit":
        keep_playing = False
    elif guess == "a":
        print("Correct" if a_followers > b_followers else "Wrong")
    elif guess == "b":
        print("Correct" if b_followers > a_followers else "Wrong")
    else:
        print("Not a valid choice.")

print("Thanks for playing.")
