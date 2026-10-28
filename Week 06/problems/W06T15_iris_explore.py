import pandas as pd

df = pd.read_csv('data/iris_dataset.csv')

print("First 5 rows:")
print(df.head())

print("\nShape:", df.shape)
print("\nData types:")
print(df.dtypes)
print("\nDescribe:")
print(df.describe())

print("\nFlowers per species:")
print(df['target'].value_counts())

print("\nMissing values:")
print(df.isnull().sum())
print("\nDuplicated rows:", df.duplicated().sum())
