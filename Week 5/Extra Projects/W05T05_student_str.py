class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} (age {self.age})"


students = [
    Student("Alice", 19),
    Student("Bob", 21),
    Student("Cara", 20),
    Student("Dan", 22),
    Student("Eve", 18),
]

for student in students:
    print(student)
