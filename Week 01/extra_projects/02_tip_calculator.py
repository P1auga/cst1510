"""Tip Calculator - split a bill and a tip between any number of people."""

bill = float(input("What was the total bill? $"))
people = int(input("How many people are splitting it? "))
tip_percent = float(input("What percentage tip would you like to give? "))

each = (bill / people) * (1 + tip_percent / 100)

print(f"Each person should pay: ${each:.2f}")
