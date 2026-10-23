"""Python Pizza - size, pepperoni and extra cheese."""

size = input("What size pizza would you like? S, M or L: ").strip().upper()
pepperoni = input("Do you want pepperoni? Y or N: ").strip().upper()
cheese = input("Do you want extra cheese? Y or N: ").strip().upper()

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print(f"{size} is not a size we sell.")
    raise SystemExit

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
