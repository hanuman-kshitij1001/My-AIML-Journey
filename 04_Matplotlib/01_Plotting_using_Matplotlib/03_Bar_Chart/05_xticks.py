import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# a problem
children = [10,20,40,10,30]
colors = ['red red red red red red','blue blue blue blue','green green green green green','yellow yellow yellow yellow ','pink pinkpinkpink']

plt.bar(colors,children,color='black')
plt.xticks(rotation='vertical')         # Yaha Vertical karne se hota kya hia ki ye ane Vertically a jate hai 
plt.show()



# Stacked Bar chart  # Esme Apasah Me Cheeze jud Jati hai 

#1: DataSet
df = batsman = pd.read_csv("04_Matplotlib/01_Plotting_using_Matplotlib/My_Data_Set/01_batsman_season_record.csv")

plt.bar(df['batsman'],df['2017'],label='2017')
plt.bar(df['batsman'],df['2016'],bottom=df['2017'],label='2016')
plt.bar(df['batsman'],df['2015'],bottom=(df['2016'] + df['2017']),label='2015')

plt.legend()
plt.show()