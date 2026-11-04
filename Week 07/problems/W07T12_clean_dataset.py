def clean_dataset(records):
    valid_records = []
    invalid_records = []

    for record in records:
        fields = [field.strip() for field in record.split("|")]

        if len(fields) != 4 or not all(fields):
            invalid_records.append((record, "empty field"))
            continue

        name, age, email, country = fields
        reasons = []

        if not all(char.isalpha() or char == " " for char in name):
            reasons.append("name is not letters only")

        if not age.isdigit() or not 18 <= int(age) <= 120:
            reasons.append("age not a number between 18 and 120")

        at = email.find("@")
        if at == -1 or "." not in email[at:]:
            reasons.append("invalid email")

        if reasons:
            invalid_records.append((record, "; ".join(reasons)))
        else:
            valid_records.append({
                "name": " ".join(name.title().split()),
                "age": int(age),
                "email": email,
                "country": country.upper()
            })

    return valid_records, invalid_records


raw_data = [
    "  john SMITH  | 25 | john.smith@email.com | united kingdom ",
    "  MARY  johnson | abc | mary@email | france",
    " | 30 | test@test.com | germany",
    "  bob wilson  | 17 | bob@mail.com | spain  ",
    "  alice Brown  | 28 | alice.b@data.org | italy  ",
    "charlie DAVIS | 35 | | usa"
]

valid, invalid = clean_dataset(raw_data)

print("Valid records:")
for item in valid:
    print(" ", item)

print("Invalid records:")
for record, reason in invalid:
    print(f"  {record!r} -> {reason}")
