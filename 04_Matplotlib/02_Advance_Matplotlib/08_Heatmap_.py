# Heatmap : Google Seach Kar lena bhai 


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

iris = pd.read_csv("04_Matplotlib/02_Advance_Matplotlib/All_dataSet/01_iris.csv")
batter = pd.read_csv("04_Matplotlib/02_Advance_Matplotlib/All_dataSet/02_batter.csv")
batsman_session = pd.read_csv("04_Matplotlib/02_Advance_Matplotlib/All_dataSet/03_batsman_season_record.csv")
ipl = pd.read_csv("04_Matplotlib/02_Advance_Matplotlib/All_dataSet/04_IPL_Ball_by_Ball_2008_2022.csv")


# Mia ye dekhan Chata hun Haar over ki Ball Par Kiten Chakke Lage hia haam Uska Graph Ploat karenge bhai 
# col me Honga bass 
# index me honga baal ka over 


temp_df = ipl[(ipl['ballnumber'].isin([1,2,3,4,5,6])) & (ipl['batsman_run']==6)]
temp_df

grid = temp_df.pivot_table(index='overs',columns='ballnumber',values='batsman_run',aggfunc='count')
# agr mai Eska Graph Ploat karu Toh 
plt.figure(figsize=(20,10))
plt.imshow(grid)
plt.yticks(ipl['overs'].unique(), list(range(1,21)))
plt.xticks(np.arange(0,6), list(range(1,7)))
plt.colorbar()
plt.show()