available = {"Concert": 100, "Football Game": 50, "Theater Show": 75}
purchasers = {"Concert": ["John", "Emily"], "Football Game": ["Alex"], "Theater Show": ["Sam", "John"]}

def check_availability(event):
    return available.get(event, 0)

def buy(event, user, tickets=1):
    if check_availability(event) < tickets:
        print("Not enough tickets for", event)
        return
    available[event] -= tickets
    purchasers.setdefault(event, []).append(user)
    print(user, "bought", tickets, "ticket(s) for", event)

def who_bought(event):
    print(event, "purchasers:", purchasers.get(event, []))

buy("Concert", "Anna", 2)
buy("Football Game", "Anna", 60)
who_bought("Concert")
print("Remaining:", available)
