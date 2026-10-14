def parse_csv_to_dicts(filepath):
    with open(filepath) as file:
        rows = [line.strip() for line in file if line.strip()]
    headers = rows[0].split(",")
    return [dict(zip(headers, row.split(","))) for row in rows[1:]]

records = parse_csv_to_dicts("DATA/sample_data.csv")
print("Records:", len(records))

ages = [int(record["Age"]) for record in records]
print("Average age:", sum(ages) / len(ages))
print("Oldest:", max(records, key=lambda record: int(record["Age"]))["Name"])

countries = {}
for record in records:
    countries[record["Country"]] = countries.get(record["Country"], 0) + 1
print("People per country:", countries)
