from math import pi, tan

CONVERSIONS = {
    "length": {
        "m -> ft": lambda x: x * 3.28084,
        "ft -> m": lambda x: x / 3.28084,
        "in -> cm": lambda x: x * 2.54,
        "cm -> in": lambda x: x / 2.54,
        "mi -> km": lambda x: x * 1.60934,
        "km -> mi": lambda x: x / 1.60934,
    },
    "temperature": {
        "C -> F": lambda x: x * 9 / 5 + 32,
        "F -> C": lambda x: (x - 32) * 5 / 9,
        "C -> K": lambda x: x + 273.15,
        "K -> C": lambda x: x - 273.15,
    },
    "mass": {
        "kg -> lb": lambda x: x * 2.20462,
        "lb -> kg": lambda x: x / 2.20462,
        "g -> oz": lambda x: x / 28.3495,
        "oz -> g": lambda x: x * 28.3495,
    },
    "volume": {
        "L -> gal": lambda x: x * 0.264172,
        "gal -> L": lambda x: x / 0.264172,
    },
    "pressure": {
        "bar -> psi": lambda x: x * 14.5038,
        "psi -> bar": lambda x: x / 14.5038,
    },
    "energy": {
        "J -> cal": lambda x: x / 4.184,
        "cal -> J": lambda x: x * 4.184,
    },
}


def main():
    while True:
        print("\nTypes: " + ", ".join(CONVERSIONS))
        kind = input("Type (or q to quit): ").strip().lower()
        if kind == "q":
            break
        if kind not in CONVERSIONS:
            print("Unknown type.")
            continue

        options = CONVERSIONS[kind]
        print(f"{kind.capitalize()} conversions:")
        for i, label in enumerate(options, 1):
            print(f"  {i}. {label}")

        try:
            index = int(input("> ")) - 1
            label = list(options)[index]
        except (ValueError, IndexError):
            print("Unknown conversion.")
            continue

        try:
            value = float(input("Value: "))
        except ValueError:
            print("Not a number.")
            continue
        print(f"{label}: {options[label](value):.4f}")


if __name__ == "__main__":
    main()
