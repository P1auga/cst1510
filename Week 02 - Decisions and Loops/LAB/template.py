"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  IT
Date  :

Run it:   python template.py
"""

OVER_LIMIT_COUNT = 0

while True:

    # ================================================================ INPUT
    # 1. Ask for your three values.
    #
    #    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
    #    - the second is a NUMBER (use float(), not int())
    #    - the third  is a NUMBER (use float(), not int())
    #    "quit" as the label is the signal to stop, so check it before the numbers

    label = input("Hostname (or 'quit') : ")
    if label == "quit":
        break

    value = float(input("GB used              : "))
    limit = float(input("GB total             : "))

    # ============================================================== PROCESS
    # 2. Work out the difference and the percentage.       [Typical and above]

    difference = limit - value
    percent = (value / limit) * 100

    # 3. Decide a status and store it in a variable called status.
    #
    #    Typical   : if / elif / else -> "OVER LIMIT" (100% or more),
    #                                     "WARNING" (90% or more), otherwise "OK"

    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    if status == "OVER LIMIT":
        OVER_LIMIT_COUNT += 1

    # =============================================================== OUTPUT
    # 4. Print the report.

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  Used        : {value:>10.2f}")
    print(f"  Total       : {limit:>10.2f}")
    print(f"  Free        : {difference:>10.2f}")
    print(f"  Percent     : {percent:>9.2f} %")
    print(f"  Status      : {status:>10}")
    print("=" * 34)

print(f"{OVER_LIMIT_COUNT} record(s) came back OVER LIMIT")
