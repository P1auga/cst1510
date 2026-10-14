numbers = []
while True:
    value = int(input("Enter a number (0 to stop): "))
    if value == 0:
        break
    numbers.append(value)

numbers.reverse()
for value in numbers:
    print(value)
