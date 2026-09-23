name = input("Dataset name: ")
try:
    rows = int(input("Rows: "))
    columns = int(input("Columns: "))
except ValueError:
    print("Rows and columns must be integers")
else:
    print('"' + name + '"')
    print("Rows:", rows)
    print("Columns:", columns)
    print("Cells:", rows * columns)