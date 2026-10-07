from math import tan, pi


def pentagon_area(s):
    return 5 * s ** 2 / (4 * tan(pi / 5))


if __name__ == "__main__":
    side = float(input("Side length: "))
    print(f"Area = {pentagon_area(side):.2f}")
