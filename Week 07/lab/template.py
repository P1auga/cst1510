"""
RECORD CHECK  -  my version
===========================

Name  : Ed Pliauga
Lane  :  IT
Date  : 2026-11-10

Run it:   python template.py
"""

# =================================================================== FUNCTIONS


def parse_line(raw_line):
    """Turn one messy raw status line into a clean dict."""
    line = raw_line.strip()
    hostname_part, rest = line.split(",", 1)
    hostname = hostname_part.strip().lower()

    fields = {}
    for piece in rest.split(","):
        # maxsplit=1 keeps a value that itself contains "=" intact
        key, value = piece.split("=", 1)
        fields[key.strip().lower()] = float(value.strip())

    return {"hostname": hostname, "used": fields["used"], "total": fields["total"]}


def status_of(used, total, warning_at=90):
    """Return OVER LIMIT, WARNING or OK for a used/total pair."""
    percent = (used / total) * 100
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= warning_at:
        return "WARNING"
    else:
        return "OK"


# ====================================================================== INPUT

# Own file, so the LAB's supplied messy_lines.txt is not overwritten.
RAW_FILE = "raw_records.txt"

raw_lines = [
    "  Srv-01 , used=87 , total=100  ",
    "SRV-02,used=120,total=100",
    "  srv-03,used=45 ,total=100",
    "Srv-04 , used = 93 , total=100 ",
    "  SRV-05, USED=101 , TOTAL=100",
    "srv-06,used=59,total=100",
]

with open(RAW_FILE, "w") as f:
    for line in raw_lines:
        f.write(line + "\n")


# =============================================================== PROCESS + OUTPUT

records = []
flagged = 0

with open(RAW_FILE) as f:
    for raw_line in f:
        if not raw_line.strip():
            continue

        try:
            record = parse_line(raw_line)
        except (ValueError, KeyError) as error:
            print(f"Could not parse {raw_line.strip()!r}: {error}")
            continue

        status = status_of(record["used"], record["total"])
        record["status"] = status
        records.append(record)

        if status != "OK":
            flagged += 1

        print(f"{record['hostname']:<8} {record['used']:>6.1f}/{record['total']:<6.1f} {status}")

print(f"\n{len(records)} records, {flagged} flagged")
