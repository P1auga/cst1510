"""
RECORD CHECK  -  my version
===========================

Name  : Ed Pliauga
Lane  :  IT
Date  : 2026-11-10

Run it:   python template.py
"""

# ====================================================================== CLASS


class Record:
    """One host's disk figures, with the checks that belong to them."""

    def __init__(self, label, value, limit):
        """Store the three fields for one record."""
        self.label = label
        self.value = value
        self.limit = limit

    def percent(self):
        """Return used as a percentage of total."""
        return (self.value / self.limit) * 100

    def status(self):
        """Return OVER LIMIT, WARNING or OK, using percent()."""
        p = self.percent()

        if p > 100:
            return "OVER LIMIT"
        elif p >= 90:
            return "WARNING"
        else:
            return "OK"

    def report(self, status):
        """Print the bordered report for this record."""
        print()
        print("=" * 34)
        print(f"  DISK REPORT  -  {self.label}")
        print("=" * 34)
        print(f"  Used        :{self.value:>11.2f} GB")
        print(f"  Total       :{self.limit:>11.2f} GB")
        print(f"  Free        :{self.limit - self.value:>11.2f} GB")
        print(f"  Percent used:{self.percent():>11.1f} %")
        print(f"  Status      :{status:>11}")
        print("=" * 34)


# ==================================================================== RECORDS


def load_records(path):
    """Read hostname,used,total lines into a list of Record objects."""
    records = []
    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append(Record(label, float(value), float(limit)))
    return records


records = load_records("hosts.txt")


# ==================================================================== OUTPUT

over_limit = 0

for record in records:
    status = record.status()
    if status == "OVER LIMIT":
        over_limit += 1
    record.report(status)

print(f"\n{over_limit} of {len(records)} hosts were over limit")
