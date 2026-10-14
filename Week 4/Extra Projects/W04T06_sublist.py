def isSublist(larger, smaller):
    if len(smaller) == 0:
        return True
    for start in range(len(larger) - len(smaller) + 1):
        if larger[start:start + len(smaller)] == smaller:
            return True
    return False

print(isSublist([1, 2, 3, 4], [2, 3]))
print(isSublist([1, 2, 3, 4], [2, 4]))
print(isSublist([1, 2, 3, 4], []))
print(isSublist([1, 2, 3, 4], [1, 2, 3, 4]))
