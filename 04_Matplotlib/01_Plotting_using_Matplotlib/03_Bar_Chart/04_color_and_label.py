# color and label

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#1: DataSet
df = batsman = pd.read_csv("04_Matplotlib/01_Plotting_using_Matplotlib/My_Data_Set/01_batsman_season_record.csv")


plt.bar(np.arange(df.shape[0]) - 0.2,df['2015'],width=0.2,color='orange')
plt.bar(np.arange(df.shape[0]),df['2016'],width=0.2,color='red')
plt.bar(np.arange(df.shape[0]) + 0.2,df['2017'],width=0.2,color='blue')

plt.xticks(np.arange(df.shape[0]), df['batsman'])

plt.show()


print(np.arange(df.shape[0]))

