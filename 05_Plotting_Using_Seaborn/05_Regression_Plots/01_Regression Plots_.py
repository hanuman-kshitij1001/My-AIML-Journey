import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Jab Ek Quntatity Ka Dusre Quantity ke Sath Relation Nikalte ho usse Liner reg bolte hai

#n the simplest invocation, both functions draw a scatterplot of two variables, x and y, and then fit the regression model y ~ x and plot the resulting regression line and a 95% confidence interval for that regression.

# axes level
# hue parameter is not available
tips = px.data.tips()
sns.regplot(data=tips,x='total_bill',y='tip')
plt.show()
# Hue parameter is Not avlable ^

sns.lmplot(data=tips,x='total_bill',y='tip',hue='sex')
plt.show()

# residplot: SO Ye 
sns.residplot(data=tips,x='total_bill',y='tip')
plt.show()
# Ye hamri Galti bata deta hai 

