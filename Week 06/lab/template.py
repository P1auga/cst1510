"""
RECORD CHECK  -  my version
===========================

Name  : Ed Pliauga
Lane  :  IT
Date  : 2026-11-10

Run it:   python template.py
"""

import matplotlib.pyplot as plt
import pandas as pd

# ==================================================================== LOAD

df = pd.read_csv("hosts.csv")


# ================================================================= PROCESS

df["percent"] = (df["value"] / df["limit"]) * 100

df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
)


# ================================================================== OUTPUT

print(df)

print("\nNot OK:")
print(df[df["status"] != "OK"])

print("\nCount per status:")
print(df["status"].value_counts())

df.to_csv("hosts_report.csv", index=False)

df["status"].value_counts().plot(kind="bar", title="Hosts by status")
plt.tight_layout()
plt.savefig("hosts_status.png")
plt.show()
