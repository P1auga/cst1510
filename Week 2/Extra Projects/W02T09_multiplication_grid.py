for row in range(10):
    line = ""
    for column in range(10):
        line += f"{row * column:>4}"
    print(line.lstrip() + " ")
