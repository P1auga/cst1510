"""
RECORD CHECK  -  my version
===========================

Name  : Ed
Lane  : IT
Date  : 2026-09-28

Run it:   python template.py
"""

# ==================================================================== INPUT
hostname = input("Hostname      : ")
used_gb  = float(input("Used (GB)     : "))
total_gb = float(input("Total (GB)    : "))

# ================================================================== PROCESS
free_gb      = total_gb - used_gb
difference   = used_gb - total_gb
percent_used = (used_gb / total_gb) * 100

# Extra metric: free percentage to see remaining disk headroom before it fills
free_percent = (free_gb / total_gb) * 100

# =================================================================== OUTPUT
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {hostname}")
print("=" * 34)
print(f"  Used (GB)   : {used_gb:>10.2f}")
print(f"  Total (GB)  : {total_gb:>10.2f}")
print(f"  Free (GB)   : {free_gb:>10.2f}")
print(f"  Difference  : {difference:>+10.2f}")
print(f"  Of total    : {percent_used:>10.2f} %")
print(f"  Free ratio  : {free_percent:>10.2f} %")
print("=" * 34)
