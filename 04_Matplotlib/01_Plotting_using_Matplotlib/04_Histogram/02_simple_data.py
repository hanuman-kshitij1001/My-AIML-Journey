# simple data

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = [32,45,56,10,15,27,61]
plt.hist(data,bins=[10,25,40,55,70])
plt.show()


# on some data
#7: DataSet
df = vk = pd.read_csv("04_Matplotlib/01_Plotting_using_Matplotlib/My_Data_Set/07_vk.csv")
plt.hist(df['batsman_runs'],bins=[0,10,20,30,40,50,60,70,80,90,100,110,120])
plt.show()


# handling bins
# logarithmic scale
plt.hist(vk,bins=[10,20,30,40,50,60,70],log=True)
plt.show()