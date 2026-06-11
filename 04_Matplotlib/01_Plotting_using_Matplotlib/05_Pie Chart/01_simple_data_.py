# Univariate/Bivariate Analysis
# Categorical vs numerical
# Use case - To find contibution on a standard scale

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = [23,45,100,20,49]
subjects = ['eng','science','maths','sst','hindi']
plt.pie(data,labels=subjects)

plt.show()


# dataset

#5: DataSet
df = gayle = pd.read_csv("04_Matplotlib/01_Plotting_using_Matplotlib/My_Data_Set/05_gayle-175.csv")

plt.pie(df['batsman_runs'],labels=df['batsman'],autopct='%0.1f%%')
plt.show()




## percentage and colors
plt.pie(df['batsman_runs'],labels=df['batsman'],autopct='%0.1f%%',colors=['blue','green','yellow','pink','cyan','brown'])
plt.show()




# explode shadow
plt.pie(df['batsman_runs'],labels=df['batsman'],autopct='%0.1f%%',explode=[0.3,0,0,0,0,0.1],shadow=True)
plt.savefig('Sample.png')
plt.show()
