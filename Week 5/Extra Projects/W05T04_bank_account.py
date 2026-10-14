class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds: balance is {self.balance}")
            return
        self.balance -= amount

    def show_balance(self):
        print(f"{self.owner}: balance {self.balance}")


acc = BankAccount("Alice")
acc.deposit(100)
acc.deposit(50)
acc.withdraw(30)
acc.show_balance()
acc.withdraw(500)
acc.show_balance()
