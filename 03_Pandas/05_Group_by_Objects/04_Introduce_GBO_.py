# what is GBO : 
# hamne abhi taak jo kiya unhe alg kiya 
# aaj Se haam Sikh rahe honge ki Grop me kam kaise karte hai 
# thid grooup by is very similar to Data base also 
# aaj Ke class me Jada THeory nahi hai That is Hand on Practice are there

# Sabse pahle Apko Dono library import karna hai 

import pandas as pd
import numpy as np

# fhir ye dono dataset import karne honge thaeek hai na 

dilivery = pd.read_csv("03_Pandas/05_Group_by_Objects/01_Data_Set_deliveries.csv")
imdb = pd.read_csv("03_Pandas/05_Group_by_Objects/02_Data_Set_imdb-top-1000.csv")
movies = pd.read_csv("03_Pandas/05_Group_by_Objects/03_Data_Set_movies_.csv")


# In First of the class haam movies wale pe kam karenge aur 
# in Mid of the Class Haam age ono pe kaam karne wale hai 


# Group by me aap kya karte ho data  ke adhar kissi col ke basis pe group form karte ho 
# ab kon se tyepes ko use karoge aap group form karene ke liye 
# bahut simple  hai genrally Apke pass do types ke col honga ek numrical aur dusra honga catigorical data (beacuse jaha pe catory ho) 
# agr apse koi puch group by kiss  pe lagega hamesh apka answer hona chahiye group apply hota hia catogorical col pe 
# kyu ki aap khud socho na ki aap group kiss basis pe bana sakte ho catogory ke basis pe na same yaha bhi wahi honga clear

# Ye List provide kar deta hia Ki Apke data me kon kon se col hai 
print(movies.columns.tolist())

# ye Kya KArta hai ki "Movies ko genre ke hisab se alag-alag buckets (groups) me baant do."
# Uske baad tum har bucket par operation kar sakte ho:

movies.groupby('genres')
print(movies)

# # Applying builtin aggregation fuctions on groupby objects
a = movies.groupby('genres').sum()
print(" ", a) 


# Similaraly yaha Pe mean Apply kar sakte ho 
b = movies.groupby('genres').mean(numeric_only=True)
print(b)


# find the top 3 genres by total earning
print()
top3 = movies.groupby('genres')['imdb_votes'].sum().sort_values(ascending=False).head(3)
print(top3)
# esko solve karne ka Do tarika hia Ek Toh ye hia 
# ek Aur tarika hai Eska Ulta karo Bhai 

ans = movies.groupby('genres')['imdb_votes'].sum().sort_values(ascending=False).head(3)
print(ans)


#Q3:  # find the genre with highest avg IMDB rating
a = movies.groupby('genres')['imdb_rating'].mean().sort_values(ascending=True).head()
print(a)

#Q4: # find director with most popularity poup ko haam kissi bhi ko supose kar lenge 
a = imdb.groupby('Director')['No_of_Votes'].sum().sort_values(ascending=False).head(1)
print(a)

#Q5: find the highest rated movie of each genre
#    Ek Tarika ye bhai hai 
#    movies.groupby('Genre')['IMDB_Rating'].max()
#    sir ne bola hai iese haam bad me kaenge 

#Q6: find number of movies done by each actor
# movies['Star1'].value_counts()
a = imdb.groupby('Star1')['Series_Title'].count().sort_values(ascending=False)
print(a)

#Q7: # find total number of groups -> len
print(len(imdb.groupby("Genre")))


#Q8: # find items in each group -> size
a = imdb.groupby('Genre').size()
print(a)


#Q 9: first()/last() -> nth item

# Ham Log genres ka Goup banate hai usse group by kar denge jisse bar bar nahi likhna padega

genres = imdb.groupby('Genre')
# genres.first()
# genres.last()
print(genres.nth(6))

print(genres.groups)

print(genres.describe())

print(genres.sample(2,replace=True))

print(genres.nunique())
