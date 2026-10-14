name = input("Enter a file name: ")

try:
    with open(name) as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")
except Exception as error:
    print("Something went wrong:", error)
