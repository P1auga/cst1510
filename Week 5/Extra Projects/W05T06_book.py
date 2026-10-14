class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self):
        if not self.is_available:
            print(f"'{self.title}' is already borrowed.")
            return
        self.is_available = False

    def return_book(self):
        self.is_available = True


books = [
    Book("48 Laws of Power", "Robert Greene"),
    Book("Neuromancer", "William Gibson"),
    Book("The Hobbit", "Tolkien"),
    Book("Foundation", "Isaac Asimov"),
]

books[0].borrow()
books[0].borrow()  # second attempt should be refused

print("Available:")
for b in books:
    if b.is_available:
        print(f"- {b.title} by {b.author}")

author = input("Enter an author: ")
found = [b for b in books if b.author == author]
for b in found:
    print(f"- {b.title} by {b.author}")
if not found:
    print("No books by that author.")
