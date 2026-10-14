for path in ("data/test.txt", "data/user_info.txt"):
    print("---", path)
    with open(path) as file:
        print(file.read())

with open("data/user_info.txt", "a") as file:
    file.write("\nCourse: Python\n")

with open("data/user_info.txt") as file:
    content = file.read()

print("Lines:", len(content.splitlines()))
print("Characters:", len(content))
