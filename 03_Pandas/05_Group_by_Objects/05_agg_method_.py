import pandas as pd
import numpy as np
dilivery = pd.read_csv("03_Pandas/05_Group_by_Objects/01_Data_Set_deliveries.csv")
imdb = pd.read_csv("03_Pandas/05_Group_by_Objects/02_Data_Set_imdb-top-1000.csv")
movies = pd.read_csv("03_Pandas/05_Group_by_Objects/03_Data_Set_movies_.csv")
genres = imdb.groupby('Genre')
# agg method

# passing dict

a = genres.sum(numeric_only=True)
print(a)

b = genres.agg(
    {
        'Runtime':'mean',
        'IMDB_Rating':'mean',
        'No_of_Votes':'sum',
        'Gross':'sum',
        'Metascore':'min'
    }
)
print(b)


# passing list
# c = genres.agg(['min','max','mean','sum'])
# print(c)


# # Adding both the syntax

m = genres.agg(
    {
        'Runtime':['min','mean'],
        'IMDB_Rating':'mean',
        'No_of_Votes':['sum','max'],
        'Gross':'sum',
        'Metascore':'min'
    }
)
print()
print()
print(m)