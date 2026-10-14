class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


s1 = Student("Alice", 19)
s2 = Student("Bob", 21)

print(s1.name, s1.age)
print(s2.name, s2.age)
