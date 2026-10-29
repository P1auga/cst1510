# Finding: 10.0.0.12 and 10.0.0.5 tie on 8 total failures each, but 10.0.0.12
# is the one to escalate first - all 8 came from a single session.

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/login_attempts.csv")

print(df.head())
print(df.dtypes)
print(len(df), "sessions")

print("\nSessions with 3+ failures:")
print(df[df["failed"] >= 3])

per_ip = df.groupby("ip")["failed"].sum().sort_values(ascending=False)
print("\nTotal failures per IP:")
print(per_ip)

print("\nWorst IP overall:")
print(per_ip.head(1))

df["suspicious"] = df["failed"].apply(lambda f: f >= 3)

per_ip.plot(kind="bar", title="Failed attempts per IP")
plt.tight_layout()
plt.savefig("failed_per_ip.png")

df[df["suspicious"]].to_csv("flagged_ips.csv", index=False)
print("\nWrote flagged_ips.csv")
