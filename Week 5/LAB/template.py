"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  IT
Date  :

Run it:   python template.py
"""

# ====================================================================== CLASS
# 1. Record, with status() worked out from value and limit.

class Record:
    def __init__(self, label, value, limit):
        """Store the hostname, GB used and GB total for one record."""
        self.label = label
        self.value = value
        self.limit = limit

    def percent(self):
        """Return GB used as a percentage of GB total."""
        return (self.value / self.limit) * 100

    def status(self):
        """Return OVER LIMIT, WARNING or OK from this record's percent."""
        p = self.percent()
        if p >= 100:
            return "OVER LIMIT"
        elif p >= 90:
            return "WARNING"
        else:
            return "OK"


# ==================================================================== RECORDS
# 2. Load the records from servers.txt.

def load_records(path):
    """Read label,value,limit lines from a file and return a list of Records."""
    records = []
    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append(Record(label, float(value), float(limit)))
    return records


records = load_records("servers.txt")


# ==================================================================== OUTPUT
# 3. A report per record, then the count.

over_limit_count = 0

for record in records:
    status = record.status()
    difference = record.value - record.limit
    percent = record.percent()

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f"  Used        : {record.value:>10.1f}")
    print(f"  Total       : {record.limit:>10.1f}")
    print(f"  Difference  : {difference:>+10.1f}")
    print(f"  Of total    : {percent:>9.1f} %")
    print(f"  Status      : {status:>10}")
    print("=" * 34)

    if status == "OVER LIMIT":
        over_limit_count += 1

print()
print(f"Checked {len(records)} records. {over_limit_count} were over limit.")