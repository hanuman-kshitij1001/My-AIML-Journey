# A second way to plot Facet plots -> FacetGrid
# Facetgrid = 
# figure level -> relplot -> displot -> catplot -> lmplot

import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
tips = px.data.tips()
sns.catplot(data=tips,x='sex',y='total_bill',kind='violin',col='day',row='time')
plt.show()

# Yaha Maine Eska 
g = sns.FacetGrid(data=tips,col='day',row='time',hue='smoker')
g.map(sns.boxplot,'sex','total_bill')
g.add_legend()
plt.show()