import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.read_csv("dataset/train.csv")
df2 = pd.read_csv("dataset/test.csv")

corr = df1.corr()
print(corr)