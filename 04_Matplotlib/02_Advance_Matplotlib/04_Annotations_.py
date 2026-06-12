# Anotaion :

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

iris = pd.read_csv("04_Matplotlib/02_Advance_Matplotlib/All_dataSet/01_iris.csv")
batter = pd.read_csv("04_Matplotlib/02_Advance_Matplotlib/All_dataSet/02_batter.csv")

# Maine Yaha Sikha ki kaise maine point ko lable kar diya 
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
plt.scatter(x,y)
plt.text(1,5, 'Point 1')
plt.text(2,6, 'Point 1')
plt.text(3,7, 'Point 1')
plt.text(4,8, 'Point 1', fontdict={'size':12, 'color':'red'})
plt.show()


# Chalo ab Haam batter pe kaam karte hia 
plt.scatter(batter['avg'], batter['strike_rate'])
# mai yaha manula 100 ko lable nahi karuna Uske liye Loop lagauga Theek hai 
for i in range(batter.shape[0]):
    plt.text(batter['avg'].values[i], batter['strike_rate'].values[i], batter['batter'].values[i])

plt.show()


# abhi For better stauation ke liye size ko change kar sakte ho 

plt.figure(figsize=(25,20))
plt.scatter(batter['avg'], batter['runs'])
# mai yaha manula 100 ko lable nahi karuna Uske liye Loop lagauga Theek hai 
for i in range(batter.shape[0]):
    plt.text(batter['avg'].values[i], batter['runs'].values[i], batter['batter'].values[i])

plt.show()