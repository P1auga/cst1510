numbers = []

while True:
    text = input('Enter a positive number or "done": ')
    if text.lower() == "done":
        break
    if text.isdigit():
        numbers.append(int(text))

if numbers:
    print("Numbers entered:", numbers)
    first_even = None
    for number in numbers:
        if number % 2 == 0:
            first_even = number
            break
    if first_even is None:
        print("No even numbers found")
    else:
        print("First even number:", first_even)
else:
    print("No numbers were entered")
