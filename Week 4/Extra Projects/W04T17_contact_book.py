contacts = {
    "Mom": "555-1234",
    "Dad": "555-5678",
    "Friend": "555-9012"
}

contacts["Sister"] = "555-3456"
print("Mom's number:", contacts["Mom"])

for name, number in contacts.items():
    print(f"{name}: {number}")
