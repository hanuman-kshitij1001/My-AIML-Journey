import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

iris = pd.read_csv("04_Matplotlib/02_Advance_Matplotlib/All_dataSet/01_iris.csv")
batter = pd.read_csv("04_Matplotlib/02_Advance_Matplotlib/All_dataSet/02_batter.csv")


plt.figure(figsize=(18,10))
plt.scatter(batter['avg'],batter['strike_rate'],s=batter['runs'])

plt.axhline(130,color='red')
plt.axhline(140,color='green')
plt.axvline(30,color='red')

for i in range(batter.shape[0]):
  plt.text(batter['avg'].values[i],batter['strike_rate'].values[i],batter['batter'].values[i])

plt.show()