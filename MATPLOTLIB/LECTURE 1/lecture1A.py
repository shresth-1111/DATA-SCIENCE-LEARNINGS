#importing libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

#PART 1

#Creating a 2D line plot 
#Purpose - Used for bivariate analysis numerical vs categorical / numerical vs numerical

year = [2015,2016,2017,2018,2019,2020]
price=[48000,54000,57000,49000,47000,45000]

# continuous timeline → numerical                    [2015,2016,2017,2018,2019,2020]
# repeated labels/groups → categorical usage         [2015,2016,2015,2015,2016]

# plt.plot(year,price)         #For plotting a 2D line plot
# plt.show()

#Working on real data set 

#Virat Kohli vs #Rohit Sharma 
batsman=pd.read_csv("sharma-kohli.csv");  #Reading file 

#Showing them on one graph
plt.plot(batsman["index"],batsman["RG Sharma"],color="blue",label="Rohit Sharma")
plt.plot(batsman["index"],batsman["V Kohli"],color="red",label="Virat Kohli")
plt.legend()  #To show the label on the top of graph that hepls to read which plot belongs to whom
plt.grid()    #Creates grid(boxes) on the graph
plt.show()

#Showing them on different graph

# plt.figure() → naya graph canvas banata hai
# har show() ek separate graph display karega - ek ek karke graphs appear honge 
#You can also write one plt.show() at the end only that will work too instead of separate plt.show()


plt.figure()    
plt.plot(batsman["index"],batsman["RG Sharma"],color="blue",marker="o")  
#Marker are used to show the exact point of meeting of x and y on the line plot (You can change the size using marker size)
plt.title("Rohit Sharma")
plt.show()

plt.figure()
plt.plot(batsman["index"],batsman["V Kohli"],color="red")
plt.title("Virat Kohli")
plt.show()

#Some other attributes that you can add with plt.plot for designing
#linestyle
#linewidth

#for title use 
#Plt.title
#Plt.xtitle
#Plt.ytitlt