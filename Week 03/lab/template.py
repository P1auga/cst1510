"""
RECORD CHECK  -  my version
===========================

Name  : Ed Pliauga
Lane  :  IT
Date  : 2026-10-07

Run it:   python template.py
"""


# =================================================================== FUNCTIONS
# 1. One job per function: calculate, return, and only print_report() prints.

def status_of(percent):
    """Return OVER LIMIT, WARNING or OK for a percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    return "OK"


def check(value, limit):
    """Return the difference and the percentage, without printing."""
    return value - limit, (value / limit) * 100


def print_report(label, value, limit, difference, percent, status):
    """Print the bordered record-check block for one record."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)

    print(f"  Used        :{value:>11.2f} GB")
    print(f"  Limit       :{limit:>11.2f} GB")
    print(f"  Difference  :{difference:>+11.2f} GB")
    print(f"  Percent used:{percent:>11.1f} %")
    print(f"  Status      : {status}")

    print("=" * 34)


# ==================================================================== INPUT
# 2. Ask for your three values. The loop means one run checks a whole batch.

over_limit = 0

while True:
    label = input("Hostname  (or quit): ")

    if label.strip().lower() == "quit":
        break

    value = float(input("GB used   : "))
    limit = float(input("GB limit  : "))

    # ============================================================== PROCESS
    # 3. Work out the difference, the percentage, and the status.
    difference, percent = check(value, limit)
    status = status_of(percent)

    if status == "OVER LIMIT":
        over_limit += 1

    # =============================================================== OUTPUT
    # 4. Print the report.
    print_report(label, value, limit, difference, percent, status)

print(f"\n{over_limit} of the records checked were over limit.")


# ==========================================================================
# 5. Before you finish:
#
#    [x] Run it three times with different numbers
#    [x] Run it with a limit of 0 and note the error (do not fix it yet)
#    [x] Check every function does one job - if a function both calculates
#        and prints, split it
