"""
RECORD CHECK  -  my version
===========================

Name  : Ed Pliauga
Lane  :  IT
Date  : 2026-09-30

Run it:   python template.py
"""

# ==================================================================== INPUT
# 1. Ask for your three values. The loop means one run checks a whole batch.

over_limit = 0

while True:
    label = input("Hostname  (or quit): ")

    if label.strip().lower() == "quit":
        break

    value = float(input("GB used   : "))
    limit = float(input("GB limit  : "))

    # ============================================================== PROCESS
    # 2. Work out the difference and the percentage.   [Typical and above]

    difference = value - limit
    percent = (value / limit) * 100

    # 3. Decide a status and store it in a variable called status.

    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    if status == "OVER LIMIT":
        over_limit += 1

    # =============================================================== OUTPUT
    # 4. Print the report.

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

print(f"\n{over_limit} of the records checked were over limit.")


# ==========================================================================
# 5. Before you finish:
#
#    [x] Run it three times with different numbers
#    [x] Run it with a limit of 0 and note the error (do not fix it yet)
#    [x] Check every variable name says what it holds
