# Finding: north has the highest average usage (88.7%); srv-03 is the single
# most at-risk server at 120%, and 3 of 10 servers are OVER LIMIT.

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("../walkthroughs/01_Series_and_DataFrame/servers.csv")

print(df.head())
print(df.dtypes)
print(len(df), "servers,", len(df.columns), "columns")

df["percent"] = (df["used"] / df["total"]) * 100

at_or_above_90 = df[df["percent"] >= 90]
print("\nAt or above 90%:", len(at_or_above_90))
print(at_or_above_90[["hostname", "region", "percent"]])

print("\nAverage percent per region:")
print(df.groupby("region")["percent"].mean())

print("\nMost at risk:")
print(df.sort_values("percent", ascending=False).head(1))

df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
)

print("\nServers per status:")
print(df["status"].value_counts())

df["status"].value_counts().plot(kind="bar", title="Servers by status")
plt.tight_layout()
plt.savefig("servers_by_status.png")

df[df["status"] == "OVER LIMIT"].to_csv("servers_at_risk.csv", index=False)
print("\nWrote servers_at_risk.csv")
