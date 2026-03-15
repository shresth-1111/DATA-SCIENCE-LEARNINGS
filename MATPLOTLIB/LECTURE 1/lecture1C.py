import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Making a Bar Chart
# children=[10,20,30,40,50]
# color=["red","blue","orange","purple","green"]
#plt.bar(color,children)
# plt.barh(color,children)


#Plotting a multiple bar chart
df=pd.read_csv("batsman_season_record.csv")

#Single Record
# plt.bar(df["batsman"],df["2016"])


#Multiple Record
# plt.bar(np.arange(df.shape[0])-0.2,df["2015"],width=0.2)
# plt.bar(np.arange(df.shape[0]),df["2016"],width=0.2)
# plt.bar(np.arange(df.shape[0])+0.2,df["2017"],width=0.2)

# plt.xticks(np.arange(df.shape[0]),df["batsman"])

# plt.xticks(rotation='vertical')   To rotate the names on the x axis in case the lenght of the name is very large


#Stacked Bar Chart
plt.bar(df["batsman"],df["2017"],label='2017')
plt.bar(df["batsman"],df["2016"],bottom=(df["2017"]),label="2016")
plt.bar(df["batsman"],df["2015"],bottom=(df["2016"]+df["2017"]),label="2015")

plt.legend()
plt.show()