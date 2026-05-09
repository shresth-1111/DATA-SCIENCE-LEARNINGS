#importing libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#PART 4

#Creating Histogram
#Purpose - Used for univariate analysis generally for numerical data specially for frquency count 

plt.figure()
data=[32,45,56,10,15,27,61]
plt.hist(data)    #Bins will be decide internally on their own

plt.figure()
plt.hist(data,bins=[10,20,30,40,50,60,70])  #Deciding bin size manually
#Bins created will be 
#10-20 (10 included, 20 excluded)
#20-30 (20 included, 30 excluded) ...continue

#Use rwidth to change the width of bars (rwidth have nothing to do with bin size)
#If frequency of few data points is too high compare to other you can use log=true as an attribute

plt.show()