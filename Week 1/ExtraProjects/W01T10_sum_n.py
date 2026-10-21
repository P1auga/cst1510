try:
    n = int(input("Positive integer n: "))
except ValueError:
    print("Not an integer")
else:
    total = n * (n + 1) // 2
    print("Sum of 1..%d = %d" % (n, total))