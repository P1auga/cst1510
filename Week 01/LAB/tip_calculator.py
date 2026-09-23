# Ed's Tip Calculator

print("Welcome to Ed's Tip Calculator.")
bill = float(input("Total Bill: £"))
people = int(input("Number of People: "))
tip_percent = float(input("What percentage tip would you like to give? (e.g. 10, 12, 15): "))

total_with_tip = bill * (1 + tip_percent / 100)
per_person = total_with_tip / people

print(f"Each person should pay: £{per_person:.2f}")