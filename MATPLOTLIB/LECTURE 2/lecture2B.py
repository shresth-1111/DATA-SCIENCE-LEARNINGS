import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('batter_2.csv')
# print(df.shape)

random_df=df.head(100).sample(25,random_state=5)
# print(random_df)

plt.figure(figsize=(20,15))

plt.scatter(random_df["avg"],random_df["strike_rate"],s=random_df["runs"])

for i in range(random_df.shape[0]):
    plt.text(random_df["avg"].values[i],random_df["strike_rate"].values[i],random_df["batter"].values[i])

plt.title("Average vs Strike Rate")
plt.xlabel("Average")
plt.ylabel("Strike Rate")


plt.show()