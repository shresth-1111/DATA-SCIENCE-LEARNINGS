#Importing librarires

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#PART 3

#Creating a Bar Chart
#Purpose - Used for bivariate analysis numerical vs categorical 

children=[15,20,32,25,16,32]
color=["blue","orange","chocolate","purple","black","white"]

# plt.figure()
# plt.bar(color,children)

# plt.figure()
# plt.barh(color,children)

#Working on real data set

dataset=pd.read_csv("batsman_season_record.csv")

# plt.figure()
# plt.bar(dataset["batsman"],dataset["2015"])


#Grouped Bar Charts

x=np.arange(dataset.shape[0])   #To create number of position

plt.figure()
#Allocation position
plt.bar(x-0.2,dataset["2015"], width=0.2,label="2015")   
plt.bar(x,dataset["2016"], width=0.2,label="2016")
plt.bar(x+0.2,dataset["2017"], width=0.2,label="2017")

plt.xticks(x, dataset["batsman"])   #Replacing actual position with the batsman name
#On the above xticks we can add attribute rotation-"vertical" to show names vertically  

# plt.legend()
# plt.show()

#Desigining becomes little complex and difficult in grouped bar charts 

#Stacked Bar Charts 

plt.figure()
plt.bar(dataset["batsman"],dataset["2015"],label="2015")     #Sabse niche
plt.bar(dataset["batsman"],dataset["2016"],bottom=(dataset["2015"]),label="2016")   #Uske upar, 2015 iske niche rahega 
plt.bar(dataset["batsman"],dataset["2017"],bottom=(dataset["2015"]+dataset["2016"]),label="2017")  #Sabse upar, 2015,2016 iske niche rahega 

plt.legend()
plt.show()
