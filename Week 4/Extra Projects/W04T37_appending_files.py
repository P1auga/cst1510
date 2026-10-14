for path in ("DATA/test.txt", "DATA/user_info.txt"):
    print("---", path)
    with open(path) as file:
        print(file.read())

with open("DATA/user_info.txt", "a") as file:
    file.write("\nCourse: Python\n")

with open("DATA/user_info.txt") as file:
    content = file.read()

print("Lines:", len(content.splitlines()))
print("Characters:", len(content))
