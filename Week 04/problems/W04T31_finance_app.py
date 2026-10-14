expenses = {"Food": [25, 40, 15], "Entertainment": [50, 20], "Travel": [300, 150]}

def add_expense(category, amount):
    expenses.setdefault(category, []).append(amount)

def remove_expense(category, amount):
    if category in expenses and amount in expenses[category]:
        expenses[category].remove(amount)

def summary():
    for category, amounts in expenses.items():
        print(f"{category}: {sum(amounts)}")
    print("Total:", sum(sum(amounts) for amounts in expenses.values()))

add_expense("Food", 30)
remove_expense("Travel", 150)
summary()
