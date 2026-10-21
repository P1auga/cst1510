class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def apply_discount(self, percent):
        self.price = round(self.price * (1 - percent / 100), 2)


products = [
    Product("Keyboard", 40.0, 3),
    Product("Mouse", 15.0, 10),
    Product("Monitor", 200.0, 2),
    Product("Cable", 5.0, 25),
    Product("Webcam", 60.0, 4),
]

total = sum(p.total_value() for p in products)
print(f"Inventory total: {total}")

for p in products:
    p.apply_discount(10)

print("Prices after 10% discount:")
for p in products:
    print(f"- {p.name}: {p.price}")
