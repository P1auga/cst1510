class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def average_mark(self, student_name):
        for s in self.students:
            if s.name == student_name:
                return sum(s.marks) / len(s.marks)
        return None

    def top_student(self):
        return max(self.students, key=lambda s: sum(s.marks) / len(s.marks))


course = Course("Python")
course.add_student(Student("Alice", [80, 90, 70]))
course.add_student(Student("Bob", [60, 65, 70]))
course.add_student(Student("Cara", [95, 88, 92]))
course.add_student(Student("Dan", [50, 55, 60]))

for s in course.students:
    print(f"{s.name}: {course.average_mark(s.name):.2f}")

top = course.top_student()
print(f"Top student: {top.name} ({course.average_mark(top.name):.2f})")
