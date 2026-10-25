"""Password Generator - letters, symbols and numbers, shuffled."""

import random

letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
symbols = list("!#$%&()*+")
numbers = list("0123456789")

n_letters = int(input("How many letters would you like? "))
n_symbols = int(input("How many symbols would you like? "))
n_numbers = int(input("How many numbers would you like? "))

password_list = []

for _ in range(n_letters):
    password_list.append(random.choice(letters))

for _ in range(n_symbols):
    password_list.append(random.choice(symbols))

for _ in range(n_numbers):
    password_list.append(random.choice(numbers))

# Shuffling before joining keeps the character types from clustering.
random.shuffle(password_list)

print("".join(password_list))
