class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


rects = [
    Rectangle(3, 4),
    Rectangle(5, 5),
    Rectangle(2, 10),
    Rectangle(6, 7),
]

for i, r in enumerate(rects, 1):
    print(f"Rectangle {i}: area {r.area()}, perimeter {r.perimeter()}")

largest = max(rects, key=lambda r: r.area())
print(f"Largest area: {largest.width}x{largest.height} = {largest.area()}")
