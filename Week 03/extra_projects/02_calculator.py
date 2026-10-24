"""Calculator - one function per operation, chained through a loop."""


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculate(n1, operator, n2):
    """Call the matching function and return its result."""
    if operator == "+":
        return add(n1, n2)
    elif operator == "-":
        return subtract(n1, n2)
    elif operator == "*":
        return multiply(n1, n2)
    elif operator == "/":
        return divide(n1, n2)
    else:
        return None


n1 = float(input("What's the first number? "))

keep_going = True

while keep_going:
    operator = input("Pick an operation (+ - * /): ").strip()

    if operator not in ("+", "-", "*", "/"):
        print("Pick one of + - * /")
        continue

    n2 = float(input("What's the next number? "))

    result = calculate(n1, operator, n2)

    print(f"{n1} {operator} {n2} = {result}")

    choice = input(f"Type 'y' to continue with {result}, or 'n' to start over: ").strip().lower()

    if choice == "y":
        n1 = result
    else:
        n1 = float(input("What's the first number? "))
