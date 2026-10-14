import random

ticket = random.sample(range(1, 50), 6)
ticket.sort()
print("Lottery numbers:", ticket)
