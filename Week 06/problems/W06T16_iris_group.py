import pandas as pd

df = pd.read_csv('data/iris_dataset.csv')

means = df.groupby('target').mean(numeric_only=True)
print("Mean measurements per species:")
print(means.round(2))

print("\nLargest average petal length:", means['petal length (cm)'].idxmax())
print("Smallest average sepal width:", means['sepal width (cm)'].idxmin())

df['petal_area'] = df['petal length (cm)'] * df['petal width (cm)']
print("\n5 flowers with largest petal area:")
print(df.nlargest(5, 'petal_area'))

corr = df['petal length (cm)'].corr(df['petal width (cm)'])
print("\nCorrelation between petal length and petal width:", round(corr, 3))
# 0.963 is a very strong positive relationship: longer petals go with wider petals.
