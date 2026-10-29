# Finding: three of ten responses were unanswered (30%); category A has the
# strongest average score (81.5) among the rows that actually answered.

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/survey_results.csv")

print(df.head())
print(df.dtypes)
print(len(df), "rows")

unanswered = df[df["answered"] == 0]
print(f"\nUnanswered: {len(unanswered)} of {len(df)} ({len(unanswered) / len(df) * 100:.1f}%)")

clean = df[df["answered"] == 1]

print("\nAverage score per category:")
print(clean.groupby("category")["score"].mean().sort_values(ascending=False))

clean = clean.copy()
clean["result"] = clean["score"].apply(lambda s: "Pass" if s >= 60 else "Fail")

print("\nPass/fail counts:")
print(clean["result"].value_counts())

clean["result"].value_counts().plot(kind="bar", title="Survey pass/fail")
plt.tight_layout()
plt.savefig("survey_results.png")

clean.to_csv("survey_results_clean.csv", index=False)
print("\nWrote survey_results_clean.csv")
