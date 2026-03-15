import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Using subplotting one figure various graphs
# fig, ax=plt.subplots(nrows=2,sharex=True)

# bat_avsr=pd.read_csv('batter_2.csv')

# ax[0].scatter(bat_avsr["runs"],bat_avsr["avg"])
# ax[1].scatter(bat_avsr["runs"],bat_avsr["strike_rate"])

# ax[0].set_title("Batsman Average vs Runs")
# ax[0].set_xlabel("Runs")
# ax[0].set_ylabel("Average")

# ax[1].set_title("Batsman Strike Rate vs Runs")
# ax[1].set_xlabel("Runs")
# ax[1].set_ylabel("Strike Rate")

# plt.show()

#TASK 

batter_rec=pd.read_csv('batter_2.csv')

fig, ax=plt.subplots(nrows=2,ncols=2,figsize=(20,20))


ax[0][0].scatter(batter_rec["avg"],batter_rec["strike_rate"])
ax[0][1].scatter(batter_rec["avg"],batter_rec["runs"])
ax[1][0].hist(batter_rec["avg"],bins=[0,10,20,30,40,50],rwidth=0.7)
ax[1][1].hist(batter_rec["runs"],bins=[0,1000,2000,3000,4000,5000,6000,7000],rwidth=0.7)

ax[0][0].set_title("Avg vs Strike Rate")
ax[0][0].set_xlabel("Average")
ax[0][0].set_ylabel("Strike Rate")

ax[0][1].set_title("Avg vs Runs")
ax[0][1].set_xlabel("Average")
ax[0][1].set_ylabel("Runs")

ax[1][0].set_title("Average of batsman")
ax[1][0].set_xlabel("Avg bins")
ax[1][0].set_ylabel("Number of Players")

ax[1][1].set_title("Runs of batsman")
ax[1][1].set_xlabel("Run bins")
ax[1][1].set_ylabel("Number of Players")

plt.show()