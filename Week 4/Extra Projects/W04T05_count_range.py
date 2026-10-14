def countRange(values, minimum, maximum):
    count = 0
    for value in values:
        if minimum <= value < maximum:
            count += 1
    return count

print(countRange([1, 2, 3, 4, 5], 2, 5))
print(countRange([10, 20, 30, 40], 15, 40))
print(countRange([1.5, 2.5, 3.5, 4.5], 2.0, 4.0))
print(countRange([1.5, 2.5, 3.5, 4.5], 1.0, 3.0))
