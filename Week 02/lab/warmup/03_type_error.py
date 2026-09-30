# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

limit = 20
value = float(input("Value: "))   # input() gives back text, so convert it

if value > limit:
    print("OVER")
else:
    print("OK")
