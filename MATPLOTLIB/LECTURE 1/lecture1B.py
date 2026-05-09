#Importing libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#PART 2

#Creating a Scatter Plot
#Purpose - Used for bivariate analysis of numerical vs numerical

x=np.linspace(-10,10,50)
y=10*x+3+np.random.randint(0,300,50)

plt.figure()
plt.scatter(x,y)

#Working on real data set

dataset=sns.load_dataset("tips")
print(dataset)

plt.figure()
plt.scatter(dataset["total_bill"],dataset["tip"])

#Now you can use those scttered markers to indicate one more data say size
plt.figure()
plt.scatter(dataset["total_bill"].head(10),dataset["tip"].head(10),s=dataset["size"].head(10))

# total_bill → x-axis
# tip → y-axis
# size → marker/dot ka size
# bada circle → table size zyada
# chhota circle → fewer people


#We can plot scatter plot usig plt.plot() but styling becomes little difficult in this method
plt.figure()
plt.plot(x,y,'o')

plt.show()

