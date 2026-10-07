# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

def check(value, limit):
    return "OVER LIMIT" if value > limit else "OK"

status = check(87, 100)   # a local variable has to be returned to be seen

print(status)
