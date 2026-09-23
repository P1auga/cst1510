"""
RECORD CHECK  -  my version
===========================

Name  : Ed Pliauga
Lane  :  IT
Date  : 2026-09-23

Run it:   python template.py
"""

# ==================================================================== INPUT
# 1. Ask the user for your three values.

label = input("Hostname  : ")
first = float(input("GB used   : "))
second = float(input("GB total  : "))


# ================================================================== PROCESS
# 2. Work out what you were NOT given.

difference = second - first
percent = (first / second) * 100


# =================================================================== OUTPUT
# 3. Print the report.

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"  Used        :{first:>11.2f} GB")
print(f"  Total       :{second:>11.2f} GB")
print(f"  Free        :{difference:>11.2f} GB")
print(f"  Percent used:{percent:>12.1f} %")

# Headroom left before the disk fills - the number this lane acts on.
print(f"  Headroom    :{100 - percent:>12.1f} %")

print("=" * 34)
