#Importing  libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#PART 5

#Creating Pie Charts
#Purpose - Used for univariate or bivariate analysis [numerical / numerical vs categorical]

data=[23,45,100,20,49]

plt.figure()
plt.pie(data)

plt.figure()
plt.pie(data,autopct="%0.1f%%")  #Used to show percentage on chart

plt.figure()
subjects=["Maths","Physics","CS","Chemistry","English"]
plt.pie(data,labels=subjects,autopct="%0.1f%%")     #Used to show labels to the pie (be careful of the order should be same in both lists data and subjects)
#Similarly you can pass list of colors to change colors, in same order

plt.figure()
plt.pie(data,explode=[0.1,0,0,0,0.1]) #To make the feel deattached/separate from others 

plt.show()
