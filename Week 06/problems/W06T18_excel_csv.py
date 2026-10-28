import pandas as pd

excel = pd.read_excel('data/data.xlsx')
sample = pd.read_csv('data/sample_data.csv')

print("Excel shape:", excel.shape, "CSV shape:", sample.shape)
print("Same columns:", list(excel.columns) == list(sample.columns))
print("Same rows:", excel.equals(sample))

combined = pd.concat([excel, sample], ignore_index=True)
combined = combined.drop_duplicates()
print("\nCombined without duplicates:")
print(combined)

print("\nPeople older than 30, sorted by Age:")
print(combined[combined['Age'] > 30].sort_values('Age'))
