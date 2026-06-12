import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

iris = pd.read_csv("04_Matplotlib/02_Advance_Matplotlib/All_dataSet/01_iris.csv")
batter = pd.read_csv("04_Matplotlib/02_Advance_Matplotlib/All_dataSet/02_batter.csv")
batsman_session = pd.read_csv("04_Matplotlib/02_Advance_Matplotlib/All_dataSet/03_batsman_season_record.csv")
ipl = pd.read_csv("04_Matplotlib/02_Advance_Matplotlib/All_dataSet/04_IPL_Ball_by_Ball_2008_2022.csv")


# A diff way to plot graphs
batter.head()

plt.figure(figsize=(15,6))
plt.scatter(batter['avg'],batter['strike_rate'])
plt.title('Something')
plt.xlabel('Avg')
plt.ylabel('Strike Rate')

plt.show()



fig,ax = plt.subplots(figsize=(15,6))

ax.scatter(batter['avg'],batter['strike_rate'],color='red',marker='+')
ax.set_title('Something')
ax.set_xlabel('Avg')
ax.set_ylabel('Strike Rate')

fig.show()



# Mai yaha Ek Hi Figure me Do 3 -4 graphs plot karna chahta hun theek hai na kaise karunga wo Cheeze Yah Mai Sikhne ja Rhaa hun Done 

fig, ax = plt.subplots(nrows=2,ncols=1,sharex=True,figsize=(10,6))

ax[0].scatter(batter['avg'],batter['strike_rate'],color='red')
ax[1].scatter(batter['avg'],batter['runs'])

ax[0].set_title('Avg Vs Strike Rate')
ax[0].set_ylabel('Strike Rate')


ax[1].set_title('Avg Vs Runs')
ax[1].set_ylabel('Runs')
ax[1].set_xlabel('Avg')

plt.show()





fig, ax = plt.subplots(nrows=2,ncols=2,figsize=(10,10))

ax[0,0].scatter(batter['avg'],batter['strike_rate'],color='red')
ax[0,1].scatter(batter['avg'],batter['runs'])
ax[1,0].hist(batter['avg'])
ax[1,1].hist(batter['runs'])
plt.show()




fig = plt.figure()

ax1 = fig.add_subplot(2,2,1)
ax1.scatter(batter['avg'],batter['strike_rate'],color='red')

ax2 = fig.add_subplot(2,2,2)
ax2.hist(batter['runs'])

ax3 = fig.add_subplot(2,2,3)
ax3.hist(batter['avg'])
plt.show()



fig, ax = plt.subplots(nrows=2,ncols=2,sharex=True,figsize=(10,10))

ax[1,1]
plt.show()