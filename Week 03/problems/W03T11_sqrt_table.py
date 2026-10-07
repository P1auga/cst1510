from math import sqrt

print(f"{'Number':<12}Square root")
for n in range(0, 20, 2):
    print(f"{n:<4}\t \t{sqrt(n):.2f}")
