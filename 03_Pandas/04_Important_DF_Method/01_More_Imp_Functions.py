# value_counts
# sort_values
# rank
# sort index
# set index
# rename index -> rename
# reset index
# unique & nunique
# isnull/notnull/hasnans
# dropna
# fillna
# drop_duplicates
# drop
# apply
# isin
# corr
# nlargest -> nsmallest
# insert
# copy

# Each one of them is Important 
# Agr Ye 20+ function Acche se use karna a gaye toh app data set bahut acche se usse aur maupulate kar paoge 

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
marks = pd.DataFrame([
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,70,14],
    [80,70,14]
],columns=['iq','marks','package'])
ipl = pd.read_csv("03_Pandas/04_Important_DF_Method/02_Data_set_IPL_.csv")
movies = pd.read_csv("03_Pandas/04_Important_DF_Method/03_Data_Set_movies_.csv")
health = pd.read_csv("03_Pandas/04_Important_DF_Method/04_DataSet_Health.csv")

# Method 1: value_counts(series and dataframe)
# Har Unique Item ki Freq Ka Count nikal ke deta hai 
# JAise haam marks Wale Pe Chalene Wale hai 
a = marks.value_counts()  # Ye Pure Rows Ka Freq Count nikal Raha hai 
                          # Ye bahut usse full nahi rahta hai Pure data frame p elagta hia esliye But hn ye series me Kaam KArta hai 
print(a)


#Q1 : # find which player has won most potm -> in finals and qualifiers
      # Hame Uss Player ka Name Niklna JIsne Ipl Ke Final ya Semi-final usme sabse jada man of the matach award jite hai 

a = ipl[~ipl['MatchNumber'].str.isdigit()]['Player_of_Match'].value_counts()
print(a)

#Q2 Toss Jitne Ke baad Team Bating Karti ya Balling karti hai aur fhir espe char banna hai
# Yaha Ek Col hai Toss Dicision Jo ye Bata raha hai ki Team Jitne ke baad balling kar rahi hia ye bating 
# Chalo mai toss dission wale value pe value count laga dunga ye automatic mujhe bat denga kitni baar batinga kari hai 
# aur kitni balling 
b = ipl['TossDecision'].value_counts().plot(kind='pie')

print(b)
# plt.show()


#Q3 : # how many matches each team has played
c = (ipl['Team2'].value_counts() + ipl['Team1'].value_counts()).sort_values(ascending=False)
(ipl['Team2'].value_counts() + ipl['Team1'].value_counts()).sort_values(ascending=False).plot(kind='pie')
# print(c)
# plt.show()



#Method 2: sort_value ( series aur df dono pe applicable hai)
x = pd.Series([12,14,1,56,89])
print(x.sort_values(ascending=False))

# Chalo esse Data Frame Pe kaam karte hai chalo haam movies wala data uthate hai 
print(movies.head(4))

# Ab Haam Dekhte Hai Ki kaise Espe Sort values apply karte hai 
# Sabse pahele mai Single col pe chata hun phir multiple col pe bhi kaam karenge 
# Mujhe ye chaliye Mera Data Solve ho Jaye Col Ke hisab se 
print(movies.sort_values(['title_x']))
# THis Is The way To Sort data frame On the basis of 1 col 

students = pd.DataFrame(
    {
        'name':['nitish','ankit','rupesh',np.nan,'mrityunjay',np.nan,'rishabh',np.nan,'aditya',np.nan],
        'college':['bit','iit','vit',np.nan,np.nan,'vlsi','ssit',np.nan,np.nan,'git'],
        'branch':['eee','it','cse',np.nan,'me','ce','civ','cse','bio',np.nan],
        'cgpa':[6.66,8.25,6.41,np.nan,5.6,9.0,7.4,10,7.4,np.nan],
        'package':[4,5,6,np.nan,6,7,8,9,np.nan,np.nan]

    }
)
print(students.sort_values('name'))
print(students.sort_values('name',na_position='first',ascending=False)) # yaha Pe na wali values Sabse top ho jayegi

# ab Baat karte hai ki Multiple col se sorting karna hai toh kaise karenge 
# yaha Pe of release ka col hai tile ka col mai es dataset ko essa karna chahta hun ki soring hoo year ke hisab se 
# Phir mai kya karna chata hun ki uss movies me ghus ke sari movies ko alpha sort karunga 

print(movies.sort_values(['year_of_release','title_x'],ascending=[True,False]))