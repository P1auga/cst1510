"""Blind Auction - collect bids, announce only the winner."""

bids = {}
bidding = True

while bidding:
    name = input("What is your name? ").strip()
    bid = float(input("What is your bid? $"))

    bids[name] = bid

    more = input("Are there any other bidders? Type 'yes' or 'no': ").strip().lower()
    if more != "yes":
        bidding = False

winner = ""
highest = 0

for name, bid in bids.items():
    if bid > highest:
        highest = bid
        winner = name

print(f"The winner is {winner} with a bid of ${highest:.2f}")
