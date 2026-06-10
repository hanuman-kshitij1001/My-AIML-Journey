# The pivot table takes simple column-wise data as input, and groups the entries into a two-dimensional table that provides a multidimensional summarization of the data.

# 1. Pivot Table Kya Hai?
#    Pivot Table ek data summarization tool hai jo large dataset ko summarize karne ke liye use hota hai.
#    Isse hum data ko different categories ke basis par aggregate kar sakte hain.

# Its Is a Super Usefull
# Ye Esa Kuch naya Offer nahi kar raha hai ye aap bana sajte ho jo app Pahele Usse kiye o usse bhi 
# Bass Ye pivot table Ek shorthnds provide karta hai 
# Ye Apko excel wagera me Direct dikhega Theek 

# yaha pe hamne Jo libraray import kari thi wo toh rahengi hi uske baad yaha pe ek lib import kane wale hai that is 
# import seaborn as sns 
# Actually ye data visulization lib hai esse haam apne data ka visulization kar sakte hai 
# eske bare me detailed Study KArenge 
import numpy as np
import pandas as pd
import seaborn as sns

# aaj Haam Esse Visulization ke liye nahi balki mai Esse ESke andhr ki ek Cheez hai  uuse use karne ke liye import kar rhaa hun


# es baar jab haam yaha data frame banaiynge toh pd se nahi sns se banayenge 
df = sns.load_dataset('tips')
df.head()

# seaborn ke kuch toys library built in ate hai 
# ab Yah pe tips name ki ek library hai jaha Pe ek pure time period me jitne bhi customer aye hai unka detailed note down kiya hai 
# Esme Ye sab data hai 
# Ye apke Liye Ek good data Hai 

# pivot table samjhne ke liye ek ex lete hai 
# agr mujhe gender ke basis pe average total bill 
# jitne bhi mere female custo hai wo on the whole kitna bill pay karti hia aur 
# same male also 


# Do 3 tarike hai unme se sabse asan tarika hai ap group by kar do 
result = df.groupby('sex')[['total_bill']].mean()
print(result)

# esme se jo smoker male hai wo kitna bill pay karti hai same for female also smoker aur non smokker dono ke liye 

result = df.groupby(['sex','smoker'])[['total_bill']].mean()
print(result)

# ab Apko multi index data frame dikh raha honga 
# ab agr aap esse sahi formate me dekhna chate ho toh aap unstack() ko call kar do 
# unstack kya karega ye jo andhar wala index hai boundray ke sare pahle wala esko andhr wala row bana denaga 
result = df.groupby(['sex','smoker'])[['total_bill']].mean().unstack()
print(result)


# agr apko pata karna hia ki average male smoke pe kitan kharchakarta hai 

result = df.groupby('sex','smoker')
print(result)

# reather than Use Ye sab Ap pivort tabel usse karo 
# pivot table me apko 3 cheeze batni hoti hai 
# 1: index kon sa col banega = sex wala 
# 2: col kon sa col banega  = yes or no as an Smoker
# 3: value kya

result = df.pivot_table(index='sex',columns='smoker',values='total_bill',observed=True)
print(result)
# you can see Excatly same result Theek hai na 

#esme 
# multindeing
# margins
# Esme Ploting bhia padhaya hai sirne theek hai na han ji 

