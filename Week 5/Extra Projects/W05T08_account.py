class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.failed_attempts = 0

    def login(self, password):
        if self.failed_attempts >= 3:
            print("Account is locked.")
            return False
        if password == self.password:
            self.failed_attempts = 0
            return True
        self.failed_attempts += 1
        print(f"Wrong password. Failed attempts: {self.failed_attempts}")
        return False


acc = Account("alice", "secret")

print(acc.login("secret"))   # True
print(acc.login("wrong"))    # False, attempts 1
print(acc.login("wrong"))    # False, attempts 2
print(acc.login("wrong"))    # False, attempts 3 -> locked
print(acc.login("secret"))   # refused, locked
print(acc.login("secret"))   # still refused
