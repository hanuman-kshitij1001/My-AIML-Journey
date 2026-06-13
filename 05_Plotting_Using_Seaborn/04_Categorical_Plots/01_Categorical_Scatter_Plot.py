#Categorical Scatter Plot  EssePlot jo aap Cato.. data pe plot karte ho 
# . Stripplot
# . Swarmplot



#1. Stripplot

import seaborn as sns

import matplotlib.pyplot as plt
import plotly.express as px

# import datasets
tips = sns.load_dataset('tips')
iris = sns.load_dataset('iris')

sns.scatterplot(data=tips, x='total_bill',y='tip')
plt.show()

# Strip plot .. # axes level function
sns.stripplot(data=tips, x='day',y='total_bill')
plt.show()

# abhi Yaha Mai Dekh Raha Hun Ki Ye Bahut Faile Huye Hai 
# Ek para meter hai Esse samate ne ke liye 

sns.stripplot(data=tips, x='day',y='total_bill', jitter='False')
plt.show()

# using catplot
# figure level function
sns.catplot(data=tips, x='day',y='total_bill',kind='strip')


# jitter : Jitna Jitter ka value badhte jaoge uthna hi ye aur felte jate hia 
sns.catplot(data=tips, x='day',y='total_bill',kind='strip',jitter=0.2,hue='sex')

# swarmplot  # Ye Apko Thoda Better Represention Eske Andhar algo chal rahi hoti hai ess wajha se essa hota hai 
sns.catplot(data=tips, x='day',y='total_bill',kind='swarm')

# Ye Same Fuction aap Axis level pe bhi run kar sakte ho 
sns.swarmplot(data=tips, x='day',y='total_bill')

# hue
sns.swarmplot(data=tips, x='day',y='total_bill',hue='sex')