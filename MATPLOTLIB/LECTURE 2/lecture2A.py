import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

iris=pd.read_csv('iris.csv')
# print(iris.head(90))

plt.figure(figsize=(15,7))

iris["Species"]=iris['Species'].replace({
    "Iris-setosa":0,                            #Changing the name of Species
    "Iris-virginica":1,                         #helps to plot them correctly and separately 
    "Iris-versicolor":2                         #every species look different and identifiable
})

plt.scatter(iris["SepalLengthCm"],iris["PetalLengthCm"],c=iris["Species"],cmap="winter")
plt.colorbar()                                 #To show the color bar


plt.show()