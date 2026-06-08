# split (apply) combine
# apply -> builtin function

import pandas as pd
import numpy as np
dilivery = pd.read_csv("03_Pandas/05_Group_by_Objects/01_Data_Set_deliveries.csv")
imdb = pd.read_csv("03_Pandas/05_Group_by_Objects/02_Data_Set_imdb-top-1000.csv")
movies = pd.read_csv("03_Pandas/05_Group_by_Objects/03_Data_Set_movies_.csv")

genres = imdb.groupby('Genre')

df = genres.apply(min)
print(df)
# Ye Dono Same Hi Cheeze hai 
df = genres.min(numeric_only=False)
print(df)


#Q1:  find number of movies starting with A for each group
def foo(group):
  print(group)
  return group
df = genres.apply(foo)
print(df)

# dusra tarika 
def foo(group):
  return group['Series_Title'].str.startswith('A').sum()
  
df = genres.apply(foo)
print(df)

# # find ranking of each movie in the group according to IMDB score

def rank_movie(group):
  group['genre_rank'] = group['IMDB_Rating'].rank(ascending=False)
  return group
genres.apply(rank_movie)


# find normalized IMDB rating group wise
def normal(group):
  group['norm_rating'] = (group['IMDB_Rating'] - group['IMDB_Rating'].min())/(group['IMDB_Rating'].max() - group['IMDB_Rating'].min())
  return group
# Check Normalization Formula bro 

print()
print()
print(genres.apply(normal))