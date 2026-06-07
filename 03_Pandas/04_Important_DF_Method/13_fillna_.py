# fillna(series + dataframe)

# Ab Agr missing value hia toh karna kya hai 
# Do method haam disccus karenge JIsse ap Future me bahut use karoge 
# 1 dropna
# 2 fillna

# Fillna Ki khanai hai ki kyu missing data ko hatna Usse fill in kartehai 

import pandas as pd
import numpy as np

students = pd.DataFrame(
    {
        'name':['nitish','ankit','rupesh',np.nan,'mrityunjay',np.nan,'rishabh',np.nan,'aditya',np.nan],
        'college':['bit','iit','vit',np.nan,np.nan,'vlsi','ssit',np.nan,np.nan,'git'],
        'branch':['eee','it','cse',np.nan,'me','ce','civ','cse','bio',np.nan],
        'cgpa':[6.66,8.25,6.41,np.nan,5.6,9.0,7.4,10,7.4,np.nan],
        'package':[4,5,6,np.nan,6,7,8,9,np.nan,np.nan]

    }
)

a = students['name'] 
print(a) 
# yaha Maine Dekha Ki name Me 3 na value 
# ab Mai Esee fillna karne wala hun tell see
ans = students['name'].fillna('unknown')
print(ans)
# aacha toh nan likhne ke bajaye ye waha value fhil kar raha hai value ka name hai unknow 
# Ek kaam karo kshitij ya Kuch aur date hai jaise Etc 
# chalo dataframe pe laga ke dekh lete hai 

ans = students.fillna('tiwari')
print(ans)
# jaha jaha missing values this apne sabko tiwai se replace kar diya 
# waise ye df me karna sahi nahi hai it advice aap col by col basis pe handle karo jada accha honga theek hai na 

ans = students['package'].fillna(students['package'].mean())
print(ans)

students['name'].fillna(method='ffill')
# ya kya karta hai upaer ka Dekh ke niche daal detahai 

students['name'].fillna(method='bfill')
# ye kya karta hai niche ka upar daal deta hai 

# simple hai aaj toh samjhme a raha hai acche se Yeah 
