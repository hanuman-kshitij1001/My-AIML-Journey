# groupby on multiple cols

import pandas as pd
import numpy as np
dilivery = pd.read_csv("03_Pandas/05_Group_by_Objects/01_Data_Set_deliveries.csv")
imdb = pd.read_csv("03_Pandas/05_Group_by_Objects/02_Data_Set_imdb-top-1000.csv")
movies = pd.read_csv("03_Pandas/05_Group_by_Objects/03_Data_Set_movies_.csv")

genres = imdb.groupby('Genre')

duo = imdb.groupby(['Director','Star1'])
print(duo)

# size
duo.size()

# get_group
duo.get_group(('Aamir Khan','Amole Gupte'))

#Q1 # find the most earning actor->director combo
a = duo["Gross"].sum().sort_values(ascending=False).head(1)
print(a)

#Q 2:  find the best(in-terms of metascore(avg)) actor->genre combo
b = imdb.groupby(['Star1','Genre'])['Metascore'].mean().reset_index().sort_values('Metascore',ascending=False).head(1)
print(b)


# agg on multiple groupby
c = duo.agg(['min','max','mean'])
print(c)