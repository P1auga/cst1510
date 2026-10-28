import pandas as pd

df = pd.read_csv('data/CARS.text')

print("5 cars with best mpg:")
print(df.nlargest(5, 'mpg')[['model', 'mpg', 'cyl', 'hp']])
print("\n5 cars with worst mpg:")
print(df.nsmallest(5, 'mpg')[['model', 'mpg', 'cyl', 'hp']])

print("\n4 cylinders with hp above 90:")
print(df[(df['cyl'] == 4) & (df['hp'] > 90)][['model', 'cyl', 'hp']])

print("\nSummary by cylinder count:")
print(df.groupby('cyl').agg(Count=('model', 'count'), Avg_MPG=('mpg', 'mean'), Avg_HP=('hp', 'mean')).round(1))

def efficiency(mpg):
    if mpg >= 25:
        return 'High'
    if mpg >= 18:
        return 'Medium'
    return 'Low'

df['Efficiency'] = df['mpg'].apply(efficiency)
print("\nEfficiency counts:")
print(df['Efficiency'].value_counts())

df.to_csv('cars_clean.csv', index=False)
