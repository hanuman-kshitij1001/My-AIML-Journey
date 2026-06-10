# eske liya real word deta ka usse karne wale hai so 
# import titanic
import pandas as pd
import numpy as np
titanic = pd.read_csv("03_Pandas/07_Vector Str_DateTime_in_Pandas/02_Vector_String/Data_Set_titanic.csv")
print(titanic)

# # Common Functions

#1: # lower/upper/capitalize/title

df = titanic['Name']
print(df)


# aggr aap sare passange ka name capital me likhna chahate ho to 
df['Name'].str.lower()
df['Name'].str.upper()

df['Name'].str.capitalize() # kay karta hai sare word ka First letter capital me kar deta hai 
df['Name'].str.title() # kay karta hai sare word ka First letter capital me kar deta hai har word ka karega 


# mujhe us passenge ka name nikalna hai jika name sabse bada hai 
# toh sabse pahele 
# pahele name col me jaunga uske len pe jaunga fhir max pe jajunga 
df['Name'].str.len() == 82
# yaha se mujhe boolean series mila ab ai esse masking karne wala hun 

name = df['Name'][df['Name'].str.len() == 82].values[0]


# ek aur function Called  strip
# ye kya karta hai ki apke pass ek esa string hai jaise hi strip chalte ho 
# jitne bhi leading aur ending space hata deta hai 
# ye same kaam aap chalo toh col pe bhi kar sakte ho 

# ek aur function called split 
# ye kya karta hai ki name sur name , title , miss , title uske bad bande ka name ata hai 
# mia apne dataset me 3 naye col banne wale hia mai 3 chezo ko alag karna chahta hun 
# aap dekho toh sir name uar name , pe connected hai ]
# jaise hi comma pe split maroe surname alg ho jayega aur name alaga 
# ek function hong get wo name de denga str.get se 

# split -> get
df['lastname'] = df['Name'].str.split(',').str.get(0)

# ab mai title uar name ko alag alag col me dal raha hun toh kya karunga ki 
df[['title','firstname']] = df['Name'].str.split(',').str.get(1).str.strip().str.split(' ', n=1, expand=True)


# replace

# jaha mises honga usse wo miss se replace kar denga done 

df['title'].str.replace('Ms','Miss')



## filtering

# startswith/endswith
df[df['firstname'].str.endswith('A')]

# isdigit/isalpha...
df[df['firstname'].str.isdigit()]



# For Advance Level Fitering 
# uske liye mai applying regex

# cointains ka Use karke ap regex expresion pass karte ho
# # contains
# search john -> both case 
df[df['firstname'].str.contains('john',case=False)]

# find lastnames with start and end char vowel
df[df['lastname'].str.contains('^[^aeiouAEIOU].+[^aeiouAEIOU]$')]


# yaha pe Slicing bhi kar sakte ho

# slicing
df['Name'].str[::-1]