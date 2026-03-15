import seaborn as sns 
import matplotlib.pyplot as plt
import plotly.express as px

gap=px.data.gapminder()

# filtration=gap["country"]=="India"   #Filtering Out India Only
# df=gap.loc[filtration]

# sns.lineplot(data=df,x="year",y="lifeExp")  #Axis Level Function
# sns.relplot(data=df,x="year",y="lifeExp",kind="line") #Figure Level Function

filtration2=gap["country"].isin(["India","Brazil","Germany"])
df2=gap.loc[filtration2]

# sns.relplot(data=df2,x="year",y="lifeExp",kind="line",hue="country",style="continent")

sns.relplot(kind="line",data=df2,x="year",y="lifeExp",row="continent")

plt.show()