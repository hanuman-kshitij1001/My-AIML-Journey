# Categorical Estimate Plot -> for central tendency ko measure karna 
# Barplot
# Pointplot
# Countplot


import seaborn as sns

import matplotlib.pyplot as plt
import plotly.express as px

# import datasets
tips = sns.load_dataset('tips')
iris = sns.load_dataset('iris')


#1- # barplot
sns.barplot(data=tips, x='sex', y='total_bill')
plt.show()
# Ye Note for upper jo black wali dandi hai uske liye hai
# Note : When there are multiple observations in each category, it also uses bootstrapping to compute a confidence interval around the estimate, which is plotted using error bars

#  some issue with errorbar
import numpy as np
sns.barplot(data=tips, x='sex', y='total_bill',hue='smoker',estimator=np.min)


## point plot
# ye Bar ka hi bhai bass ye minus the bars matlb sab same bass bar ke badle point a jatahai 
sns.pointplot(data=tips, x='sex', y='total_bill',hue='smoker',ci=None)
plt.show()

# countplot
sns.countplot(data=tips,x='sex',hue='day')
plt.show()

# faceting using catplot
sns.catplot(data=tips, x='sex',y='total_bill',col='smoker',kind='box',row='time')
plt.show()