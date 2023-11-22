import pandas as pd

df1 = pd.read_csv("dataset/train.csv")
df2 = pd.read_csv("dataset/test.csv")

df1_copy = df1.copy()
print(df1)