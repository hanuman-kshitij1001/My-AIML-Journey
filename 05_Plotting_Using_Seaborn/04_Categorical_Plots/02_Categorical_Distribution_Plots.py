# Categorical Distribution Plots
# 1. Boxplot
# 2. Violinplot

# Box Plot — Short Summary

# Box Plot ek statistical graph hai jo data distribution ko five-number summary ki madad se dikhata hai:

# Minimum (sabse chhoti value)
# Q1 (First Quartile) – 25% data iske neeche hota hai
# Median (Q2) – beech ki value
# Q3 (Third Quartile) – 75% data iske neeche hota hai
# Maximum (sabse badi value)

# Box plot se hum:

# Data ka spread (dispersion) dekh sakte hain
# Outliers identify kar sakte hain
# Data symmetric hai ya skewed hai, ye samajh sakte hain
# Data kitna clustered ya spread out hai, ye dekh sakte hain
# One-line Notes

# Box Plot: A visualization that summarizes a dataset using the five-number summary and helps identify distribution, spread, skewness, and outliers.

import seaborn as sns

import matplotlib.pyplot as plt
import plotly.express as px

# import datasets
tips = sns.load_dataset('tips')
iris = sns.load_dataset('iris')

# Box plot4
sns.boxplot(data=tips,x='day',y='total_bill')
plt.show()

# Using catplot
sns.catplot(data=tips,x='day',y='total_bill',kind='box')
# Bass kind me box dal do ho jata hai 


# hue
sns.boxplot(data=tips,x='day',y='total_bill',hue='sex')
plt.show()

# single boxplot -> numerical col
sns.boxplot(data=tips,y='total_bill')
plt.show()



#2- Violinplot = (Boxplot + KDEplot) <> 
# violinplot 
sns.violinplot(data=tips,x='day',y='total_bill')
plt.show() # Esko Bola Jata hai voilinplot
# Yaha Becch me Jo Dikhai De raha hia Wo Box hai Ye 
# Curve kde hai jo data Ka Ditribution dikha raha hai 


# Now Run This Code With The Help of catplot
sns.catplot(data=tips,x='day',y='total_bill',kind='violin')

# Now move TO add hue parameter
# # hue
sns.catplot(data=tips,x='day',y='total_bill',kind='violin',hue='sex',split=True)
# Yaha split true karne se side by side do graph ban jayenge theek 
plt.show()
# Note : I Have use box Plot jada voil.... se 

