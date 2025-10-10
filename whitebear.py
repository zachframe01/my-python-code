import pandas as pd

df = pd.read_csv("orders.csv")
print(df)

print("now the head")
print("the head is the first 5 columns!")

print(df.head())

print('this is the info')
print(df.info())

print('this is the describe')
print(df.describe())

