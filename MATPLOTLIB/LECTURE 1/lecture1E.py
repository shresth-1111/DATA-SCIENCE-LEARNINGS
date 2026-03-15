import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Making a PieChart
# data=[23,45,100,20,49]
# subj=["science","sst","maths","it","english"]
# explosion=[0.1,0,0,0.1,0]
# plt.pie(data,labels=subj,autopct='%0.2f%%',explode=explosion)

#USING PROPER DATA SET
df=pd.read_csv('gayle-175.csv')

plt.pie(df["batsman_runs"],labels=df["batsman"],colors=["green","brown","grey","black","darkblue","skyblue"],autopct='%0.1f%%')
plt.show()