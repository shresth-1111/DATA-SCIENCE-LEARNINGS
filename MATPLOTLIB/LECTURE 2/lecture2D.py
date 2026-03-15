#3D PLOTS

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Plotting a 3D scatter plot

# batter_rec=pd.read_csv('batter_2.csv')

# fig=plt.figure() #Creating a figure 

# ax1=plt.subplot(projection="3d")
# ax1.scatter3D(batter_rec["runs"],batter_rec["avg"],batter_rec["strike_rate"])

# ax1.set_title("IPL BATSMAN AVG SR RUNS CHART")
# ax1.set_xlabel("Runs Scored")
# ax1.set_ylabel("Average")
# ax1.set_zlabel("Strike Rate")

#Plotting a 3D line plot

#Using hardcoded data

# x=[0,1,5,15]
# y=[0,10,13,0]
# z=[0,13,20,9]

# fig=plt.figure()

# ax1=plt.subplot(projection="3d")
# ax1.scatter3D(x,y,z)
# ax1.plot3D(x,y,z,color='red')

#Plotting a 3D surface plot

x=np.linspace(-10,10,100)
y=np.linspace(-10,10,100)

xx,yy=np.meshgrid(x,y)
z=xx**2+yy**2

fig=plt.figure()

ax=plt.subplot(projection="3d")
ax.plot_surface(xx,yy,z)

ax.set_xlabel("Values of x")
ax.set_ylabel("Values of y")
ax.set_zlabel("Values of z")

plt.show()