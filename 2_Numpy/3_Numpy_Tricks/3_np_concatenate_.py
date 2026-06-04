# Genrally Haam Esse 2-D Arrays Ke sath Kar rahe honge 
# Ye Array ko Concatination ka deta hai 
# Note:
# concatenate karte waqt dono arrays ki dimensions same honi chahiye. Ek 1D aur doosri 2D hai, isliye error aayega:

import numpy as np
a = np.random.randint(1,100,15)
b = np.random.randint(1,100,25)

#Ye Dono Ek Sath Mill Jayenge Esli Ko Bolte hia Concatination 
c = np.concatenate((a,b),axis=0)
# Yaha Axis = 1 Nahi Chalega Kyu Col Me Nahi KAr sake one Dim Hai Esliye
print(c)



# 2-d me Dekh lete hai 
d = np.random.randint(1,100,24).reshape(6,4)
m = np.random.randint(1,100,30).reshape(6,5)
print(m)

n = np.concatenate((d,m), axis = 1)
print(n)


# Accha Ek Baat AUr Mai Yaha Pe v.stack aur hstack Ko Usse na Karke Mai ye Use kar sakta hun 