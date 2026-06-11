import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#2: Data set 
df = batter = pd.read_csv("04_Matplotlib/01_Plotting_using_Matplotlib/My_Data_Set/02_batter.csv")
df = df.head(50)
print(df)


plt.scatter(df['avg'],df['strike_rate'],color='red',marker='o')
plt.title('Avg and SR analysis of Top 50 Batsman')
plt.xlabel('Average')
plt.ylabel('SR')
plt.show()

