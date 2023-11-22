import pandas as pd

df1 = pd.read_csv("dataset/train.csv")
df2 = pd.read_csv("dataset/test.csv")

print(df1['Pclass'].dtype)
df1['Pclass'] = df1['Pclass'].astype(str)
print(df1['Pclass'].dtype)