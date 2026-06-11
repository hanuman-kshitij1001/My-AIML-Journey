# Agr Ap Chalo Toh Grid On Kar sakte Ho "
# For Information ko Acche se Dikhne ke liye "
# Readablity badhta hai 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

price = [48000,54000,57000,49000,47000,45000,4500000]
year = [2015,2016,2017,2018,2019,2020,2021]
plt.plot(price, year)
plt.title('The Graph Is Showing How Grid Works')
plt.xlabel('price')
plt.ylabel('year')

plt.grid()
plt.show()


# Data Set
sharma_k = pd.read_csv("04_Matplotlib/01_Plotting_using_Matplotlib/My_Data_Set/06_sharma-kohli.csv")
plt.plot(sharma_k['index'],sharma_k['V Kohli'],color="#F18F0F",linestyle='solid',linewidth=1,marker='o',markersize=4)
plt.plot(sharma_k['index'],sharma_k['RG Sharma'],color="#009BFC",linestyle='dashdot',linewidth=2,marker='*')

plt.title('The Graph Is Showing How Grid Works')
plt.xlabel("X-Axis")
plt.ylabel('Y-Axis')
plt.show()

