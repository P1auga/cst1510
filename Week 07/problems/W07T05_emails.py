raw_names = [
    "  JOHN smith  ",
    "mary JOHNSON",
    "  bob WILSON  "
]

for raw in raw_names:
    name = raw.strip().title()
    first, surname = name.lower().split()
    email = first + "." + surname + "@company.com"
    print(f"{name} \u2192 {email}")
