# dropna(series + dataframe) -> how parameter -> works like or

# Ab Agr missing value hia toh karna kya hai 
# Do method haam disccus karenge JIsse ap Future me bahut use karoge 
# 1 dropna
# 2 fillna

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

# abhi mujhe kya karna hai eske sare missig values ko hatna hai 
a = students['name']
# abhi maine name ka Col print kara diya hai 
print(a)
# ab Mai Yaha Se missing values hata dunga 
a = students['name'].dropna()
print(a)
# ab Dekhoge toh output haat chuka hai 


# ab Mai Pure ke pure Data Ke Frame ke uppar dropna aply karunga 
#Note: kiss bhi Row me agr ek bhi missing value hai toh pura ka ura row haat deta hai 
a = students.dropna()  # how likha jata by defaut wo any hota hia 
print(a)
# dekha sara data hata diya 

# but mai esse hatna hai jaha par sari ki sari values missing hai 
a = students.dropna(how='all')
print(a)


# aap kiss particula col bhi sambhal sakte ho 
# yahi wo char row hai col ke name koi value nahi hai 

a = students.dropna(subset=['name'])
# shif wahi row bach gaye jaha name ka value missing nahi tha
print(a)

# haam us rows ko hatna chate hia jaha name me missing hai or college me missing bass 
a = students.dropna(subset=['name','college'])
print(a)

# note ye Sab Permant opretion nahi huye hai kyu maine inplace changes nahi hai agr aap student print karoge toh apko wahi same data milega 