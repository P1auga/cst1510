def sum_row(matrix, rowIndex):
    return sum(matrix[rowIndex])

matrix = []
print("Enter a 4-by-4 matrix:")
for _ in range(4):
    matrix.append([int(x) for x in input().split()])

for index in range(4):
    print(f"Sum of row {index}: {sum_row(matrix, index)}")
