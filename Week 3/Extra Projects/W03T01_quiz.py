import random


def division(a, b):
    if b == 0:
        raise ZeroDivisionError("cannot divide by zero")
    return a / b


def remainder(a, b):
    if b == 0:
        raise ZeroDivisionError("cannot take the remainder by zero")
    return a % b


MENU = {
    "1": ("Addition", "+", lambda a, b: a + b),
    "2": ("Subtraction", "-", lambda a, b: a - b),
    "3": ("Multiplication", "*", lambda a, b: a * b),
    "4": ("Division", "/", None),
    "5": ("Exponent", "**", lambda a, b: a ** b),
    "6": ("Remainder", "%", remainder),
}


def ask_question(symbol, answer):
    try:
        guess = input(f"What is the answer? ")
        if guess.strip() == "":
            return False
        if symbol == "/":
            return abs(float(guess) - answer) < 1e-9
        return int(guess) == answer
    except ValueError:
        print("That is not a number.")
        return False


def main():
    score = 0
    while True:
        print("\nChoose an operation:")
        for key, (name, _, _) in sorted(MENU.items(), key=lambda item: int(item[0])):
            print(f"  {key}. {name}")
        print("  q. Quit")

        try:
            choice = input("> ").strip()
        except EOFError:
            break
        if choice.lower() == "q":
            break
        if choice not in MENU:
            print("Invalid choice.")
            continue

        name, symbol, op = MENU[choice]
        number1 = random.randint(0, 9)
        number2 = random.randint(0, 9)

        if choice in ("4", "6"):
            try:
                answer = division(number1, number2) if choice == "4" else remainder(number1, number2)
            except ZeroDivisionError as err:
                print(f"Error: {err}. Try another question.")
                continue
        else:
            answer = op(number1, number2)

        print(f"{number1} {symbol} {number2}")
        if ask_question(symbol, answer):
            score += 1
            print("Correct!")
        else:
            print(f"Wrong. The answer is {answer}")

    print(f"\nScore: {score} correct")


if __name__ == "__main__":
    main()
