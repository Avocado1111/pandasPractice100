import pandas as pd

df1 = pd.read_csv("dataset/train.csv")
df2 = pd.read_csv("dataset/test.csv")

print(df1['Sex'].unique())

print(df1[''].unique())
