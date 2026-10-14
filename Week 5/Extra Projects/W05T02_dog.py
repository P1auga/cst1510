class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

    def birthday(self):
        self.age += 1


dog = Dog("Rex", 3)
dog.bark()
dog.birthday()
dog.birthday()
print(dog.age)
