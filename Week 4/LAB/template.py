"""
RECORD CHECK  -  my version
===========================

Name  : J.Ward
Lane  :  IT      (delete two)
Date  : 2026-03-19

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.


def check_record(value, limit):
    """Return the difference, percent used and status for one record."""
    difference = value - limit
    percent = (value / limit) * 100
    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
    return difference, percent, status


def print_report(label, value, limit):
    """Print one formatted line for a record."""
    difference, percent, status = check_record(value, limit)
    print(f"{label}: {value}/{limit} ({percent:.1f}%) {status}")


def load_records(path):
    """Read label,value,limit lines from a file and return a list of dicts."""
    records = []
    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append({"label": label, "value": float(value), "limit": float(limit)})
    return records


def write_results(path, records):
    """Write one label,status line per record to a file."""
    with open(path, "w") as f:
        for record in records:
            _, _, status = check_record(record["value"], record["limit"])
            f.write(f"{record['label']},{status}\n")


# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.

try:
    records = load_records("servers.txt")
except FileNotFoundError:
    print("servers.txt not found - starting with no records")
    records = []


# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

over_limit = 0

for record in records:
    print_report(record["label"], record["value"], record["limit"])
    _, _, status = check_record(record["value"], record["limit"])
    if status == "OVER LIMIT":
        over_limit += 1

print(f"{over_limit} of {len(records)} were over limit")

write_results("results.txt", records)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
