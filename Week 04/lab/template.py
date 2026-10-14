"""
RECORD CHECK  -  my version
===========================

Name  : Ed Pliauga
Lane  :  IT
Date  : 2026-11-10

Run it:   python template.py
"""

# =================================================================== FUNCTIONS


def check_record(value, limit):
    """Return difference, percent and status for one record."""
    difference = value - limit
    percent = (value / limit) * 100

    if percent > 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    return difference, percent, status


def print_report(hostname, used_gb, total_gb):
    """Print the report block for one host."""
    difference, percent, status = check_record(used_gb, total_gb)
    free_gb = total_gb - used_gb

    print("=" * 34)
    print(f"  DISK REPORT  -  {hostname}")
    print("=" * 34)
    print(f"  Used        :{used_gb:>11.2f} GB")
    print(f"  Total       :{total_gb:>11.2f} GB")
    print(f"  Free        :{free_gb:>11.2f} GB")
    print(f"  Over limit  :{difference:>+11.2f} GB")
    print(f"  Percent used:{percent:>11.1f} %")
    print(f"  Status      :{status:>11}")
    print("=" * 34)


# ====================================================================== STORE


def load_records(path):
    """Read hostname,used,total lines into a list of dicts; [] if missing."""
    records = []
    try:
        with open(path) as f:
            for line in f:
                label, value, limit = line.strip().split(",")
                records.append({
                    "label": label,
                    "value": float(value),
                    "limit": float(limit),
                })
    except FileNotFoundError:
        print(f"{path} not found - reporting nothing")
    return records


def save_results(path, records):
    """Write one label,status line per record."""
    with open(path, "w") as f:
        for record in records:
            _, _, status = check_record(record["value"], record["limit"])
            f.write(f"{record['label']},{status}\n")


# =============================================================== PROCESS + OUTPUT

records = load_records("hosts.txt")

over_limit = 0
for record in records:
    print_report(record["label"], record["value"], record["limit"])
    if check_record(record["value"], record["limit"])[2] == "OVER LIMIT":
        over_limit += 1

print(f"\n{over_limit} of {len(records)} hosts were over limit")

save_results("results.txt", records)
