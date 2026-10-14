groups = {"John": ["Math", "Physics"], "Emily": ["Physics", "Biology"], "Alex": ["Math"]}

def join(student, group):
    if student not in groups:
        groups[student] = []
    if group not in groups[student]:
        groups[student].append(group)

def leave(student, group):
    if student in groups and group in groups[student]:
        groups[student].remove(group)

def display(student):
    print(student, "is in:", groups.get(student, []))

join("Sam", "Math")
join("John", "Biology")
leave("Alex", "Math")

for student in groups:
    display(student)
