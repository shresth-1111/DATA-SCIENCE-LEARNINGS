import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Making a Histogram

# classMark=[10,20,30,40,50,60,70,80,90,100]
# data=np.arange(0,20,2)
# print(data)
# plt.hist(data,bins=[0,5,10,15,20],rwidth=1)


#USING PROPER DATA SET
# df=pd.read_csv('vk.csv')
# print(df)
# plt.hist(df["batsman_runs"],bins=np.arange(0,130,10),rwidth=0.5)

#USING A BIG DATA SET
# direc=np.load('big-array.npy')
# plt.hist(direc,bins=[10,20,30,40,50,60,70],log=True,rwidth=0.5)
plt.show()

