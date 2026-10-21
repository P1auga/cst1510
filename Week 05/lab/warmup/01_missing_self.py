# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

class Record:
    def status(self):
        return "OK"

r = Record()
print(r.status())
