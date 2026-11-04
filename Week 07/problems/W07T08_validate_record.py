def validate_record(record):
    errors = []
    fields = record.split(",")

    if len(fields) != 4:
        return ["record must have exactly 4 fields"]

    name, age, email, phone = [field.strip() for field in fields]

    if not all([name, age, email, phone]):
        return ["all fields must be non-empty"]

    if not all(char.isalpha() or char == " " for char in name):
        errors.append("name must contain only letters and spaces")

    if not age.isdigit() or not 18 <= int(age) <= 100:
        errors.append("age must be a number between 18 and 100")

    if "@" not in email or "." not in email:
        errors.append("email must contain @ and .")

    if not (phone.startswith("+") or phone.startswith("0")):
        errors.append("phone must start with + or 0")

    return errors


records = [
    "Alice Smith,25,alice@email.com,+447123456789",
    "Bob,abc,bob@email,07123456789",
    "Charlie123,30,charlie@mail.com,447123456789",
    ",22,missing@mail.com,+440000000000"
]

for record in records:
    errors = validate_record(record)
    if errors:
        print(record, "->", "; ".join(errors))
    else:
        print(record, "-> valid")
