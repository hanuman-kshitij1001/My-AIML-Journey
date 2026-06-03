# Item_Size: Ye batata Hia Ki Haar item Memory Me kitna Size occupy karta hai Item Matlb Elemets 

import numpy as np

#Ex1:
a = np.array([1,2,3])
print(a.itemsize)    # 8  Out put ayagea

#Ex2:
b = np.array([[1,2,3], [1,2,3]])
print(b.itemsize)    # 8 Out put ayagea

#Ex3:
c = np.array([[[1,2,3]]])
print(c.itemsize)    # 8 Out put ayagea


# Yah Sara 8 A raha hai Kyu Ki Int 8 bit ka hota hai kya Nahi Ye System p esayad depend karta hai 
# Ye Baat Rakhna Ki Int 32 jo hota hai Wo 4 Bit Let ahia aur 64 bit hamesa 8 bit leta hai float ke barabar