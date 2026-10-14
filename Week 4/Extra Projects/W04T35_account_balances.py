try:
    accounts = {}
    with open("DATA/accounts1.txt") as file:
        for line in file:
            if not line.strip():
                continue
            account_id, surname, balance = line.split()
            accounts[account_id] = {"name": surname, "balance": float(balance)}
except FileNotFoundError:
    print("File not found")
else:
    print(f"{'ID':<6}{'Name':<12}{'Balance':>10}")
    for account_id, account in accounts.items():
        print(f"{account_id:<6}{account['name']:<12}{account['balance']:>10.2f}")

    total = sum(account["balance"] for account in accounts.values())
    print("Total balance:", round(total, 2))

    richest = max(accounts.items(), key=lambda item: item[1]["balance"])
    print("Highest balance:", richest[1]["name"], richest[1]["balance"])
