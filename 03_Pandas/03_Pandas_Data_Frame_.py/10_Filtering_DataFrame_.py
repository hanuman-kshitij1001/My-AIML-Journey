import pandas as pd
ipl = pd.read_csv("03_Pandas/03_Pandas_Data_Frame_.py/02_Data_set_IPL_.csv")
movies = pd.read_csv("03_Pandas/03_Pandas_Data_Frame_.py/03_Data_Set_movies_.csv")
student_data = [  
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,50,2]
]
student_dict = {
    'name':['nitish','ankit','rupesh','rishabh','amit','ankita'],
    'iq':[100,90,120,80,0,0],
    'marks':[80,70,100,50,0,0],
    'package':[10,7,14,2,0,0]
}
students1  = pd.DataFrame(student_data, columns=['iq','marks', 'package'])
students2 = pd.DataFrame(student_dict)



# Ab Haam Yaha Se Fiter karna sikhre Honge 
# Apko Data Milega Logical Basis Pe apko Yah Data Ko filter karn ahonga 

# Chalo Apne IPL wale DataSet Pe kaam KArte hai 

#Q1: Find all the final winners 

# Sabse pahle App ye paat karoge ki kon se matches final hai 
a = ipl['MatchNumber'] == 'Final'
print(a)
# OR
print(ipl[ipl['MatchNumber'] == 'Final'])
# OR
new_df = ipl[a]
print(new_df)

#ab mujhe yaha do session or Wining nikalne hai toh mai Yaha pe Fancy indeing lagaunga 
print(new_df[['Season', 'WinningTeam']])


# agr mai Es Pure COde Ek Line me likhna ho toh 

ans = ipl[ipl['MatchNumber'] == 'Final'][['Season','WinningTeam']]
print(ans)


#Q2: # how many super over finishes have occured
# Out of all the Matches me Se kitne me se supper over hua hai 
# Tarika Kya hia Mujhe Apne IPL Wale Data frame Me jana Honga Waha Jake Dekhna Honga Ki Kon Sa Col Hai Jo Es Information ko De raha hai 
# Apne Dekha Apke Pass EK Super over karke col hai jisme Values hai Y OR N karke Samjha 
# Ab Code se kaise Fetach karna honga I will Show U 
sv = ipl['SuperOver'] == 'Y'
print(sv) # yaha Se wo boolean ki series mil jayegi jaha jaha pe super over hua hai 
# ab mujhe ye batna hai Ki Kitne number of matches hai agr mai eske upper rows laga du 
sv = sv = ipl[ipl['SuperOver'] == 'Y'].shape[0]
print("Super Over:",sv)


#Q3 # how many matches has csk won in kolkata
# Hame Ye nikalna Hai ki CHaennai Super king ne Kolkats me match jite hai 
location =  ipl['City'] =='Kolkata'
print(location)
# but ab mujhe esi team chahiye jo shir chai 
ans = ipl[(ipl['City'] == 'Kolkata') & (ipl['WinningTeam'] == 'Chennai Super Kings')].shape[0]
print("CSK ne Kolkata me " ,ans, "Jite")

#Q4: # toss winner is match winner in percentage
Winner = (ipl[ipl['TossWinner'] == ipl['WinningTeam']].shape[0]/ipl.shape[0])*100
print(Winner)

#Q4: # movies with rating higher than 8 and votes>10000
ans = movies[(movies['imdb_rating'] > 8.5) & (movies['imdb_votes'] > 10000)].shape[0]
print(ans)


#Q5: Action movies with rating higher than 7.5
# mask1 = movies['genres'].str.split('|').apply(lambda x:'Action' in x)
mask1 = movies['genres'].str.contains('Action')
mask2 = movies['imdb_rating'] > 7.5

movies[mask1 & mask2]


#Q6: write a function that can return the track record of 2 teams against each other
