#importing libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Making a 2D LINE PLOT

#Data set
# price=[48000,54000,57000,49000,47000,45000]
# year=[2015,2016,2017,2018,2019,2020]

# plt.plot(year,price)

#USING PROPER DATA SET
batsman=pd.read_csv("sharma-kohli.csv")

# print(batsman)
# print(batsman.loc[batsman["index"]==2016,"V Kohli"])        JUST PRACTICING PANDAS

plt.plot(batsman["index"],batsman["V Kohli"],
        color="red",
        linestyle="dashed",
        linewidth=2,
        marker='D',
        markersize=5,
        label="KING"
        )
plt.plot(batsman["index"],batsman["RG Sharma"],
        color="blue",
        linestyle="dashed",
        linewidth=2,
        marker='D',
        markersize=5,
        label="HITMAN"
        )

plt.title("Rohit Sharma Vs Virat Kohli Career Comparison")
plt.xlabel("IPL Seasons")
plt.ylabel("Runs Scored")



plt.legend()  #For executing the label feature...
plt.show()   #For executing thr graph...
