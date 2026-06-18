import requests  # Esse haam htpp req karte using python
import pandas as pd

response = requests.get('https://api.themoviedb.org/3/movie/popular?api_key=9c3510b4224a5c362c701d95238b950d')
# Ab Jaise Hi Esko Run Karo Toh Hota kya hai 
# Python request library ka Usee karke Https pe request maar raha hia uss api pe aur Api palt kar data denga jo data hame yaha pe dikhai denga
# Jab Mai Esse Run Karung 

data = response.json()
print(data)



movies_result  = response.json()['results']
# Ye Kaya karega Esse shirf result ko dikhayega 
print(movies_result)

# Ab ess movies ko pandas me late hai 
df = pd.DataFrame(movies_result)
print(df)

#
jo_chahiye = pd.DataFrame(response.json()['results'])[['id', 'title', 'overview', 'release_date', 'popularity','vote_average', 'vote_count']]
print(jo_chahiye)

# Ab Bass Muje Kya karna hai Ki mujhe ye kaam loop me karna hai 
# Aur loop Kitni Bar Chalega Jitne pages honge 
# har baar loop ke andhar ek Naya Df banayenge 
# Aur usse purane data frame me append kar denge 
# last me when loops end we create a larg df of 8000 movies

# step 1: mia Yaha pe Empty df baana raha hun theek hai 
df = pd.DataFrame() 

# step 2: mai ab ek Loop Chala raha hun 
for i in range(1, 429):
    # har baar loop ke ander mai es url pe hi karunga 
    response = requests.get('https://api.themoviedb.org/3/movie/popular?api_key=9c3510b4224a5c362c701d95238b950d&language=en-US&page={}'.format(i))   # matlb jo bhi i ka value honga wahi mera page number honga theek 
    temp_df = pd.DataFrame(response.json()['results'])[['id', 'title', 'overview', 'release_date', 'popularity','vote_average', 'vote_count']]
    df = df.concat(temp_df, ignore_index=True)





