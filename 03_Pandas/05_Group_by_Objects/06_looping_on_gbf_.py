import pandas as pd
import numpy as np
dilivery = pd.read_csv("03_Pandas/05_Group_by_Objects/01_Data_Set_deliveries.csv")
imdb = pd.read_csv("03_Pandas/05_Group_by_Objects/02_Data_Set_imdb-top-1000.csv")
movies = pd.read_csv("03_Pandas/05_Group_by_Objects/03_Data_Set_movies_.csv")

genres = imdb.groupby('Genre')

for group, data in genres:
    # print(type(group), type(data))
    print(data)

# Chalo ek Quesion Karte hai 
# mujhe g ka Hiestes Rated movies nikalni hai 

df = pd.DataFrame(columns=imdb.columns)
for group, data in genres:
    top_movie  = data[data['IMDB_Rating'] == data['IMDB_Rating'].max()]
print(df)


# latest pandas me append haat gaya hai Esliye Concat likha hai append haatta ke 