human_years = float(input("Enter human years: "))

if human_years < 0:
    print("Error: years cannot be negative")
elif human_years <= 2:
    dog_years = human_years * 10.5
    print(f"Dog years: {dog_years}")
else:
    dog_years = 2 * 10.5 + (human_years - 2) * 4
    print(f"Dog years: {dog_years}")
