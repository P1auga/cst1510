while True:
    try:
        number = int(input("Enter a whole number: "))
        break
    except ValueError:
        print("That is not a whole number, try again.")

print("Squared:", number ** 2)
