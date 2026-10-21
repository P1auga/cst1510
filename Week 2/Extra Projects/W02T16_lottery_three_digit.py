from random import randint

lottery = randint(100, 999)
guess = int(input("Enter a three-digit number: "))

if guess == lottery:
    award = 10000
elif sorted(str(guess)) == sorted(str(lottery)):
    award = 3000
elif set(str(guess)) & set(str(lottery)):
    award = 1000
else:
    award = 0

print(f"Lottery number: {lottery}")
if award:
    print(f"You won £{award:,}")
else:
    print("No award")
