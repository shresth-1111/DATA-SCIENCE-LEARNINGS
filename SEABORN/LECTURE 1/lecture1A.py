import seaborn as sns 
import matplotlib.pyplot as plt
import plotly.express as px

tips=sns.load_dataset('tips')
# sns.scatterplot(data=tips,x="total_bill",y="tip")  #This is a axes level function

# sns.relplot(data=tips,x="total_bill",y="tip",kind="scatter")  #This is a figure level function 

# sns.scatterplot(data=tips,x="total_bill",y="tip",hue="sex")  #To differentiate on the basis of sex (it will use color)

# sns.scatterplot(data=tips,x="total_bill",y="tip",hue="sex",style="time")  #To differentiate on the basis of timing (it will use shape)

sns.scatterplot(data=tips,x="total_bill",y="tip",hue="sex",style="time",size="size")

plt.show()