import pandas as pd

df1 = pd.read_csv("dataset/train.csv")
df2 = pd.read_csv("dataset/test.csv")

df1 = df1.sort_values('Fare')
print(df1)