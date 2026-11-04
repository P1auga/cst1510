def check_password(password):
    if " " in password:
        print(f"{password!r} rejected: contains a space")
        return

    score = 0
    score += 1 if len(password) >= 8 else 0
    score += 1 if any(char.isupper() for char in password) else 0
    score += 1 if any(char.islower() for char in password) else 0
    score += 1 if any(char.isdigit() for char in password) else 0
    score += 1 if any(char in "@#$%!" for char in password) else 0

    if score <= 2:
        label = "Weak"
    elif score <= 4:
        label = "Medium"
    else:
        label = "Strong"

    print(f"{password!r} -> score {score}/5 ({label})")


test_passwords = [
    "hello",
    "Hello123",
    "My Pass!",
    "Str0ng@Pass",
    "12345678"
]

for password in test_passwords:
    check_password(password)
