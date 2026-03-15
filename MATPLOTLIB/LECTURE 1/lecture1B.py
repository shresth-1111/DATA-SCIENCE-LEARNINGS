import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Making a scatter plot
# x=np.linspace(-10,10,50) #making an array of 50 numbers between -10 and 10 equally placed
# y=10*x+3+ np.random.randint(0,300,50) #Making an array of 50 numbers 10*x+3 means take one element from x multiply by 10 then add 3 then add the element from the np.radint array

# plt.scatter(x,y)

#USING PROPER DATA SET
# df=pd.read_csv('batter.csv')
# plt.scatter(df["avg"].head(50),df["strike_rate"].head(50))

# plt.title("Batsman Average vs Strike Rate Comparison")
# plt.xlabel("Average")
# plt.ylabel("Strike Rate")

#USING SEABORN DATASET
tips=sns.load_dataset('tips')
plt.scatter(tips["total_bill"].head(10),tips["tip"].head(10),s=tips["size"].head(10))

# print(tips)
plt.show()

