"""Treasure Island - a nested if/else choose-your-own-adventure."""

print("Welcome to Treasure Island. Your mission is to find the treasure.")

direction = input('You are at a crossroad. Where do you want to go? "left" or "right": ').strip().lower()

if direction == "left":
    action = input('You come to a lake. "wait" for a boat, or "swim" across? ').strip().lower()

    if action == "wait":
        door = input('You arrive at a house with three doors. "red", "yellow" or "blue"? ').strip().lower()

        if door == "yellow":
            print("You found the treasure. You win!")
        elif door == "red":
            print("Burned by fire. Game over.")
        elif door == "blue":
            print("Eaten by beasts. Game over.")
        else:
            print("That door does not exist. Game over.")
    else:
        print("Attacked by a trout. Game over.")
else:
    print("Fell into a hole. Game over.")
