# Pd . concat kya karta hai 
# kabhi bhi do data ko Vertically Jone ki Jarurat pade toh ye Function kam ata hai 
# Chalo jase hamare pass nov aur dec ka data hai Chalo haam usse Concat kar dete hai 
import pandas as pd
import numpy as np
nov = pd.read_csv("03_Pandas/06_Marg_joining_Conct_/All Data Sets/04_Data_Set_reg-month1.csv")
dec = pd.read_csv("03_Pandas/06_Marg_joining_Conct_/All Data Sets/05_Data_Set_reg-month2.csv")

df = pd.concat([nov,dec])

# jaise hi es Code ko run karunga Ye code vertically merge ho jayenge Theek 
# Ye Kitne Bhi File Kar sakta hai No limit 

print(df)

# Esme Ek Dikkat kya hoti hai ki Index Fhir Se 0 se  chalu ho jate after Adding 
# Ese Hatne Ke liye mere Pass Kush hai that is called 

df = pd.concat([nov, dec], ignore_index=True) # jab App True kar dete toh stacking ke baad naye index ayenge 
print(df)

# Ye Same Kaam Ap Append Ko Use karke Bhi Kar sakte ho 
# Ye haam Nahi Kar sakte hia Kyu Ki Appen Naye Version me hata diya gaya hai 
# df = nov.append(dec)
# print(df)
# Ese Yad Rakhna Ya Use Karna Koi Matlb hi nahi hai 


# mullitindex -> fetch using iloc

# What if Agr mujhe ye karna ho ki Exiting index ko Hatna Nahi chahta hun toh aap Kya Kroge ki 
# Original Rakhte huye bhi diff create kar sakte ho 
df = pd.concat([nov, dec], keys=['nov', 'dec'])
# aap Kya Bol rahe ho ki nov wale data frame ko provide this index and dec ko provide this index key me jo jiss jagha hai 
print(df)


multi = pd.concat([nov, dec], keys=['nov', 'dec'])
df = multi.loc['nov', 5]
print(df)

# a = multi.loc[('Dec', 5)]
# print(a)



# Ab Chalo Haam Side by side Jodana Chata hun toh mai Ye bhi kar sakta hun 
# Horiz adding 

df = pd.concat([nov, dec], axis = 1)
print(df)

shape = df = pd.concat([nov, dec], axis = 1).shape
print(shape)