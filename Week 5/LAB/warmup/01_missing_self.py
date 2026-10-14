# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

class Record:
    def __init__(self, value):
        self.value = value

    def status(self):
        return self.value

r = Record(95)
print(r.status())
