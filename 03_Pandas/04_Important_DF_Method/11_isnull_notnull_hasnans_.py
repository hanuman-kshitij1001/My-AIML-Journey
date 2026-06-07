# isnull(series + dataframe)
# notnull(series + dataframe)
# hasnans(series)
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


#1:
print(students)

#1:
ans = students['name'].isnull()
print(ans)
# Ye Jaha Jaha False Hai Waha Missing Value Nahi HAi Jaha jaha True aya Hia Waha Missing Value hongi 
#


# notnull # Eska Ulta puchta hia 
# agr notnull honga toh missing hia toh true denga warna false denga 
ans = students['name'][students['name'].notnull()]
print(ans)

#3: Yes ya No Me ye batayega ki apke col me koi bhi missing value Hai Ya Nahi 
#   hogi toh true warna false Simple
ans = students['name'].hasnans
print(ans) # Ture


# ab mai pure data fram me lagata hun 
ans = students.isnull()
print(ans)

# same cheez aap not null pe bhi laga sakte ho 
ans = students.notnull()
print(ans)

# yaha hashnan nahi hota hai yaha pe theek na 
# Hashnan shirf sereis me hota hai pure ke pure data frame pe nahi chalta hai 

# Ab Agr missing value hia toh karna kya hai 
# Do method haam disccus karenge JIsse ap Future me bahut use karoge 
# 1 dropna
# 2 fillna