"""Coffee Machine - nested dicts, checked by functions."""

MENU = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0},
}

resources = {"water": 300, "milk": 200, "coffee": 100}


def report(resources):
    """Print the current levels of everything the machine holds."""
    for item, amount in resources.items():
        print(f"{item}: {amount}")


def enough(resources, drink):
    """Return True if every ingredient for drink is in stock."""
    for item, needed in MENU[drink]["ingredients"].items():
        if resources.get(item, 0) < needed:
            print(f"Sorry, not enough {item}.")
            return False
    return True


def make(resources, drink):
    """Deduct the ingredients and return the money taken."""
    for item, needed in MENU[drink]["ingredients"].items():
        resources[item] -= needed

    coins = float(input("Please insert coins (just a number): $"))

    if coins < MENU[drink]["cost"]:
        print("Sorry, that's not enough money. Money refunded.")
        return 0.0

    change = coins - MENU[drink]["cost"]
    if change > 0:
        print(f"Here is ${change:.2f} in change.")

    return MENU[drink]["cost"]


def coffee_machine():
    """Run the machine until the user types 'off'."""
    takings = 0.0

    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()

        if choice == "off":
            return takings
        elif choice == "report":
            report(resources)
        elif choice in MENU:
            if enough(resources, choice):
                takings += make(resources, choice)
                print(f"Here is your {choice}. Enjoy!")
        else:
            print("That drink is not on the menu.")


print(f"Machine turned off. Total taken: ${coffee_machine():.2f}")
